from typing import List
from PyRep.pyrep.objects.shape import Shape
from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from RLBench.rlbench.backend.task import Task
from RLBench.rlbench.backend.conditions import DetectedCondition, NothingGrasped


class StackWine(Task):

    def init_task(self):
        wine_bottle = Shape('wine_bottle')
        self.register_graspable_objects([wine_bottle])
        self.register_success_conditions(
            [DetectedCondition(wine_bottle, ProximitySensor('success')),
             NothingGrasped(self.robot.gripper)])

    def init_episode(self, index: int) -> List[str]:
        return ['stack wine bottle',
                'slide the bottle onto the wine rack',
                'put the wine away',
                'leave the wine on the shelf',
                'grasp the bottle and put it away',
                'place the wine bottle on the wine rack']

    def variation_count(self) -> int:
        return 1
