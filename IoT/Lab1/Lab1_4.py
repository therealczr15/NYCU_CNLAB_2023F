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

while True:
  # get humidity and temperature
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  # set v = 331 + 0.6 * temperature
  v = 331 + 0.6 * temperature
  # set pin
  TRIG = 16
  E = 18
  LED_PIN = 12

  print('1')
  
  # numbered in order according to GPIO pin
  GPIO.setmode(GPIO.BOARD)
  # set TRIG to GPIO.OUT
  GPIO.setup(TRIG, GPIO.OUT)
  # set E to GPIO.IN
  GPIO.setup(E, GPIO.IN)
  # set TRIG to a low logic level
  GPIO.setup(TRIG, GPIO.LOW)
  # set LED_PIN to GPIO.OUT
  GPIO.setup(LED_PIN, GPIO.OUT)

  def measure():
    # trigger a low logic level
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(E) == GPIO.LOW:
      # start time
      pulse_start = time.time()
    while GPIO.input(E) == GPIO.HIGH:
      # time received from the echo
      pulse_end = time.time()
    # duration from emission to receiving the echo
    t = pulse_end - pulse_start
    # distance = time * velocity
    d = t * v
    # one-way distance
    d = d / 2
    # m to cm
    d = d * 100
    
    # LED exhibits different reactions based on varying distances
    if(d < 10):
      GPIO.output(LED_PIN, GPIO.HIGH)
    elif(d < 20):
      GPIO.output(LED_PIN, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(LED_PIN, GPIO.LOW)
      time.sleep(0.1)
    else:
      GPIO.output(LED_PIN, GPIO.LOW)
      
    return d

  while(1):
    print('============================')
    # output temperature
    print('Temp:{0:0.1f}*C'.format(temperature))
    # output velocity
    print('V=331+0.6*{0:0.1f}'.format(temperature))
    print(' =' + str(v))
    # output distance(cm)
    print('Distance:' + str(measure()) + 'cm')
    
    time.sleep(1)
    
  GPIO.cleanup()    