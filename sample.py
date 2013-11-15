import xbox
import time

# Setup joystick
joy = xbox.Joystick()

try:
    #Valid connect may require joystick input to occur
    print "Waiting for Joystick to connect"
    while not joy.connected():
        time.sleep(0.10)

    #Show misc inputs until Back button is pressed    
    while not joy.Back() and joy.connected():
        print joy.connected(),"ABXY",joy.A(),joy.B(),joy.X(),joy.Y(), \
              "DPAD",joy.dpadLeft(), joy.dpadRight(), joy.dpadUp(), joy.dpadDown(), \
              "START",joy.Start(),"LEFT THUMBSTICK", joy.leftThumbstick(), \
              "LEFT X/Y",joy.leftX(),joy.leftY(),"RIGHT TRIGGER",joy.rightTrigger()
        time.sleep(0.10)

finally:
    #Always close out so that xboxdrv subprocess ends
    joy.close()
    print "Done."
