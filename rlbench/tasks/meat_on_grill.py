from typing import List
from RLBench.rlbench.backend.task import Task
from RLBench.rlbench.backend.conditions import NothingGrasped, DetectedCondition
from PyRep.pyrep.objects.shape import Shape
from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from PyRep.pyrep.objects.dummy import Dummy

MEAT = ['chicken', 'steak']


class MeatOnGrill(Task):

    def init_task(self) -> None:
        self.steak = Shape('steak')
        self.chicken = Shape('chicken')
        self.success_sensor = ProximitySensor('success')
        self.register_graspable_objects([self.chicken, self.steak])
        self.w1 = Dummy('waypoint1')

    def init_episode(self, index: int) -> List[str]:
        conditions = [NothingGrasped(self.robot.gripper)]
        if index == 0:
            self.w1.set_position(
                [2.8756e-2, 4.9857e-3, 8.0645e-4],
                relative_to=self.chicken, reset_dynamics=False)
            conditions.append(
                DetectedCondition(self.chicken, self.success_sensor))
        else:
            self.w1.set_position(
                [-1.2818e-2, -4.4837e-3, -4.627e-3],
                relative_to=self.steak, reset_dynamics=False)
            conditions.append(
                DetectedCondition(self.steak, self.success_sensor))
        self.register_success_conditions(conditions)
        return ['put the %s on the grill' % MEAT[index],
                'pick up the %s and place it on the grill' % MEAT[index],
                'grill the %s' % MEAT[index]]

    def variation_count(self) -> int:
        return 2
