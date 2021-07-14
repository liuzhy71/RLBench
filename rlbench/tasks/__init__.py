from RLBench.rlbench.tasks.beat_the_buzz import BeatTheBuzz
from RLBench.rlbench.tasks.block_pyramid import BlockPyramid
from RLBench.rlbench.tasks.change_channel import ChangeChannel
from RLBench.rlbench.tasks.change_clock import ChangeClock
from RLBench.rlbench.tasks.close_box import CloseBox
from RLBench.rlbench.tasks.close_door import CloseDoor
from RLBench.rlbench.tasks.close_drawer import CloseDrawer
from RLBench.rlbench.tasks.close_fridge import CloseFridge
from RLBench.rlbench.tasks.close_grill import CloseGrill
from RLBench.rlbench.tasks.close_jar import CloseJar
from RLBench.rlbench.tasks.close_laptop_lid import CloseLaptopLid
from RLBench.rlbench.tasks.close_microwave import CloseMicrowave
from RLBench.rlbench.tasks.empty_container import EmptyContainer
from RLBench.rlbench.tasks.empty_dishwasher import EmptyDishwasher
from RLBench.rlbench.tasks.get_ice_from_fridge import GetIceFromFridge
from RLBench.rlbench.tasks.hang_frame_on_hanger import HangFrameOnHanger
from RLBench.rlbench.tasks.hannoi_square import HannoiSquare
from RLBench.rlbench.tasks.hit_ball_with_queue import HitBallWithQueue
from RLBench.rlbench.tasks.hockey import Hockey
from RLBench.rlbench.tasks.insert_usb_in_computer import InsertUsbInComputer
from RLBench.rlbench.tasks.lamp_off import LampOff
from RLBench.rlbench.tasks.lamp_on import LampOn
from RLBench.rlbench.tasks.light_bulb_in import LightBulbIn
from RLBench.rlbench.tasks.light_bulb_out import LightBulbOut
from RLBench.rlbench.tasks.meat_off_grill import MeatOffGrill
from RLBench.rlbench.tasks.meat_on_grill import MeatOnGrill
from RLBench.rlbench.tasks.move_hanger import MoveHanger
from RLBench.rlbench.tasks.open_box import OpenBox
from RLBench.rlbench.tasks.open_door import OpenDoor
from RLBench.rlbench.tasks.open_drawer import OpenDrawer
from RLBench.rlbench.tasks.open_fridge import OpenFridge
from RLBench.rlbench.tasks.open_grill import OpenGrill
from RLBench.rlbench.tasks.open_jar import OpenJar
from RLBench.rlbench.tasks.open_microwave import OpenMicrowave
from RLBench.rlbench.tasks.open_oven import OpenOven
from RLBench.rlbench.tasks.open_window import OpenWindow
from RLBench.rlbench.tasks.open_wine_bottle import OpenWineBottle
from RLBench.rlbench.tasks.phone_on_base import PhoneOnBase
from RLBench.rlbench.tasks.pick_and_lift import PickAndLift
from RLBench.rlbench.tasks.pick_up_cup import PickUpCup
from RLBench.rlbench.tasks.place_cups import PlaceCups
from RLBench.rlbench.tasks.place_hanger_on_rack import PlaceHangerOnRack
from RLBench.rlbench.tasks.place_shape_in_shape_sorter import PlaceShapeInShapeSorter
from RLBench.rlbench.tasks.play_jenga import PlayJenga
from RLBench.rlbench.tasks.plug_charger_in_power_supply import PlugChargerInPowerSupply
from RLBench.rlbench.tasks.pour_from_cup_to_cup import PourFromCupToCup
from RLBench.rlbench.tasks.press_switch import PressSwitch
from RLBench.rlbench.tasks.push_button import PushButton
from RLBench.rlbench.tasks.push_buttons import PushButtons
from RLBench.rlbench.tasks.put_all_groceries_in_cupboard import PutAllGroceriesInCupboard
from RLBench.rlbench.tasks.put_books_on_bookshelf import PutBooksOnBookshelf
from RLBench.rlbench.tasks.put_bottle_in_fridge import PutBottleInFridge
from RLBench.rlbench.tasks.put_groceries_in_cupboard import PutGroceriesInCupboard
from RLBench.rlbench.tasks.put_item_in_drawer import PutItemInDrawer
from RLBench.rlbench.tasks.put_knife_in_knife_block import PutKnifeInKnifeBlock
from RLBench.rlbench.tasks.put_knife_on_chopping_board import PutKnifeOnChoppingBoard
from RLBench.rlbench.tasks.put_money_in_safe import PutMoneyInSafe
from RLBench.rlbench.tasks.put_plate_in_colored_dish_rack import PutPlateInColoredDishRack
from RLBench.rlbench.tasks.put_rubbish_in_bin import PutRubbishInBin
from RLBench.rlbench.tasks.put_shoes_in_box import PutShoesInBox
from RLBench.rlbench.tasks.put_toilet_roll_on_stand import PutToiletRollOnStand
from RLBench.rlbench.tasks.put_tray_in_oven import PutTrayInOven
from RLBench.rlbench.tasks.put_umbrella_in_umbrella_stand import PutUmbrellaInUmbrellaStand
from RLBench.rlbench.tasks.reach_and_drag import ReachAndDrag
from RLBench.rlbench.tasks.reach_target import ReachTarget
from RLBench.rlbench.tasks.remove_cups import RemoveCups
from RLBench.rlbench.tasks.scoop_with_spatula import ScoopWithSpatula
from RLBench.rlbench.tasks.screw_nail import ScrewNail
from RLBench.rlbench.tasks.set_the_table import SetTheTable
from RLBench.rlbench.tasks.setup_checkers import SetupCheckers
from RLBench.rlbench.tasks.slide_block_to_target import SlideBlockToTarget
from RLBench.rlbench.tasks.slide_cabinet_open import SlideCabinetOpen
from RLBench.rlbench.tasks.slide_cabinet_open_and_place_cups import SlideCabinetOpenAndPlaceCups
from RLBench.rlbench.tasks.solve_puzzle import SolvePuzzle
from RLBench.rlbench.tasks.stack_blocks import StackBlocks
from RLBench.rlbench.tasks.stack_cups import StackCups
from RLBench.rlbench.tasks.stack_wine import StackWine
from RLBench.rlbench.tasks.straighten_rope import StraightenRope
from RLBench.rlbench.tasks.sweep_to_dustpan import SweepToDustpan
from RLBench.rlbench.tasks.take_cup_out_from_cabinet import TakeCupOutFromCabinet
from RLBench.rlbench.tasks.take_frame_off_hanger import TakeFrameOffHanger
from RLBench.rlbench.tasks.take_item_out_of_drawer import TakeItemOutOfDrawer
from RLBench.rlbench.tasks.take_lid_off_saucepan import TakeLidOffSaucepan
from RLBench.rlbench.tasks.take_money_out_safe import TakeMoneyOutSafe
from RLBench.rlbench.tasks.take_off_weighing_scales import TakeOffWeighingScales
from RLBench.rlbench.tasks.take_plate_off_colored_dish_rack import TakePlateOffColoredDishRack
from RLBench.rlbench.tasks.take_shoes_out_of_box import TakeShoesOutOfBox
from RLBench.rlbench.tasks.take_toilet_roll_off_stand import TakeToiletRollOffStand
from RLBench.rlbench.tasks.take_tray_out_of_oven import TakeTrayOutOfOven
from RLBench.rlbench.tasks.take_umbrella_out_of_umbrella_stand import TakeUmbrellaOutOfUmbrellaStand
from RLBench.rlbench.tasks.take_usb_out_of_computer import TakeUsbOutOfComputer
from RLBench.rlbench.tasks.toilet_seat_down import ToiletSeatDown
from RLBench.rlbench.tasks.toilet_seat_up import ToiletSeatUp
from RLBench.rlbench.tasks.turn_oven_on import TurnOvenOn
from RLBench.rlbench.tasks.turn_tap import TurnTap
from RLBench.rlbench.tasks.tv_off import TvOff
from RLBench.rlbench.tasks.tv_on import TvOn
from RLBench.rlbench.tasks.unplug_charger import UnplugCharger
from RLBench.rlbench.tasks.water_plants import WaterPlants
from RLBench.rlbench.tasks.weighing_scales import WeighingScales
from RLBench.rlbench.tasks.wipe_desk import WipeDesk

FS10_V1 = {
    'train': [
        ReachTarget,
        CloseBox,
        CloseMicrowave,
        PlugChargerInPowerSupply,
        ToiletSeatDown,
        TakeUmbrellaOutOfUmbrellaStand,
        PutUmbrellaInUmbrellaStand,
        SlideCabinetOpen,
        CloseFridge,
        PickAndLift
    ],
    'test': [
        OpenBox,
        OpenMicrowave,
        UnplugCharger,
        ToiletSeatUp,
        OpenFridge,
    ]
}

FS25_V1 = {
    'train': FS10_V1['train'] + FS10_V1['test'] + [
        TurnTap,
        LightBulbIn,
        TvOff,
        OpenWindow,
        CloseDoor,
        PushButton,
        PutItemInDrawer,
        OpenDrawer,
        CloseDrawer,
        TurnOvenOn
    ],
    'test': [
        LightBulbOut,
        TvOn,
        OpenOven,
        OpenDoor,
        TakeItemOutOfDrawer
    ]
}

FS50_V1 = {
    'train': FS25_V1['train'] + FS25_V1['test'] + [
        BeatTheBuzz,
        BlockPyramid,
        ChangeClock,
        CloseJar,
        CloseLaptopLid,
        EmptyContainer,
        EmptyDishwasher,
        GetIceFromFridge,
        HangFrameOnHanger,
        HannoiSquare,
        PutRubbishInBin,
        PutShoesInBox,
        PutToiletRollOnStand,
        PutTrayInOven,
        ReachAndDrag,
        RemoveCups,
        ScoopWithSpatula,
        SetTheTable,
        SetupCheckers,
        SlideBlockToTarget
    ],
    'test': [
        Hockey,
        InsertUsbInComputer,
        PressSwitch,
        PlayJenga,
        MeatOffGrill,
    ]
}

FS95_V1 = {
    'train': FS50_V1['train'] + FS50_V1['test'] + [
        HitBallWithQueue,
        ScrewNail,
        LampOff,
        LampOn,
        MeatOnGrill,
        MoveHanger,
        OpenJar,
        OpenWineBottle,
        PlaceCups,
        PlaceHangerOnRack,
        PlaceShapeInShapeSorter,
        PutBottleInFridge,
        PutKnifeInKnifeBlock,
        PutMoneyInSafe,
        PutPlateInColoredDishRack,
        SlideCabinetOpenAndPlaceCups,
        StackBlocks,
        StackCups,
        StackWine,
        StraightenRope,
        SweepToDustpan,
        TakeCupOutFromCabinet,
        TakeFrameOffHanger,
        TakeLidOffSaucepan,
        TakeMoneyOutSafe,
        TakeOffWeighingScales,
        TakePlateOffColoredDishRack,
        TakeShoesOutOfBox,
        TakeToiletRollOffStand,
        TakeUsbOutOfComputer,
        WaterPlants,
        WeighingScales,
        WipeDesk,
        ChangeChannel,
        OpenGrill,
        CloseGrill,
        SolvePuzzle,
        PickUpCup,
        PhoneOnBase,
        PourFromCupToCup
    ],
    'test': [
        PutKnifeOnChoppingBoard,
        PutBooksOnBookshelf,
        PushButtons,
        PutGroceriesInCupboard,
        TakeTrayOutOfOven,
    ]
}

MT15_V1 = {
    'train': FS10_V1['train'] + FS10_V1['test']
}


MT30_V1 = {
    'train': FS25_V1['train'] + FS25_V1['test']
}

MT55_V1 = {
    'train': FS50_V1['train'] + FS50_V1['test']
}

MT100_V1 = {
    'train': FS95_V1['train'] + FS95_V1['test']
}