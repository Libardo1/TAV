import xbox
import time
import RPi.GPIO as GPIO


r_led = 20
l_led = 24

l_motor = 27
r_motor = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(r_led, GPIO.OUT)
GPIO.setup(l_led, GPIO.OUT)
GPIO.setup(r_motor, GPIO.OUT)
GPIO.setup(l_motor, GPIO.OUT)

joy = xbox.Joystick()

print ("Xbox controller sample: Press Back button to exit")
# Loop until back button is pressed

while not joy.Back():
    # Show connection status
    if joy.connected():
        print ("Connected   ")
    else:
        print ("Disconnected")
    # Left and right analog stick
    print('Lx, Ly, Rx, Ry', joy.leftX(), joy.leftY(), joy.rightX(), joy.rightY())

    # Right Motor
    if joy.rightY() == 1.0:
        GPIO.output(r_motor, GPIO.HIGH)
    else:
        GPIO.output(r_motor, GPIO.LOW)
    # Left Motor
    if joy.leftY() == 1.0:
        GPIO.output(l_motor, GPIO.HIGH)
    else:
        GPIO.output(l_motor, GPIO.LOW)

    # Head lights
    if joy.rightTrigger() == 1.0:
        GPIO.output(r_led, GPIO.HIGH)
    else:
        GPIO.output(r_led, GPIO.LOW)

    if joy.leftTrigger() == 1.0:
        GPIO.output(l_led, GPIO.HIGH)
    else:
        GPIO.output(l_led, GPIO.LOW)
        
    # Move cursor back to start of line
    print (chr(13))

# Close out when done
GPIO.cleanup()
joy.close()
