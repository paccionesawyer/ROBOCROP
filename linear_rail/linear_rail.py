import RPi.GPIO as GPIO
import time

class LinearRail:
    def __init__(self, direction_pin, step_pin, freq=50):
        
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        
        # using pin numbers (BOARD) rather than GPIO numbers (BCM) for pin naming
        GPIO.setmode(GPIO.BCM)
        
        # initializing pins as outputs
        GPIO.setup(direction_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        
        self.last_signal = False

    # set speed of motor
    def move(self, num_steps, delay):
        
        if (num_steps > 0):
            GPIO.output(self.direction_pin, GPIO.HIGH)
            for i in range(num_steps):
                cur_signal = not self.last_signal
                GPIO.output(self.step_pin, cur_signal)
                self.last_signal = cur_signal
                time.sleep(delay)
        elif (num_steps < 0):
            GPIO.output(self.direction_pin, GPIO.LOW)
            for i in range(-num_steps):
                cur_signal = not self.last_signal
                GPIO.output(self.step_pin, cur_signal)
                self.last_signal = cur_signal
                time.sleep(delay)
