import os,sys
sys.path.append('~GrovePi/Software/Python')
sys.path.append('~GrovePi/Software/Python/grove_rgb_lcd')
import time
import grovepi
import grove_rgb_lcd as lcd

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0

grovepi.pinMode(potentiometer,"INPUT") #configure grovepi


# clear lcd screen  before starting main loop
lcd.setText("")
lcd.setRGB(0,0,0) #set to white

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
      lcd.setRGB(255,0,0) #set screen to red
      lcd.setText_norefresh(str(thresh_cm) + " OBJ PRES" + "\n" + str(range)) #print thresh value with object present tag
    else:
      lcd.setRGB(0,255,0) #set screen to green
      lcd.setText_norefresh(str(thresh_cm)+ " " + "\n" + str(range)) #print thresh value and range
    
    time.sleep(1) #add delay to see values on lcd clearly
  except IOError:
    print("Error")
