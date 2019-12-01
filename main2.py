import cv2
import numpy as np 
from picamera.array import PiRGBArray
from picamera import PiCamera
import serial

#Opening the serial port for serial communication. Fill the com port for the Arduino in ' '
ser1 = serial.Serial(' ', 9600)             #Servo arduino
ser2 = serial.Serial(' ', 9600)             #DC motors arduino

#Initializing the PiCamera and extracting a reference from its raw video stream
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

#Extracting frames from the camera and processing them
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image = frame.array
    #Converting from BGR to HSV
    hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   
    # Red mask
    low_red = np.array([161, 155, 50])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(image, image, mask=red_mask)

    # Blue mask
    low_blue = np.array([100 , 150, 0])
    high_blue = np.array([140 , 255 , 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(image, image, mask=blue_mask)

    # Yellow mask
    low_yellow = np.array([20, 100, 100])
    high_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(image, image, mask= yellow_mask)

    #Displaying various video streams
    cv2.imshow("Frame", image)
    cv2.imshow("Red", red)
    cv2.imshow("Yellow", yellow)
    cv2.imshow("Blue" , blue)

    #Converting from HSV to Grayscale
    gray_red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)
    gray_red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
    gray_yellow = cv2.cvtColor(yellow, cv2.COLOR_HSV2BGR)
    gray_yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2GRAY)
    gray_blue = cv2.cvtColor(blue, cv2.COLOR_HSV2BGR)
    gray_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    
    #Counting number of pixels of a particular colour
    Red_ct = cv2.countNonZero(gray_red) 
    Yellow_ct = cv2.countNonZeroa(gray_yellow) 
    Blue_ct = cv2.countNonZero(gray_blue) 
    
    #Setting threshold values
    Red_thr = 2500
    Yellow_thr = 7000
    Blue_thr = 6000

    while Red_ct >= Red_thr and Yellow_ct >= Yellow_thr and Blue_ct >= Blue_thr:
        s1 = "OPEN!"
        s1_enc = s1.encode()
        s2 = "OBJECT DETECTED!"
        s2_enc = s2.encode()
        ser1.write(s1_enc)
        ser2.write(s2_enc)


    key = cv2.waitKey(1)
    if key == 27:
        break