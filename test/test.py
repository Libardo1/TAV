import RPi.GPIO as GPIO
import time 

motor0 = 27
motor1 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor0, GPIO.OUT)
GPIO.setup(motor1, GPIO.OUT)

# Test motors
GPIO.output(motor0, GPIO.HIGH)
GPIO.output(motor1, GPIO.HIGH)
print('Motors on!')

time.sleep(5)

GPIO.output(motor0, GPIO.LOW)
GPIO.output(motor1, GPIO.LOW)
print('Motors off!')

time.sleep(5)

# Test motors again
GPIO.output(motor0, GPIO.HIGH)
GPIO.output(motor1, GPIO.HIGH)
print('Motors on again!')

time.sleep(5)

GPIO.output(motor0, GPIO.LOW)
GPIO.output(motor1, GPIO.LOW)
print('Motors off again!')

time.sleep(5)


GPIO.cleanup()