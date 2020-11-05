import cv2
from easytello import tello
#
# set drone image parameters
width = 320  # width of the drone image
height = 240  # height of the drone image
startCounter = 0  # set to 0 if you want flight, 1 if you want the drone not to fly

drone = tello.Tello()
# Turning on stream
drone.streamon()
# Turning off stream
drone.streamoff()

drone.video_thread()

drone.get_battery()

drone.takeoff()

for i in range(4):

    drone.forward(20)
    drone.cw(90)

drone.land()
