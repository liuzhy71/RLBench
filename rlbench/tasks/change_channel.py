from typing import List, Tuple
from RLBench.rlbench.backend.task import Task
from RLBench.rlbench.backend.conditions import JointCondition, DetectedCondition
from PyRep.pyrep.objects.shape import Shape
from PyRep.pyrep.objects.joint import Joint
from PyRep.pyrep.objects.dummy import Dummy
from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from RLBench.rlbench.backend.spawn_boundary import SpawnBoundary
import numpy as np


class ChangeChannel(Task):

    def init_task(self) -> None:
        self._remote = Shape('tv_remote')
        self._joint_conditions = [
            JointCondition(Joint('target_button_joint1'), 0.003),
            JointCondition(Joint('target_button_joint2'), 0.003)
        ]
        self._w6 = Dummy('waypoint6')
        self._w6z = self._w6.get_position()[2]
        self.register_graspable_objects([self._remote])
        self._spawn_boundary = SpawnBoundary([Shape('spawn_boundary')])
        self._target_buttons = [
            Shape('target_button_wrap1'), Shape('target_button_wrap2')]

    def init_episode(self, index: int) -> List[str]:
        detectors = [ProximitySensor('success%d' % i) for i in range(2)]
        self.register_success_conditions([
            self._joint_conditions[index],
            DetectedCondition(self._remote, detectors[0]),
            DetectedCondition(self._remote, detectors[1])
        ])
        x, y, _ = self._target_buttons[index % 2].get_position()
        self._w6.set_position([x, y, self._w6z])
        self._spawn_boundary.clear()
        self._spawn_boundary.sample(self._remote)
        btn = ['plus', 'minus']
        chnl = ['up', 'minus']
        return ['turn the channel %s' % chnl[index],
                'change the television channel %s' % chnl[index],
                'point the remote at the tv and press the %s button to turn '
                'the channel %s' % (btn[index], chnl[index]),
                'using the tv remote, ensure it is facing the television and '
                'press the %s button to increment the channel %s by one'
                % (btn[index], chnl[index]),
                'find the %s button on the remote, rotate the remote such that'
                ' it is pointed at the tv, then press the button to change '
                'the channel %s' % (chnl[index], btn[index])]

    def variation_count(self) -> int:
        return 2

    def base_rotation_bounds(self) -> Tuple[Tuple[float, float, float],
                                            Tuple[float, float, float]]:
        return (0.0, 0.0, -0.5*np.pi), (0.0, 0.0, +0.5 * np.pi)
