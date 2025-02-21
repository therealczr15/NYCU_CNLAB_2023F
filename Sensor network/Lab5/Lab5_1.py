# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO

import telepot
from telepot.loop import MessageLoop

import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# LED_1_PIN 
''' start of you code '''
PIN = 16                                    
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, False) 
''' end of you code '''

# Setup DHT11 
''' start of you code '''
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']
''' end of you code '''

# GPIO#, ex: GPIO4 = Pin7
''' start of you code '''
gpio = 4
''' end of you code '''

def action(msg):
    # 解析從 Telegram Bot 收到的訊息，取出 chat_id 和 text
    # msg 為 nested dict 
    # 此處會用到的 function
    #   1. msg['...']
    ''' start of you code '''
    chat_id = msg['from']['id']
    command = msg['text']

    print('Received: {cmd}'.format(cmd = command))
    ''' end of you code '''

    # 判斷接收到的指令並控制 LED 燈
    # 此處會用到的 function
    #    1. GPIO.output(..., ...)
    #    2. telegram_bot.sendMessage(chat_id, message)
    if 'on' in command:
        ''' start of you code '''
        message = "Turned on the light"
        GPIO.output(PIN,GPIO.HIGH)
        telegram_bot.sendMessage(chat_id, message)
        ''' end of you code '''
    
    elif 'off' in command:
        ''' start of you code '''
        message = "Turned off the light"
        GPIO.output(PIN,GPIO.LOW)
        telegram_bot.sendMessage(chat_id, message)

        ''' end of you code '''

    # Get humidity & temperature
    # 此處會用到的 function
    #    1.  Adafruit_DHT.read_retry(...., ....)
    ''' start of you code '''
    humidity, temp = Adafruit_DHT.read_retry(sensor, gpio)
        
    ''' end of you code '''

    # 判斷接收到的指令並透過 Telegram Bot 回傳溫溼度給使用者
    # 此處會用到的 function
    #    1. telegram_bot.sendMessage(chat_id, message)
    ''' start of you code '''
    if 'humidity' in command:
        message = "The current humidity is " + str(humidity) + "%"
        telegram_bot.sendMessage(chat_id, message)
    ''' end of you code '''

    ''' start of you code '''
    if 'temperature' in command:
        message = "The current temperature is " + str(temp) + "%"
        telegram_bot.sendMessage(chat_id, message)
    ''' end of you code '''

# 填寫當初設定 Telegram Bot 的 token
''' start of you code '''
telegram_bot = telepot.Bot('6833994098:AAGnsxM65zEu9fGrPd-JU1ua1-A1nBFYMao')
''' end of you code '''

print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Send the command to turn on or off the light...')

while True:
    time.sleep(3)