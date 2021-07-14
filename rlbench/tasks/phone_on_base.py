from typing import List

from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from PyRep.pyrep.objects.shape import Shape

from RLBench.rlbench.backend.conditions import DetectedCondition, NothingGrasped
from RLBench.rlbench.backend.task import Task


class PhoneOnBase(Task):

    def init_task(self) -> None:
        phone = Shape('phone')
        self.register_graspable_objects([phone])
        self.register_success_conditions([
            DetectedCondition(phone, ProximitySensor('success')),
            NothingGrasped(self.robot.gripper)
        ])

    def init_episode(self, index: int) -> List[str]:
        return ['put the phone on the base',
                'put the phone on the stand',
                'put the hone on the hub',
                'grasp the phone and put it on the base',
                'place the phone on the base',
                'put the phone back on the base']

    def variation_count(self) -> int:
        return 1
