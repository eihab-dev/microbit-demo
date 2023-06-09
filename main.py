
# Imports go at the top
from microbit import *
import power
import random
import music

# Code in a 'while True:' loop repeats forever
name="name"
grade=90

def ideal():
   grid = [Image().invert()*(i/9) for i in range(9, -1, -1)]
   sleep(random.randint(100, 350))
   display.show(grid, delay=100, wait=False)

while True:
   ideal()
   
   if button_a.is_pressed():
       display.scroll(name,delay=100,wait=True,loop=False,monospace=True)
   
   if button_b.is_pressed():
       
       if grade >= 90:
           display.show(Image.HAPPY)
           sleep(599)
           display.scroll("Excellent",monospace=True)
      
       else:
           display.show(Image.SAD)
           sleep(599)
           display.scroll("try harder",monospace=True ) 
          
   if temperature() <= 30:
       power.off()


   
