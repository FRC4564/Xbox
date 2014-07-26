xbox.py
=======

Python class to support reading xbox 360 wired and wireless controller input under Linux.  Makes it easy to get real-time input from controller buttons, analog sticks and triggers.  Built and tested on RaspberryPi running Raspbian.

Requires that xboxdrv be installed first:

    sudo apt-get install xboxdrv

To test the driver, issue the following command and see if the controller inputs are recognized

    sudo xboxdrv --detach-kernel-driver

See http://pingus.seul.org/~grumbel/xboxdrv/ for details on xboxdrv

Once the driver is installed, you can run the sample code to see how the Python classs module works.

    sudo python sample.py

Example class usage:

    import xbox
    joy = xbox.Joystick()         #Initialize joystick
    
    if joy.A():                   #Test state of the A button (1=pressed, 0=not pressed)
        print 'A button pressed'
    x_axis   = joy.leftX()        #X-axis of the left stick (values -1.0 to 1.0)
    (x,y)    = joy.leftStick()    #Returns tuple containing left X and Y axes (values -1.0 to 1.0)
    trigger  = joy.rightTrigger() #Right trigger position (values 0 to 1.0)
    
    joy.close()                   #Cleanup before exit

Note: Run with sudo privileges to allow xboxdrv necessary access to USB device
