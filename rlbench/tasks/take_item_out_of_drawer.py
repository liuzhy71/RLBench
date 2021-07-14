from typing import List
from PyRep.pyrep.objects.dummy import Dummy
from PyRep.pyrep.objects.joint import Joint
from PyRep.pyrep.objects.shape import Shape
from PyRep.pyrep.objects.proximity_sensor import ProximitySensor
from RLBench.rlbench.backend.task import Task
from RLBench.rlbench.backend.conditions import DetectedCondition

OPTIONS = ['bottom', 'middle', 'top']


class TakeItemOutOfDrawer(Task):

    def init_task(self) -> None:
        self.anchors = [Dummy('waypoint_anchor_%s' % opt)
                        for opt in OPTIONS]
        self.joints = [Joint('drawer_joint_%s' % opt)
                       for opt in OPTIONS]
        self.waypoint1 = Dummy('waypoint1')
        self.item = Shape('item')
        self.register_graspable_objects([self.item])

    def init_episode(self, index: int) -> List[str]:
        option = OPTIONS[index]
        anchor = self.anchors[index]
        self.waypoint1.set_position(anchor.get_position())
        _, _, z_target = anchor.get_position()
        x, y, z = self.item.get_position()
        self.item.set_position([x, y, z_target])
        success_sensor = ProximitySensor('success_' + option)
        self.register_success_conditions(
            [DetectedCondition(self.item, success_sensor, negated=True)])
        return ['take item out of the %s drawer' % option,
                'open the %s drawer and take the cube out' % option,
                'grasp the %s handle on the drawers, pull the drawer open, and'
                ' take out what you find inside' % option,
                'clear out the %s drawer' % option,
                'make sure the %s drawer is empty' % option,
                'lift the block out of the %s drawer' % option,
                'using the handle, open the %s drawer, and remove any items #'
                'inside' % option]

    def variation_count(self) -> int:
        return 3
