# import RPi.GPIO as GPIO
# import time
# 
# direction_pin = 31
# step_pin = 33
# 
# freq = 60
# 
# # using pin numbers (BOARD) rather than GPIO numbers (BCM) for pin naming
# GPIO.setmode(GPIO.BOARD)
# 
# # initializing pins as outputs
# GPIO.setup(direction_pin, GPIO.OUT)
# GPIO.setup(step_pin, GPIO.OUT)
# 
# # setting up PWM channels on pins at specified frequency
# pwm1 = GPIO.PWM(step_pin, freq) # for controlling step frequency
# 
# GPIO.output(direction_pin, GPIO.LOW)
# pwm1.start(80)
# time.sleep(4)
# pwm1.ChangeDutyCycle(0)
# 
# time.sleep(2)
# 
# GPIO.output(direction_pin, GPIO.HIGH)
# pwm1.start(80)
# time.sleep(2)
# pwm1.stop()

# GPIO.cleanup()

import time
from linear_rail import LinearRail

direction_pin = 11
step_pin = 13

rail = LinearRail(direction_pin, step_pin)

print("Forwards 40 ticks")
rail.move(6000, 0.001)

time.sleep(2)

print("Backwards 40 ticks")
rail.move(-6000, 0.001)