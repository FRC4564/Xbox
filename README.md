xbox.py
=======

Python class to support reading xbox 360 wired and wireless controller input under Linux.  Makes it easy to get real-time input from controller buttons, analog sticks and triggers.  Built and tested on RaspberryPi running Raspbian.

Requires that xboxdrv be installed first:

    sudo apt-get install xboxdrv

To test the driver, issue the following command and see if the controller inputs are recognized

    sudo xboxdrv --detach-kernel-driver

See http://pingus.seul.org/~grumbel/xboxdrv/ for details on xboxdrv

Download the python module and sample code with the following:

    wget https://raw.githubusercontent.com/FRC4564/Xbox/master/xbox.py
    wget https://raw.githubusercontent.com/FRC4564/Xbox/master/sample.py

You can run the sample code to see how the Joystick class works.

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

Note:
Run your code with sudo privileges to allow xboxdrv the necessary control over USB devices.
If you want, you can provide your user account with the proper access, so you needn't use sudo.

First, add your user to the root group. Here's how to do this for the user ‘pi’

    sudo usermod -a -G root pi

Create a permissions file using the nano text editor.

    sudo nano /etc/udev/rules.d/55-permissions-uinput.rules

Enter the following rule and save your entry.

    KERNEL=="uinput", MODE="0660", GROUP="root"

Troubleshooting
---------------

I find that xboxdrv occasionally has trouble connecting to the controller.  You may see a USB device error or something similar.  Issuing the following command will detach and reconnect the controller.

    sudo xboxdrv --detach-kernel-driver
    
You should now be able to move the joysticks and press buttons to see the controller state display for all inputs.  Just press Ctrl-C to exit and then relaunch your python code that uses xbox.py.

If your wireless controller still won't connect, press the sync button on the controller and the receiver (both devices need to be powered).

Usage
-----

A good application for an XBox controller is for robot control.  Check out [Basic PiBot](https://github.com/FRC4564/BasicPiBot) for more details.
