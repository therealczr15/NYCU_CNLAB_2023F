# import package
import RPi.GPIO as GPIO
import time

# do not display warning messages
GPIO.setwarnings(False)
# numbered in order according to GPIO pin
GPIO.setmode(GPIO.BOARD)
# LED pin is 12 (GPIO18)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
  # s
  for i in range(3) :
    # set the LED_PIN to a high logic level (turn on the light)
    GPIO.output(LED_PIN, GPIO.HIGH)
    # lasting 0.1 seconds
    time.sleep(0.1)
    # set the LED_PIN to a low logic level (turn off the light)
    GPIO.output(LED_PIN, GPIO.LOW)
    # lasting 0.1 seconds
    time.sleep(0.1)  
  time.sleep(0.3)
  
  # o
  for i in range(3) :
    # set the LED_PIN to a high logic level (turn on the light)
    GPIO.output(LED_PIN, GPIO.HIGH)
    # lasting 0.3 seconds
    time.sleep(0.3)
    # set the LED_PIN to a low logic level (turn off the light)
    GPIO.output(LED_PIN, GPIO.LOW)
    # lasting 0.1 seconds
    time.sleep(0.1)
  time.sleep(0.3)
  
  # s
  for i in range(3) :
    # set the LED_PIN to a high logic level (turn on the light)
    GPIO.output(LED_PIN, GPIO.HIGH)
    # lasting 0.1 seconds
    time.sleep(0.1)
    # set the LED_PIN to a low logic level (turn off the light)
    GPIO.output(LED_PIN, GPIO.LOW)
    # lasting 0.1 seconds
    time.sleep(0.1)
  time.sleep(0.7)