# -*- coding: utf-8 -*-
import zmq
import random
import time

import Adafruit_DHT

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

context = zmq.Context()
socket = context.socket(zmq.PUB)

# IP 記得更改
socket.bind("tcp://192.168.0.167:5577")


while True:
    # 從溫濕度模組取的數值
    # 此處會用到的 function
    #    1.  Adafruit_DHT.read_retry(...., ....)

    ''' start of you code '''
    
    humidity, temp = Adafruit_DHT.read_retry(sensor, gpio)
    ''' end of you code '''

    socket.send("temp = %d" % (temp))
    time.sleep(0.5)

    socket.send("humidity = %d" % (humidity))
    time.sleep(0.5)
