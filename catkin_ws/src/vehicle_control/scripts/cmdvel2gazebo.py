#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import math, sys, getopt

class cmdvel2gazebo:
    def __init__(self, ns):
        rospy.init_node('cmdvel2gazebo', anonymous=True)

        rospy.Subscriber('/catvehicle/cmd_vel_safe', Twist, self.callback)
        self.pub_steerL = rospy.Publisher('/catvehicle/front_left_steering_position_controller/command', Float64, queue_size=1)
        self.pub_steerR = rospy.Publisher('/catvehicle/front_right_steering_position_controller/command', Float64, queue_size=1)
        self.pub_rearL = rospy.Publisher('/catvehicle/joint1_velocity_controller/command', Float64, queue_size=1)
        self.pub_rearR = rospy.Publisher('/catvehicle/joint2_velocity_controller/command', Float64, queue_size=1)

        self.x = 0
        self.z = 0

        self.L = 2.62
        self.T = 1.301

        self.timeout = rospy.Duration.from_sec(0.2)
        self.lastMsg = rospy.Time.now()

        self.maxsteerInside = 0.6
        rMax = self.L / math.tan(self.maxsteerInside)
        rIdeal = rMax + (self.T / 2.0)
        self.maxsteer = math.atan2(self.L, rIdeal)
        rospy.logwarn("######### MAXIMUM ideal steering angle set to ==" + str(self.maxsteer))

    def callback(self, data):
        self.x = 2.8101 * data.linear.x
        self.z = max(-self.maxsteer, min(self.maxsteer, data.angular.z))
        self.lastMsg = rospy.Time.now()

    def publish(self):
        delta_last_msg_time = rospy.Time.now() - self.lastMsg
        msgs_too_old = delta_last_msg_time > self.timeout
        if msgs_too_old:
            self.x = 0
            msgRear = Float64()
            msgRear.data = self.x
            self.pub_rearL.publish(msgRear)
            self.pub_rearR.publish(msgRear)
            return

        if self.z != 0:
            r = self.L / math.fabs(math.tan(self.z))
            rL = r - (math.copysign(1, self.z) * (self.T / 2.0))
            rR = r + (math.copysign(1, self.z) * (self.T / 2.0))

            msgRearR = Float64()
            msgRearR.data = self.x * rR / r
            self.pub_rearR.publish(msgRearR)

            msgRearL = Float64()
            msgRearL.data = self.x * rL / r
            self.pub_rearL.publish(msgRearL)

            msgSteerL = Float64()
            msgSteerL.data = math.atan2(self.L, rL) * math.copysign(1, self.z)
            self.pub_steerL.publish(msgSteerL)

            msgSteerR = Float64()
            msgSteerR.data = math.atan2(self.L, rR) * math.copysign(1, self.z)
            self.pub_steerR.publish(msgSteerR)
        else:
            msgRear = Float64()
            msgRear.data = self.x
            self.pub_rearL.publish(msgRear)
            self.pub_rearR.publish(msgRear)

            msgSteer = Float64()
            msgSteer.data = self.z
            self.pub_steerL.publish(msgSteer)
            self.pub_steerR.publish(msgSteer)

def main(argv):
    ns = ''
    node = cmdvel2gazebo(ns)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        node.publish()
        rate.sleep()

if __name__ == '__main__':
    main(sys.argv[1:])
