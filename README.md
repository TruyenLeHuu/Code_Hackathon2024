# #Code-Hackathon2024
Prepare API and Scenes for Code_LikeaBosch Hackathon2024

!! Caution Nguyen and Thien,...
!!! Don't replace all folder, just 03_Client and 04_Template
# Update
        get_is_in_checkpoint() API
        get_traffic_signs() just return one position of turn left traffic sign

# Spawn scene by using: 
        start_scene(number)
                number is 1 to 5 (scene 1 to 5)

# API for scene 1:
        - get_vehicle_obstacle()
        return value:   {   
                                is_obstacle: True/False
                                obstacle_actor: vehicle/walker
                                obstacle_distance: 5.243424241
                        }

        - get_collision()
        return int

        - get_run_time()
        return int (seconds)

# API for scene 2:
        - get_collision()
        return int

        - get_traffic_signs()
        """ Traffic sign value return position of turn left sign:
        {   
                x: 19.149999618530273
                y: 9.0
                z: 0.0
        }
        """

        - get_is_correct_lane()
        return bool (True if correct lane, False if not correct)

        - get_run_time()
        return int (seconds)

# API for scene 3:
        - get_collision()
        return int

        - get_traffic_signs()
        """ Traffic sign value return:
                {   
                        [{
                        id: 217,
                        transform: {
                                position:
                                x: 19.149999618530273
                                y: 9.0
                                z: 0.0
                                orientation:
                                x: 0.0
                                y: -0.0
                                z: -0.9999999999997784
                                w: 6.65790272530563e-07
                        },
                        type: 1/.../10      
                        },
                        {
                        id: 219,
                        transform: {
                                position:
                                x: 19.149999618530273
                                y: 9.0
                                z: 0.0
                                orientation:
                                x: 0.0
                                y: -0.0
                                z: -0.9999999999997784
                                w: 6.65790272530563e-07
                        },
                        type: 1/.../10      
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
                        },...
                        ]
                }

        - get_traffic_lights
        """ Traffic light value return:
        {   
                [{
                id: 213,
                transform: {
                        position:
                        x: 19.149999618530273
                        y: 9.0
                        z: 0.0
                        orientation:
                        x: 0.0
                        y: -0.0
                        z: -0.9999999999997784
                        w: 6.65790272530563e-07
                },
                state: 0/1/2 (RED=0 YELLOW=1 GREEN=2)
                },
                {
                id: 214,
                transform: {
                        position:
                        x: 19.149999618530273
                        y: 9.0
                        z: 0.0
                        orientation:
                        x: 0.0
                        y: -0.0
                        z: -0.9999999999997784
                        w: 6.65790272530563e-07
                },
                state: 0/1/2 (RED=0 YELLOW=1 GREEN=2)
                },...
                ]
        }

        - get_run_time()
        return int (seconds)

# API for scene 4:
        - get_collision()
        return int

        - get_vehicle_obstacle()
        return value:   {   
                                is_obstacle: True/False
                                obstacle_actor: vehicle/walker
                                obstacle_distance: 5.243424241
                        }

        - get_current_lane()
        return string ("left" or "right")

        - get_run_time()
        return int (seconds)

# API for scene 5: Updating...

# #How to run

Before run Framework, sure that you installed ROS (Noetic) and Carla (version >= 0.9.13).

# Initial
Step1: Build ros package 02_RosCommunication -> source to this package (run devel\setup.bat to link packet with terminal)

Step2: In the same terminal, build ros package 01_RosBridge -> source to this package (this source step is important, need do this first at any terminal).

For Carla has different version (not 0.9.13), you must change this in 01_RosBridge/src/carla_ros_bridge/src/carla_ros_bridge/CARLA_VERSION file. Then build again.

## Start:
1. Launch Carla server.

2. Make sure you source to ros package at step 2 in all Ros Terminal.

3. Ros Terminal 1 (Ros Bridge):
    
        roslaunch carla_ros_bridge carla_ros_bridge.launch

4. Ros Terminal 2 (Client):
    
        python /03_Client/main.py
    
5. Ros Terminal 3 (Dev code):
   
        python /04_Template/main.py

## Code API:

You can get template in /04_Template

## Link support debug:

    https://drive.google.com/drive/folders/1jWq_q5UNM6qG1bJA6EwZWt8-pFcCHXVC
