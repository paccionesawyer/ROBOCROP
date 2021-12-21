from linear_rail.linear_rail import LinearRail
from motor.DCMotor import Motor 
import time
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO

class seedlingPlanter():
    def __init__(self):
        self.direction_pin = 17# 11 Board
        self.step_pin = 27# 13 Board
        self.linearRail = LinearRail(self.direction_pin, self.step_pin)
        self.suctionMotor = Motor(23, 24) # 16, 18 Board
        self.pumpMotor = Motor(25,8) # 22, 24
        GPIO.setmode(GPIO.BCM)
        self.kit = ServoKit(channels=16)

        self.tipServo = self.kit.servo[1]
        self.elbowServo = self.kit.servo[2]
        self.shoulderServo = self.kit.servo[3]

        self.tipCurr = 180 # Set these to default
        self.elbowCurr = 90 
        self.shoulderCurr = 90

        self.abovePots = [180, 0, 150]
        self.insertNeedle = [180, 20, 120]

        self.sampleSize = 10

        self.resetArm()

    def resetArm(self):
        # arm straight out 
        self.moveQuick(self.abovePots)
        self.tipCurr = self.abovePots[0]
        self.elbowCurr = self.abovePots[1]
        self.shoulderCurr = self.abovePots[2]

    def moveLeft(self):
        self.linearRail.move(10000, 0.001)

    def moveRight(self):
        self.linearRail.move(-10000, 0.001)

    def moveQuick(self, posArray):
        self.tipServo.angle = posArray[0]
        self.elbowServo.angle = posArray[1]
        self.shoulderServo.angle = posArray[2]

    def moveSlow(self, posArray):

        tipDiff = posArray[0] - self.tipCurr 
        elbowDiff = posArray[1] - self.elbowCurr
        shoulderDiff = posArray[2] - self.shoulderCurr

        print("tipDiff:", tipDiff)
        print("elbowDiff:", elbowDiff)
        print("shoulderDiff:", shoulderDiff)

        tipStep = tipDiff // self.sampleSize
        elbowStep = elbowDiff // self.sampleSize
        shoulderStep = shoulderDiff // self.sampleSize

        print("tipStep:", tipStep)
        print("elbowStep:", elbowStep)
        print("shoulderStep:", shoulderStep)

        for i in range(self.sampleSize - 2):
            self.tipCurr += tipStep
            self.elbowCurr += elbowStep
            self.shoulderCurr += shoulderStep

            print(self.tipCurr)
            print(self.elbowCurr)
            print(self.shoulderCurr)

            self.tipServo.angle = self.tipCurr
            self.elbowServo.angle = self.elbowCurr
            self.shoulderServo.angle = self.shoulderCurr
            time.sleep(0.1)

        self.tipServo.angle = posArray[0]
        self.elbowServo.angle = posArray[1]
        self.shoulderServo.angle = posArray[2]

    def iNeedle(self):
        # self.moveQuick(self.insertNeedle)
        self.moveSlow(self.insertNeedle)
        
    def testLinearRail(self):
        print("Forwards 40 ticks")
        self.linearRail.move(6000, 0.001)

        time.sleep(2)

        print("Backwards 40 ticks")
        self.linearRail.move(-6000, 0.001)

    def testSuc(self):
        self.suctionMotor.set_speed(-100)
        time.sleep(5)
        self.suctionMotor.stop()

    def testPump(self):
        self.pumpMotor.set_speed(40)
        time.sleep(3)
        self.pumpMotor.stop()

    def testRailandSuc(self):
        self.suctionMotor.set_speed(-100)
        time.sleep(3)
        self.linearRail.move(6000, 0.001)
        self.suctionMotor.stop()

    def spinTip(self):
        self.smoothMove(180, self.tipServo, 70)



if __name__ == "__main__":
    jeff = seedlingPlanter()
    jeff.testPump()
    # jeff.spinTip()