import os,sys
sys.path.append('~GrovePi/Software/Python')
sys.path.append('~GrovePi/Software/Python/grove_rgb_lcd')


import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0

grovepi.pinMode(potentiometer,"INPUT")


# clear lcd screen  before starting main loop
setText_norefresh("")
adc_ref = 5
grove_vcc= 5
full_angle= 300

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on$
    range = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    sensor_value = grovepi.analogRead(potentiometer)
    thresh_cm = int((sensor_value/1023.0)*200)

    # TODO: format LCD text according to threshhold
    if(range <= thresh_cm):
      setText_norefresh((str)(thresh_cm) + " OBJ PRES")
    else:
      setText_norefresh((str)(thresh_cm)+ " ")
    
    setText_norefresh("\n" + (str)(range))
    
  except IOError:
    print("Error")