# This is a sample code for implementation of an NFC Gripper.
# The demo consists of the robot picking up 3 boxes and checking if any of them are "Gelocatil"
# The NFC Gripper publishes the name of the boxes by serial communication
# When the box is found, the robot puts it in a basket
# The poses of the boxes are harcoded 

from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import serial
import time

#Initialize the serial port and wait to be connected
SerialObj = serial.Serial('/dev/ttyUSB0')
time.sleep(0.1)

def main():
    bot = InterbotixManipulatorXS(
        robot_model='wx250',
        group_name='arm',
        gripper_name='gripper'
    )

    #Function to check with the NFC sensor if the box is "Gelocatil"
    def check_medicine():
        SerialObj.timeout = 1  # Set a 5-second timeout 
        ReceivedString = SerialObj.readline().decode('ascii')
        if ReceivedString == "Gelocatil\r\n":
            print("Medicine found!!")
            bot.arm.set_ee_pose_components(**basket_transition)
            bot.arm.set_ee_pose_components(**basket_approach)
            bot.arm.set_ee_pose_components(**basket_centroid)
            bot.gripper.release()
            bot.arm.set_ee_pose_components(**basket_approach)
            SerialObj.reset_input_buffer()
        else:
         bot.gripper.release()

    #Initial state
    bot.arm.go_to_sleep_pose()
    bot.gripper.release()
    bot.arm.go_to_home_pose()
    
    # Harcoded parameters for the poses of the 3 boxes and the basket
    box1_approach = {'x': 0.1, 'y': 0.3, 'z': 0.2, 'roll': 1.0, 'pitch': 1.5}
    box1_centroid = {'x': 0.1, 'y': 0.3, 'z': 0.05, 'roll': 1.0, 'pitch': 1.5}
    box2_approach = {'x': 0.1, 'y': 0.2, 'z': 0.2, 'roll': 1.0, 'pitch': 1.5}
    box2_centroid = {'x': 0.1, 'y': 0.2, 'z': 0.05, 'roll': 1.0, 'pitch': 1.5}
    box3_approach = {'x': 0.1, 'y': 0.1, 'z': 0.2, 'roll': 1.0, 'pitch': 1.5}
    box3_centroid = {'x': 0.1, 'y': 0.1, 'z': 0.05, 'roll': 1.0, 'pitch': 1.5}
    basket_approach = {'x': -0.3, 'y': 0.2, 'z': 0.2, 'roll': 1.0, 'pitch': 1.5}
    basket_centroid = {'x': -0.3, 'y': 0.2, 'z': 0.05, 'roll': 1.0, 'pitch': 1.5}
    basket_transition = {'x': 0.1, 'y': 0.2, 'z': 0.3, 'roll': 1.0, 'pitch': 1.5}

    #Function to pick up the box with 2 waypoints: the approach and the centroid pose
    def pick_box(approach_pose, centroid_pose):
        bot.arm.set_ee_pose_components(**approach_pose)
        bot.arm.set_ee_pose_components(**centroid_pose)
        bot.gripper.grasp()
        check_medicine()
        bot.arm.set_ee_pose_components(**approach_pose)

    boxes = [(box1_approach, box1_centroid), (box2_approach, box2_centroid), (box3_approach, box3_centroid)]

    for approach_pose, centroid_pose in boxes:
        pick_box(approach_pose, centroid_pose)

    # Return home 
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()
    bot.shutdown()

if __name__ == '__main__':
    main()

