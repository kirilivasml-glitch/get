import time
import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def turn_the_on(leds, num_2):
        for i in range(8):
        GPIO.output(leds[i], num_2[i])




GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
up = 10
down = 9

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

GPIO.setup([up,down] , GPIO.IN)

num = 0

sleep_time = 0.2

if GPIO.input(up):
   if num<255:
    num+=1
    print(num, dec2bin(num))

    turn_the_on(leds, dec2bin(num) )
    time.sleep(sleep_time)
   else:
       num = 0
       print(num, dec2bin(num))
       turn_the_on(leds, dec2bin(num))
       time.sleep(sleep_time)

if GPIO.input(down):
      if num>0:
          num-=1
          print(num, dec2bin(num))
          turn_the_on(leds, dec2bin(num))
          time.sleep(sleep_time)
      else:
          num = 0
          print(num, dec2bin(num))
          turn_the_on(leds, dec2bin(num))
          time.sleep(sleep_time)

if GPIO.input(down) and GPIO.input(up):
    num = 255
    print(num, dec2bin(num))
    turn_the_on(leds, dec2bin(num))
    time.sleep(sleep_time)
