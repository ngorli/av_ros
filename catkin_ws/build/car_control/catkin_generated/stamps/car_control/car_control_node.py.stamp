#!/usr/bin/env python
import rospy
from dbw_mkz_msgs.msg import BrakeCmd, ThrottleCmd, SteeringCmd, GearCmd, Gear
from std_msgs.msg import Empty

class CarControl(object):
    def __init__(self):
        # Initialize publishers
        self.pub_brake_cmd = rospy.Publisher('/vehicle/brake_cmd', BrakeCmd, queue_size=1)
        self.pub_throttle_cmd = rospy.Publisher('/vehicle/throttle_cmd', ThrottleCmd, queue_size=1)
        self.pub_steering_cmd = rospy.Publisher('/vehicle/steering_cmd', SteeringCmd, queue_size=1)
        self.pub_gear_cmd = rospy.Publisher('/vehicle/gear_cmd', GearCmd, queue_size=1)
        self.pub_enable = rospy.Publisher('/vehicle/enable', Empty, queue_size=1)

        # State to check if DBW is enabled
        self._enable_dbw = False
        rospy.Subscriber("/vehicle/enable", Empty, self.enable_callback)

        # Ensure Gazebo is ready before publishing commands
        rospy.wait_for_service('/gazebo/set_physics_properties')
        rospy.loginfo("Gazebo Ready...")

        # Enable DBW system
        self.enable_dbw_inputs_loop()

    def enable_callback(self, data):
        """
        Callback function to set DBW enable status.
        """
        self._enable_dbw = True
        rospy.loginfo("DBW system enabled callback received.")

    def enable_dbw_inputs_loop(self):
        """
        Continuously publish enable message until DBW system is enabled.
        """
        rate = rospy.Rate(6)  # 1 Hz
        while not rospy.is_shutdown() and not self._enable_dbw:
            rospy.loginfo("Trying to enable /vehicle/enable, STATUS = " + str(self._enable_dbw))
            self.enable_dbw_inputs()
            rate.sleep()
        rospy.loginfo("DBW inputs ENABLED...")

    def enable_dbw_inputs(self):
        """
        Publish enable message to allow DBW system to accept commands.
        """
        empty_message = Empty()
        rospy.loginfo("Publishing enable command to /vehicle/enable")
        self.pub_enable.publish(empty_message)

    def cmd_publisher(self):
        """
        Continuously publish commands for throttle, brake, steering, and gear.
        """
        rate = rospy.Rate(5)  # 5 Hz
        speed = 5.0
        while not rospy.is_shutdown():
            rospy.loginfo("Publishing control commands...")
            self.throttle_cmd_publisher(throttle_value=speed)
            self.brake_cmd_publisher(brake_value=0.0)
            self.steering_cmd_publisher(angle_rad=0.0)
            self.gear_cmd_publisher(gear_value=4)
            rate.sleep()

    def throttle_cmd_publisher(self, throttle_value=0.0):
        """
        Publish throttle command.
        """
        throttle_cmd = ThrottleCmd()
        throttle_cmd.pedal_cmd = throttle_value
        throttle_cmd.pedal_cmd_type = 1  # Type 1 is typically a standard type
        throttle_cmd.enable = True
        rospy.loginfo("Throttle command published: " + str(throttle_cmd.pedal_cmd))
        self.pub_throttle_cmd.publish(throttle_cmd)

    def brake_cmd_publisher(self, brake_value=0.0):
        """
        Publish brake command.
        """
        brake_cmd = BrakeCmd()
        brake_cmd.pedal_cmd = brake_value
        brake_cmd.pedal_cmd_type = 1  # Type 1 is typically a standard type
        brake_cmd.enable = True
        rospy.loginfo("Brake command published: " + str(brake_cmd.pedal_cmd))
        self.pub_brake_cmd.publish(brake_cmd)

    def steering_cmd_publisher(self, angle_rad=0.0):
        """
        Publish steering command.
        """
        steering_cmd = SteeringCmd()
        steering_cmd.steering_wheel_angle_cmd = angle_rad
        steering_cmd.enable = True
        rospy.loginfo("Steering command published: " + str(steering_cmd.steering_wheel_angle_cmd))
        self.pub_steering_cmd.publish(steering_cmd)

    def gear_cmd_publisher(self, gear_value=0):
        """
        Publish gear command.
        """
        gear_cmd = GearCmd()
        gear_cmd.cmd.gear = gear_value
        rospy.loginfo("Gear command published: " + str(gear_cmd.cmd.gear))
        self.pub_gear_cmd.publish(gear_cmd)

if __name__ == '__main__':
    rospy.init_node('car_control_node', anonymous=True)
    car_control = CarControl()
    try:
        car_control.cmd_publisher()
    except rospy.ROSInterruptException:
        rospy.loginfo("Car control node interrupted.")
