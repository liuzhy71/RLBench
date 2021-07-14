from typing import List
from PyRep.pyrep.objects.dummy import Dummy
from PyRep.pyrep.objects.joint import Joint
from PyRep.pyrep.objects.shape import Shape
from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from RLBench.rlbench.backend.task import Task
from RLBench.rlbench.backend.conditions import DetectedCondition

OPTIONS = ['bottom', 'middle', 'top']


class PutItemInDrawer(Task):

    def init_task(self) -> None:
        self.anchors = [Dummy('waypoint_anchor_%s' % opt)
                        for opt in OPTIONS]
        self.joints = [Joint('drawer_joint_%s' % opt)
                       for opt in OPTIONS]
        self.waypoint1 = Dummy('waypoint1')
        self.item = Shape('item')
        self.register_graspable_objects([self.item])

    def init_episode(self, index) -> List[str]:
        option = OPTIONS[index]
        anchor = self.anchors[index]
        self.waypoint1.set_position(anchor.get_position())
        success_sensor = ProximitySensor('success_' + option)
        self.register_success_conditions(
            [DetectedCondition(self.item, success_sensor)])
        return ['put item in %s drawer' % option,
                'put the block away in the %s drawer' % option,
                'open the %s drawer and place the block inside of it' % option,
                'leave the block in the %s drawer' % option]

    def variation_count(self) -> int:
        return 3
