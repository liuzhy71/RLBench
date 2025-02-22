from typing import List, Tuple
from PyRep.pyrep.objects.shape import Shape
from PyRep.pyrep.objects.object import Object
from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from RLBench.rlbench.backend.task import Task
from RLBench.rlbench.backend.conditions import DetectedCondition, NothingGrasped


class OpenOven(Task):

    def init_task(self) -> None:
        self.register_success_conditions(
            [DetectedCondition(Shape('oven_door'), ProximitySensor('success')),
             NothingGrasped(self.robot.gripper)])

    def init_episode(self, index: int) -> List[str]:
        return ['open the oven',
                'open the oven door',
                'grab hold of the the handle and pull the oven door open']

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, -3.14 / 4.], [0, 0, 3.14 / 4.]

    def boundary_root(self) -> Object:
        return Shape('oven_boundary_root')
