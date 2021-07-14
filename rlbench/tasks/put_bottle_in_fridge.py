from typing import List, Tuple

import numpy as np
fromRLBench.rlbench.objects.object import Object
from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from PyRep.pyrep.objects.shape import Shape

from RLBench.rlbench.backend.conditions import DetectedCondition, NothingGrasped
from RLBench.rlbench.backend.task import Task


class PutBottleInFridge(Task):

    def init_task(self) -> None:
        bottle = Shape('bottle')
        success_sensor = ProximitySensor('success')
        self.register_graspable_objects([bottle])
        self.register_success_conditions(
            [DetectedCondition(bottle, success_sensor),
             NothingGrasped(self.robot.gripper)])

    def init_episode(self, index: int) -> List[str]:
        return ['put bottle in fridge',
                'place the bottle inside the fridge',
                'open the fridge and put the bottle in there',
                'open the fridge door, pick up the bottle, and leave it in the '
                'fridge']

    def variation_count(self) -> int:
        return 1

    def boundary_root(self) -> Object:
        return Shape('fridge_root')

    def base_rotation_bounds(self) -> Tuple[Tuple[float, float, float],
                                            Tuple[float, float, float]]:
        return (0.0, 0.0, -np.pi/4), (0.0, 0.0, np.pi/4)
