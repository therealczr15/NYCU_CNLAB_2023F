# import package
import RPi.GPIO as GPIO
import time

# do not display warning messages
GPIO.setwarnings(False)
# set v = 343m/s
v = 343
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
  # output distance(cm)
  print(measure())
  time.sleep(1)
  
GPIO.cleanup()    