import carla
from carla_msgs.msg import (CarlaWorldInfo, CarlaTrafficSign, CarlaTrafficSignList)
from geometry_msgs.msg import Pose

class ParkingScenario():
        def __init__(self):
            self.parking_first_point = 0.0
            self.vehicle_init_position  = [
                carla.Transform(carla.Location(x=-270, y=40, z=0.5), carla.Rotation(yaw=270))]
            self.vehicle_init_position_scene  = [
                carla.Transform(carla.Location(x=47.00, y=-146.10, z=1), carla.Rotation(yaw=3)),
                carla.Transform(carla.Location(x=150.60, y=-90.30, z=0.05), carla.Rotation(yaw=90)),
                carla.Transform(carla.Location(x=116.6, y=-2.3, z=0.05), carla.Rotation(yaw=180)),
                carla.Transform(carla.Location(x=-1.5, y=-17.5, z=0.05), carla.Rotation(yaw=-90)),
                carla.Transform(carla.Location(x=-1.5, y=-18.6, z=0.05), carla.Rotation(yaw=-90))]

class RoundOneScenario():
        def __init__(self):

            stop_traffic_sign_bp = "static.prop.stop"
            speed_limit_sign_30_bp = "static.prop.speedlimit.30"
            speed_limit_sign_40_bp = "static.prop.speedlimit.40"
            speed_limit_sign_50_bp = "static.prop.speedlimit.50"
            speed_limit_sign_60_bp = "static.prop.speedlimit.60"
            speed_limit_sign_90_bp = "static.prop.speedlimit.90"
            left_sign_pb = "static.prop.arrowleft"
            right_sign_pb = "static.prop.arrowright"
            straight_sign_pb = "static.prop.arrowstraight"
            crosswalk_sign_pb = "static.prop.crosswalk"

            sign_stop = 1
            sign_speed_limited_30 = 2
            sign_speed_limited_60 = 3
            sign_speed_limited_90 = 4
            sign_direct_left_turn = 5
            sign_direct_right_turn = 6
            sign_direct_straight = 7
            sign_prohibiting_right_turn = 8
            sign_prohibiting_left_turn = 9
            sign_prohibiting_straight_turn = 10
            
            self.check_point_1 = [
                (80.70, -151.90),  # Point 1 (x, y)
                (80.00, -140.3),  # Point 2 (x, y)
                (84.10, -140.1),  # Point 3 (x, y)
                (85.00, -151.30)   # Point 4 (x, y)
            ]

            self.check_point_2 = [
                (124.10, 5.40),  # Point 1 (x, y)
                (129.10, 5.3),  # Point 2 (x, y)
                (129.20, -5.8),  # Point 3 (x, y)
                (124.10, -5.8)   # Point 4 (x, y)
            ]
            self.check_point_3 = [
                (187.4, 61.8),  # Point 1 (x, y)
                (198.4, 61.8),  # Point 2 (x, y)
                (198.4, 65.9),  # Point 3 (x, y)
                (187.4, 65.9)   # Point 4 (x, y)
            ]
            self.check_point_4 = [
                (-170, 9),  # Point 1 (x, y)
                (-170, -6.6),  # Point 2 (x, y)
                (-178, -6.6),  # Point 3 (x, y)
                (-178, 9)   # Point 4 (x, y)
            ]
            self.lane_area_1 = [
                (143.80, -0.30),  # Point 1 (x, y)
                (143.80, 5.20),  # Point 2 (x, y)
                (129.10, 5.20),  # Point 3 (x, y)
                (129.10, -0.30)   # Point 4 (x, y)
            ]

            self.lane_area_1_4 = [
                (153.3, 12),  # Point 1 (x, y)
                (153.3, 90.4),  # Point 2 (x, y)
                (147.4, 90.4),  # Point 3 (x, y)
                (147.4, 12)   # Point 4 (x, y)
            ]

            self.traffic_area_1 = [
                (19.5, 9.2),  # Point 1 (x, y)
                (19.5, -9.2),  # Point 2 (x, y)
                (40, -9.2),  # Point 3 (x, y)
                (40, 9.2)   # Point 4 (x, y)
            ]

            self.weather_area_1 = [
                (15, 82),  # Point 1 (x, y)
                (15, 99),  # Point 2 (x, y)
                (-60, 99),  # Point 3 (x, y)
                (-60, 82)   # Point 4 (x, y)
            ]

            self.weather_area_2 = [
                (-40, 76),  # Point 1 (x, y)
                (-59, 76),  # Point 2 (x, y)
                (-59, 30),  # Point 3 (x, y)
                (-40, 30)   # Point 4 (x, y)
            ]

            self.parking_first_point = 0.0
            self.vehicle_init_position  = [
                carla.Transform(carla.Location(x=-265, y=-10, z=0.05), carla.Rotation(yaw=270))]
            
            self.traffic_light_transform  = [
                carla.Transform(carla.Location(x=145.6237890, y=-62.24490234, z=0.05), carla.Rotation(yaw=270)),]

            #   Stop = 1
            #   Speed Limited 40 = 2
            #   Speed Limited 60 = 3
            #   Speed Limited 90 = 4
            #   Direct Turn Left = 5
            #   Direct Turn Right = 6
            #   Direct Straight = 7
            #   Prohibiting right turn = 8
            #   Prohibiting left turn = 9
            #   Prohibiting straight turn = 10
            tranform = Pose()
            tranform.position.x = 265
            tranform.position.y = -10
            tranform.position.z = 0.05

            turn_right_tranform = Pose()
            turn_right_tranform.position.x = 145.50
            turn_right_tranform.position.y = -10.50
            turn_right_tranform.position.z = 0.05

            speed_limited_30_tranform = Pose()
            speed_limited_30_tranform.position.x = 89.30
            speed_limited_30_tranform.position.y = -8.60
            speed_limited_30_tranform.position.z = 0.05

            speed_limited_60_tranform = Pose()
            speed_limited_60_tranform.position.x = 16.10
            speed_limited_60_tranform.position.y = -8.20
            speed_limited_60_tranform.position.z = 0.05

            speed_limited_90_tranform = Pose()
            speed_limited_90_tranform.position.x = -62.10
            speed_limited_90_tranform.position.y = -8.20
            speed_limited_90_tranform.position.z = 0.05

            self.stop_sign = CarlaTrafficSign()
            self.stop_sign.id = 1
            self.stop_sign.transform = tranform
            self.stop_sign.type = sign_stop

            self.sign_speed_limited_30 = CarlaTrafficSign()
            self.sign_speed_limited_30.id = 1
            self.sign_speed_limited_30.transform = speed_limited_30_tranform
            self.sign_speed_limited_30.type = sign_speed_limited_30

            self.sign_speed_limited_60 = CarlaTrafficSign()
            self.sign_speed_limited_60.id = 2
            self.sign_speed_limited_60.transform = speed_limited_60_tranform
            self.sign_speed_limited_60.type = sign_speed_limited_60
            
            self.sign_speed_limited_90 = CarlaTrafficSign()
            self.sign_speed_limited_90.id = 3
            self.sign_speed_limited_90.transform = speed_limited_90_tranform
            self.sign_speed_limited_90.type = sign_speed_limited_90

            self.sign_direct_right_turn = CarlaTrafficSign()
            self.sign_direct_right_turn.id = 4
            self.sign_direct_right_turn.transform = turn_right_tranform
            self.sign_direct_right_turn.type = sign_direct_right_turn

            self.sign_direct_straight = CarlaTrafficSign()
            self.sign_direct_straight.id = 5
            self.sign_direct_straight.transform = tranform
            self.sign_direct_straight.type = sign_direct_straight

            self.sign_prohibiting_straight_turn = CarlaTrafficSign()
            self.sign_prohibiting_straight_turn.id = 6
            self.sign_prohibiting_straight_turn.transform = tranform
            self.sign_prohibiting_straight_turn.type = sign_prohibiting_straight_turn
            
            # self.traffic_sign_list = CarlaTrafficSignList([self.stop_sign, self.sign_speed_limited_30, self.sign_speed_limited_90, self.sign_direct_turn_left, self.sign_direct_straight, self.sign_prohibiting_straight_turn])
            # print(self.traffic_sign_list)
            # self.traffic_sign_list_2 = CarlaTrafficSignList([self.sign_direct_right_turn])
            self.traffic_sign_list_3 = CarlaTrafficSignList([self.sign_direct_right_turn, self.sign_speed_limited_30, self.sign_speed_limited_60, self.sign_speed_limited_90])

