#!/usr/bin/python

# import package
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# do not display warning messages
GPIO.setwarnings(False)
# numbered in order according to GPIO pin
GPIO.setmode(GPIO.BOARD)
# LED pin is 12 (GPIO18)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

# the sensor is the second parameter with a value of 11
# the pin is the third parameter with a value of 4
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

# enter a temperature threshold value
threshold = input()

while True:
  # get humidity and temperature
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  if humidity is not None and temperature is not None:
      # output temperature and humidity values
      print('Temp={0:0.3f}*  Humidity={1:0.3f}%'.format(temperature, humidity))
      # temperature is above the threshold
      if temperature >= threshold:
        # set the LED_PIN to a high logic level (turn on the light)
        GPIO.output(LED_PIN, GPIO.HIGH)  
      # temperature is below the threshold 
      else:
        # set the LED_PIN to a low logic level (turn off the light)
        GPIO.output(LED_PIN, GPIO.LOW)   
  else:
      print('Failed to get reading. Try again!')
      sys.exit(1)
  time.sleep(1)
  
