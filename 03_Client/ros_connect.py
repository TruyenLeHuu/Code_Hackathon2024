#!/usr/bin/env python

import rospy
import json
import math
from std_msgs.msg import String, Bool
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from carla_msgs.msg import CarlaEgoVehicleControl
from carla_msgs.msg import (CarlaEgoVehicleStatus, CarlaEgoVehicleInfo, CarlaWorldInfo, CarlaEgoVehicleObstacle,
                            CarlaActorList, CarlaTrafficLightStatusList, CarlaTrafficLightList, CarlaTrafficLight, CarlaTrafficSignList,
                            CarlaTrafficLightInfoList, CarlaEgoVehicleControl, CarlaEgoVehicleDoorStatus)
from config_param import RoundOneScenario

class RosConnect():
    def __init__(self, _vehicle_controller):
        self.hud = None
        self.world_carla = None
        self.controller = None
        self.roundOneScenario = RoundOneScenario()
        self.vehicle_controller = _vehicle_controller
        self.tfl_134_status = 0
        self.slot = -1
        self.sleep_status = 0
        self.sleep_detection_command_brake = 0
        self.weather = None
        self.is_obstacle = False
        self.obstacle_actor = "None"
        self.obstacle_distance = 0
        self.counter = 0
        self.alive_counter = 0
        self.traffic_light_info = None
        self.traffic_light_list = CarlaTrafficLightList()
        self.get_traffic_light_info()
        self.pub = rospy.Publisher('chatter', String, queue_size=10)
        self.pub_control = rospy.Publisher('/carla/hero/vehicle_control_cmd', CarlaEgoVehicleControl, queue_size=10)
        self.pub_door_status = rospy.Publisher('/carla/hero/vehicle_door_status', CarlaEgoVehicleDoorStatus, queue_size=10)
        self.pub_weather_status = rospy.Publisher('/carla/weather_status', String, queue_size=10)
        self.pub_traffic_sign_info = rospy.Publisher('/carla/traffic_sign_info', CarlaTrafficSignList, queue_size=10)
        self.pub_traffic_light_status = rospy.Publisher('/carla/traffic_light_status', CarlaTrafficLightList, queue_size=10)
        self.pub_collision = rospy.Publisher('/carla/hero/collision', Float32, queue_size=10)
        self.pub_steer = rospy.Publisher('steering', String, queue_size=10)
        self.pub_brake = rospy.Publisher('brake', String, queue_size=10)
        self.pub_speed = rospy.Publisher('speed', String, queue_size=10)
        self.pub_obstacle_distance = rospy.Publisher('/carla/hero/obstacle', CarlaEgoVehicleObstacle, queue_size=10)
        self.pub_is_correct_lane = rospy.Publisher('/carla/hero/is_correct_lane', Bool, queue_size=10)
        self.pub_current_lane = rospy.Publisher('/carla/hero/current_lane', String, queue_size=10)
        self.pub_run_time = rospy.Publisher('/carla/hero/run_time', Int32, queue_size=10)
        self.pub_is_in_checkpoint = rospy.Publisher('/carla/hero/is_in_checkpoint', Bool, queue_size=10)

        rospy.Subscriber('/carla/hero/vehicle_control_light', String, self.control_light)
        rospy.Subscriber('/carla/hero/vehicle_toggle_FR_door', Int32, self.toggle_FR_door)
        rospy.Subscriber('/carla/hero/vehicle_toggle_FL_door', Int32, self.toggle_FL_door)
        rospy.Subscriber('/carla/hero/vehicle_toggle_RR_door', Int32, self.toggle_RR_door)
        rospy.Subscriber('/carla/hero/vehicle_toggle_RL_door', Int32, self.toggle_RL_door)
        rospy.Subscriber('/carla/traffic_light/status', CarlaTrafficLightStatusList, self.get_traffic_status)
        rospy.Subscriber('/carla/start_scene', Int32, self.spawn_scene)
        
    def is_in_checkpoint_publish(self, is_in_checkpoint):
        self.pub_is_in_checkpoint.publish(is_in_checkpoint)

    def spawn_scene(self, msg):
        if (msg.data == 1):
            self.controller.respawn_car_scene_1(self.world_carla)
        elif (msg.data == 2):
            self.controller.respawn_car_scene_2()
        elif (msg.data == 3):
            self.controller.respawn_car_scene_3()
        elif (msg.data == 4):
            self.controller.respawn_car_scene_4(self.world_carla)
        elif (msg.data == 5):
            self.controller.respawn_car_scene_5()

    def take_hud(self, _hud):
        self.hud = _hud
    
    def take_controller_and_world(self, _controller, _world_carla):
        self.controller = _controller
        self.world_carla = _world_carla

    def toggle_FR_door(self, msg):
        if (msg.data):
            self.vehicle_controller.toggle_FR_door()

    def toggle_FL_door(self, msg):
        if (msg.data):
            self.vehicle_controller.toggle_FL_door()

    def toggle_RR_door(self, msg):
        if (msg.data):
            self.vehicle_controller.toggle_RR_door()

    def toggle_RL_door(self, msg):
        if (msg.data):
            self.vehicle_controller.toggle_RL_door()

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    
    def get_traffic_light_info(self):
        msg = rospy.wait_for_message(
            "/carla/traffic_light/info", CarlaTrafficLightInfoList, timeout=10)
        self.traffic_light_info = msg

        index = 0
        self.index_1 = 0
        self.distance_1 = 1000
        for traffic_info in self.traffic_light_info.traffic_lights:
            if (self.distance(traffic_info.transform.position.x, traffic_info.transform.position.y, self.roundOneScenario.traffic_light_transform[0].location.x,\
                               self.roundOneScenario.traffic_light_transform[0].location.y) < self.distance_1):
                self.index_1 = index
                self.distance_1 = self.distance(traffic_info.transform.position.x, traffic_info.transform.position.y, self.roundOneScenario.traffic_light_transform[0].location.x,\
                               self.roundOneScenario.traffic_light_transform[0].location.y)
            index+=1

    def set_obstacle(self, obstacle_actor, obstacle_distance):
        self.obstacle_actor = obstacle_actor
        self.obstacle_distance = obstacle_distance

    def set_weather(self, weather_status):
        self.weather = weather_status

    def keep_topic_alive(self):
        if (self.alive_counter > 60):
            # control_pub = rospy.Publisher('/carla/hero/vehicle_toggle_FL_door', Int32, queue_size=1)
            # control_pub.publish(0)
            self.alive_counter = 0
        else:
            self.alive_counter = self.alive_counter + 1
    def publish_obstacle_distance(self):
        if (self.counter > 5):
            obstacle = CarlaEgoVehicleObstacle()
            obstacle.is_obstacle = False
            obstacle.obstacle_actor = self.obstacle_actor
            obstacle.obstacle_distance = self.obstacle_distance
            self.pub_obstacle_distance.publish(obstacle)
            self.counter = 0
        else:
            self.counter = self.counter + 1

    def publish_status(self):
        self.pub_door_status.publish(self.vehicle_controller.get_door_status())
        self.pub_weather_status.publish(self.weather)
        self.pub_is_correct_lane.publish(not self.hud.is_minus)
        self.pub_run_time.publish(int(self.hud.run_time))
        if (self.hud.is_lane_1):
            self.pub_current_lane.publish("right")
        else:
            self.pub_current_lane.publish("left")
    
    def publish_collision(self, collision):
        self.pub_collision.publish(collision)
    
    def publish_traffic_sign_info(self):
        self.pub_traffic_sign_info.publish(self.roundOneScenario.traffic_sign_list_3)
        
    def vehicle_control_with_ros(self, control_throttle, control_steer, control_brake, 
                                 vehicle_reverse = False, vehicle_handbrake = False, vehicle_mg_shift = False, vehicle_gear = 0):
        control_msg = CarlaEgoVehicleControl()
        control_msg.throttle = control_throttle
        control_msg.steer = control_steer
        control_msg.brake = control_brake
        control_msg.reverse = vehicle_reverse
        control_msg.hand_brake = vehicle_handbrake
        control_msg.manual_gear_shift = vehicle_mg_shift
        control_msg.gear = vehicle_gear
        self.pub_control.publish(control_msg)

    def get_traffic_status(self, message):
        try:
            index = 0
            self.traffic_light_list.traffic_lights= []
            for traffic_status in message.traffic_lights:
                traffic_light = CarlaTrafficLight()
                traffic_light.id = traffic_status.id
                traffic_light.state = traffic_status.state
                traffic_light.transform = self.traffic_light_info.traffic_lights[index].transform
                if (index == self.index_1):
                    self.traffic_light_list.traffic_lights.append(traffic_light)
                index = index + 1
                # print(index)
            self.pub_traffic_light_status.publish(self.traffic_light_list)
            # print(self.traffic_light_list)
        except Exception as e:
            print("Error:", str(e))
    
    def control_door(self, message):
        try:
            self.vehicle_controller.set_door(message)
        except Exception as e:
            print("Error:", str(e))

    def control_light(self, message):
        print(message)
        try:
            if message.data == "on" or message.data == "ON" or message.data == "On" or message.data == "oN":
                self.vehicle_controller.set_light_on()
            else:
                self.vehicle_controller.set_light_off()
        except Exception as e:
            print("Error:", str(e))

    def publish_speed(self, speed):
        self.pub_speed.publish(str(speed))
    
    def publish_brake(self, brake):
        self.pub_brake.publish(str(brake))
    
    def publish_steer(self, steering):
        self.pub_steer.publish(str(steering))

