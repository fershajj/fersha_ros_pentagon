#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.141592653589793
i = 0
        
def linear(): 
    rospy.init_node('pent', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    move = Twist()   
    global i
    
    move.linear.x = 1
    move.linear.y = 0
    move.linear.z = 0
    move.angular.x = 0
    move.angular.y = 0
    move.angular.z = 0
        
    while not rospy.is_shutdown():
        t1 = rospy.get_time()
        cur_distance = 0
        while(cur_distance < 1):
            pub.publish(move)
            t2=rospy.get_time()
            cur_distance= 1*(t2-t1)
        move.linear.x = 0
        while(i<5):
            angular()       
        
        
def angular(): 
    rospy.init_node('pent', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rotate = Twist() 
    global i 
    
    rotate.angular.x = 0
    rotate.angular.y = 0
    rotate.angular.z= 0.2
    rotate.linear.x = 0
    rotate.linear.y = 0
    rotate.linear.z = 0
    t3 = rospy.get_time()
    cur_angle = 0
    
    while(cur_angle < 72*2*PI/360):
        pub.publish(rotate)
        t4 = rospy.get_time()
        cur_angle = 0.2*(t4-t3)
    rotate.angular.z = 0
    while(i<5):
        i=i+1
        linear()
    rospy.spin()
        
   
            
if __name__ == '__main__':    
    angular()
    
