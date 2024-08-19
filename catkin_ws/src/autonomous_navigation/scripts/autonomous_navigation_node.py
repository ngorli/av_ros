#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import LaserScan, Image
from dbw_mkz_msgs.msg import BrakeCmd, ThrottleCmd, SteeringCmd, GearCmd
from std_msgs.msg import Empty

class AutonomousNavigation:
    def __init__(self):
        self.pub_brake = rospy.Publisher('/vehicle/brake_cmd', BrakeCmd, queue_size=1)
        self.pub_throttle = rospy.Publisher('/vehicle/throttle_cmd', ThrottleCmd, queue_size=1)
        self.pub_steering = rospy.Publisher('/vehicle/steering_cmd', SteeringCmd, queue_size=1)
        self.pub_gear = rospy.Publisher('/vehicle/gear_cmd', GearCmd, queue_size=1)
        self.pub_enable = rospy.Publisher('/vehicle/enable', Empty, queue_size=1)

        rospy.Subscriber('/catvehicle/front_laser_points', LaserScan, self.lidar_callback)
        rospy.Subscriber('/catvehicle/camera_front/image_raw_front', Image, self.camera_callback)

        self.enable_dbw()

        self.obstacle_detected = False
        self.swerve_in_progress = False
        self.swerve_direction = 0.0
        self.swerve_duration = 0
        self.initial_steering = 0.0  

        self.control_loop()

    def enable_dbw(self):
        empty_msg = Empty()
        self.pub_enable.publish(empty_msg)
        rospy.loginfo("DBW system enabled")

    def lidar_callback(self, msg):
        front_min = min(msg.ranges[:len(msg.ranges)//3]) 
        left_min = min(msg.ranges[len(msg.ranges)//3:2*len(msg.ranges)//3])  
        right_min = min(msg.ranges[2*len(msg.ranges)//3:]) 

        detection_distance = 2.0

        if front_min < detection_distance:
            if not self.swerve_in_progress:
                self.obstacle_detected = True
                self.swerve_in_progress = True
                self.swerve_duration = 12  # Number of control loop iterations to swerve

                self.initial_steering = 0.0

                if left_min > right_min:
                    self.swerve_direction = -0.5  
                    rospy.loginfo("Swerving right")
                else:
                    self.swerve_direction = 0.5  
                    rospy.loginfo("Swerving left")

    def camera_callback(self, msg):
        pass

    def brake_cmd_publisher(self, brake_value=0.0):
        brake_cmd = BrakeCmd()
        brake_cmd.pedal_cmd = brake_value
        brake_cmd.pedal_cmd_type = 1
        brake_cmd.enable = True
        self.pub_brake.publish(brake_cmd)
    
    def throttle_cmd_publisher(self, throttle_value=0.5):
        throttle_cmd = ThrottleCmd()
        throttle_cmd.pedal_cmd = throttle_value
        throttle_cmd.pedal_cmd_type = 1
        throttle_cmd.enable = True
        self.pub_throttle.publish(throttle_cmd)

    def steering_cmd_publisher(self, angle_rad=0.0):
        steering_cmd = SteeringCmd()
        steering_cmd.steering_wheel_angle_cmd = angle_rad
        steering_cmd.enable = True
        self.pub_steering.publish(steering_cmd)

    def gear_cmd_publisher(self, gear_value=4):
        gear_cmd = GearCmd()
        gear_cmd.cmd.gear = gear_value
        self.pub_gear.publish(gear_cmd)

    def control_loop(self):
        rate = rospy.Rate(5) 
        while not rospy.is_shutdown():
            if self.swerve_in_progress:
                self.swerve_duration -= 1
                if self.swerve_duration > 0:
                    self.steering_cmd_publisher(self.swerve_direction)
                elif self.swerve_duration <= 0 and self.swerve_duration > -12:
                    self.steering_cmd_publisher(self.swerve_direction * -1)
                else:
                    self.swerve_in_progress = False
                    self.obstacle_detected = False
                    self.steering_cmd_publisher(self.initial_steering)  
                    rospy.loginfo("Straightening up and resuming original trajectory")
            else:
                self.throttle_cmd_publisher(500)  
                self.steering_cmd_publisher(0.0)  
                rospy.loginfo("Moving forward")

            self.gear_cmd_publisher(4)  
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('autonomous_navigation_node', anonymous=True)
    try:
        AutonomousNavigation()
    except rospy.ROSInterruptException:
        pass
