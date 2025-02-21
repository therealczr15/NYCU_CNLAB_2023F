# import package
import socket
import RPi.GPIO as GPIO
import time
import sys, select

# do not display warning messages
GPIO.setwarnings(False)
# set v = 343m/s
v = 343
# set pin
TRIG = 16
E = 18
LED_PIN = 12

HOST = "172.20.10.2"
PORT = 5050
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

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
  return d

while(1):
  d = measure()
  # output distance(cm)
  print d
  i, o, e = select.select([sys.stdin], [], [], 3)
  
  # if get message
  if(i):
    # read command
    key = sys.stdin.readline().strip()
    print(key, type(key))
    # if distance < 10cm
    if(d < 10):
      # send s, which means stop
      client.sendall('s')
    else:
      # else send command
      client.sendall(key)
  else:
    key = ''
    print("Nothing")
    
  # LED exhibits different reactions based on varying distances
  if(d < 10):
    print ("on")
    client.sendall('s')
    GPIO.output(LED_PIN, GPIO.HIGH)
  elif(d < 20):
    print("shine")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
  else:
    print("off")
    GPIO.output(LED_PIN, GPIO.LOW)
  time.sleep(1)
  
GPIO.cleanup()    