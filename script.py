import RPi.GPIO as GPIO

import lcddriver

import time

import os

 

# Use the Broadcom SOC Pin numbers
GPIO.setmode(GPIO.BCM)

# Import LCD driver (lcddriver.py file)
lcd = lcddriver.lcd()

# Setup the pins with internal pullups enabled and pin in reading mode.

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Shutdown button GPIO 21
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Reboot button   GPIO 18 
 

# Our functions on what to do when the button is pressed
def Shutdown(channel):                              

    print("Shutting Down")                         #Show text in terminal 

    lcd.lcd_display_string("Shutting Down",1)      #Display text in LCD 

    time.sleep(3)                                  #Sleep 3 seconds

    os.system("sudo shutdown now")                 #Write command

 
def Reboot(channel):

    print("Rebooting")

    lcd.lcd_display_string("Rebooting",1)

    time.sleep(3)

    os.system("sudo reboot")


# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(21, GPIO.FALLING, callback=Shutdown, bouncetime=2000)
GPIO.add_event_detect(18, GPIO.FALLING, callback=Reboot,   bouncetime=2000)

 
#Wait!

while 1:

   time.sleep(1)
