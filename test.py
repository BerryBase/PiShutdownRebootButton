#https://www.blog.berrybase.de/

import sys
import os 
import lcddriver
from time import *

#Lcd Inisialization 
lcd = lcddriver.lcd()


#lcd.lcd_display_string("TEXT TO PRINT", LINE, COLUMN)

lcd.lcd_display_string("Blog",1)            #Display on , 1.line , 1.column
    
lcd.lcd_display_string("BerryBase",2)       #Display on , 2.line , 1.column

sleep(3)                                    #3 Seconds 

lcd.lcd_clear()                             #Clear Display 

sys.exit()                                  #Finish Program 
