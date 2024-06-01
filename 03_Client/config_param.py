import carla
from carla_msgs.msg import (CarlaWorldInfo, CarlaTrafficSign, CarlaTrafficSignList)
from geometry_msgs.msg import Pose

class ParkingScenario():
        def __init__(self):
            self.parking_first_point = 0.0
            self.vehicle_init_position  = [
                carla.Transform(carla.Location(x=-270, y=40, z=0.5), carla.Rotation(yaw=270))]
            self.vehicle_init_position_scene  = [
                carla.Transform(carla.Location(x=-270, y=67, z=0.5), carla.Rotation(yaw=270)),
                carla.Transform(carla.Location(x=115.2, y=2.1, z=0.05), carla.Rotation(yaw=0)),
                carla.Transform(carla.Location(x=151, y=16, z=0.05), carla.Rotation(yaw=90)),
                carla.Transform(carla.Location(x=190, y=-114, z=0.05), carla.Rotation(yaw=90)),
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

            self.lane_area_1 = [
                (153.7, -38.1),  # Point 1 (x, y)
                (153.7, -9.1),  # Point 2 (x, y)
                (148.5, -9.1),  # Point 3 (x, y)
                (148.5, -38.1)   # Point 4 (x, y)
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

            turn_left_tranform = Pose()
            turn_left_tranform.position.x = 142
            turn_left_tranform.position.y = 6.5
            turn_left_tranform.position.z = 0.05

            speed_limited_30_tranform = Pose()
            speed_limited_30_tranform.position.x = 185.5
            speed_limited_30_tranform.position.y = -98
            speed_limited_30_tranform.position.z = 0.05

            speed_limited_90_tranform = Pose()
            speed_limited_90_tranform.position.x = 186.5
            speed_limited_90_tranform.position.y = 33.7
            speed_limited_90_tranform.position.z = 0.05

            self.stop_sign = CarlaTrafficSign()
            self.stop_sign.id = 1
            self.stop_sign.transform = tranform
            self.stop_sign.type = sign_stop

            self.sign_speed_limited_30 = CarlaTrafficSign()
            self.sign_speed_limited_30.id = 2
            self.sign_speed_limited_30.transform = speed_limited_30_tranform
            self.sign_speed_limited_30.type = sign_speed_limited_30

            self.sign_speed_limited_90 = CarlaTrafficSign()
            self.sign_speed_limited_90.id = 3
            self.sign_speed_limited_90.transform = speed_limited_90_tranform
            self.sign_speed_limited_90.type = sign_speed_limited_90

            self.sign_direct_turn_left = CarlaTrafficSign()
            self.sign_direct_turn_left.id = 4
            self.sign_direct_turn_left.transform = turn_left_tranform
            self.sign_direct_turn_left.type = sign_direct_left_turn

            self.sign_direct_straight = CarlaTrafficSign()
            self.sign_direct_straight.id = 5
            self.sign_direct_straight.transform = tranform
            self.sign_direct_straight.type = sign_direct_straight

            self.sign_prohibiting_straight_turn = CarlaTrafficSign()
            self.sign_prohibiting_straight_turn.id = 6
            self.sign_prohibiting_straight_turn.transform = tranform
            self.sign_prohibiting_straight_turn.type = sign_prohibiting_straight_turn
            
            self.traffic_sign_list = CarlaTrafficSignList([self.stop_sign, self.sign_speed_limited_30, self.sign_speed_limited_90, self.sign_direct_turn_left, self.sign_direct_straight, self.sign_prohibiting_straight_turn])
            # print(self.traffic_sign_list)

