from typing import List, Tuple
import numpy as np
from PyRep.pyrep.objects.shape import Shape
from PyRep.pyrep.objects.joint import Joint
from PyRep.pyrep.objects.object import Object
from RLBench.rlbench.backend.task import Task
from RLBench.rlbench.backend.conditions import JointCondition


class CloseMicrowave(Task):

    def init_task(self) -> None:
        self.register_success_conditions([JointCondition(
            Joint('microwave_door_joint'), np.deg2rad(40))])

    def init_episode(self, index: int) -> List[str]:
        return ['close microwave',
                'shut the microwave',
                'close the microwave door',
                'push the microwave door shut']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, -3.14 / 4.], [0, 0, 3.14 / 4.]

    def boundary_root(self) -> Object:
        return Shape('boundary_root')
