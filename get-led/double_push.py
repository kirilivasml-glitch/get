import time
import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

    




GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
up = 9
down = 10
num = 0

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

GPIO.setup([up,down], GPIO.IN)




sleep_time = 0.2

while True:
    if GPIO.input(up) and GPIO.input(down):
       n=255
       print(num, dec2bin(num))
       time.sleep(sleep_time)

    elif GPIO.input(up):
        if num<255:
          num+=1
          print(num, dec2bin(num))
          time.sleep(sleep_time)
        else:
          num =0
          print(num, dec2bin(num))
          time.sleep(sleep_time)
    elif GPIO.input(down):
        if num>0:
          num-=1
          print(num, dec2bin(num))
          time.sleep(sleep_time)
        else:
          num = 0
          print(num, dec2bin(num))
          time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))
        