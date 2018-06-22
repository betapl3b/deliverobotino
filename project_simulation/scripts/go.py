#!/usr/bin/python
import rospy
from geometry_msgs.msg import PoseStamped
def goHome():
    global targetPose
    targetPose.pose.orientation.w = 0
    targetPose.pose.orientation.z = 1
    targetPose.pose.position.z = 0
    targetPose.pose.position.x = 4
    targetPose.pose.position.y = 5
    targetPose.header.frame_id = 'world'
    #
    # if int(targetMarker) == 1:
    #     targetPose.pose.position.x = 2.34
    #     targetPose.pose.position.y = -9
    # elif int(targetMarker) == 2:
    #     targetPose.pose.position.x = 6
    #     targetPose.pose.position.y = 9.5
    # elif int(targetMarker) == 3:
    #     targetPose.pose.position.x = 9
    #     targetPose.pose.position.y = 8
    # elif int(targetMarker) == 4:
    #     targetPose.pose.position.x = 6
    #     targetPose.pose.position.y = 0.84
    # else:
    #     targetPose = PoseStamped()
    #     targetPose.pose.orientation.w = 1
    coords.publish(targetPose)

def deliverobotino():
    goNext = 0
    while goNext == 0:
        global targetMarker
        targetMarker = int(raw_input('Who needs my help now? (1-4)\n'))
        targetPose.pose.orientation.w = 0.5
        targetPose.pose.orientation.z = 0.5
        targetPose.pose.position.x = 1.66
        targetPose.pose.position.z = -1
        targetPose.pose.position.y = -0.86
        if int(targetMarker) == 1:
            targetPose.header.frame_id = 'ar_marker_1'
            goNext+=1
        elif int(targetMarker) == 2:
            targetPose.header.frame_id = 'ar_marker_2'
            targetPose.pose.position.x = -1
            targetPose.pose.position.z = -1
            goNext += 1
        elif int(targetMarker) == 3:
            targetPose.header.frame_id = 'ar_marker_4'
            targetPose.pose.position.x = -1
            targetPose.pose.position.z = -1
            goNext += 1
        elif int(targetMarker) == 4:
            targetPose.header.frame_id = 'ar_marker_0'
            goNext += 1
        else:
            print('Wrong number')
    coords.publish(targetPose)
    print('Clap when I can go. \n')
    clapTest = raw_input('Press any key to continue... \n')
    goHome()


rospy.init_node('controller_node')
coords = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
oneMore='test'
while not oneMore == 'quit':
    targetPose = PoseStamped()
    deliverobotino()
    print('Type anything if u need my help and "quit" if u do not \n')
    oneMore = raw_input('...')
