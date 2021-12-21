import adafruit_pca9685
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
kit.servo[1].angle = 180
# time.sleep(1)
# kit.servo[1].angle = 100