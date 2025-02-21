# -*- coding: utf-8 -*-
from flask import Flask, request, Response, jsonify, make_response

from flask_restful import Api
from flask_restful import Resource

import random
import Adafruit_DHT

# Setup DHT11 
sensor_args = {'11' : Adafruit_DHT.DHT11,
               '22': Adafruit_DHT.DHT22,
               '2302': Adafruit_DHT.AM2302}
sensor = sensor_args['11']

# GPIO#, ex: GPIO4 = Pin7
gpio = 4

class MyApp(Resource):
    def get(self):
        return Response(
            '''
            Welcome to my humidity&temperature RESTful API.
            Please make a HTTP POST request to this app, and you can
            decide to get the humidity or temperature data.
            The json embedded in the request woudl be:

            {
                "user" : "309577777",
                "data" : "H"
            }

            or

            {
                "user" : "309577777",
                "data" : "T"
            }
            '''
        )
    
    def post(self):
        json = request.get_json()

        if len(json) == 0:
            # 若使用者傳入的 Json 為空白的話，需回傳 HTTP Status Code = 400 的網頁內容
            # 此處會用到的 functions
            #    1. jsonify(message = ....)
            #    2. make_response(...., 400)

            ''' start of you code '''
            return make_response(jsonify(message = "Status Code = 400"),400)
            ''' end of you code '''
        
        ID = str(json['user'])
        data_type = json['data']


        # 從溫濕度模組取的數值
        # 此處會用到的 function
        #    1.  Adafruit_DHT.read_retry(...., ....)
 
        ''' start of you code '''
        humidity = random.randint(20,30)
        temp = random.randint(20,40)
        ''' end of you code '''
   
        # 從 json field "data" 中判斷使用者想要的是溫度還是濕度，還有例外判斷(else 的部分)
        # 此處會用到的 functions
        #    1. jsonify(message = ....)
        #    2. make_response(...., 200) or make_response(...., 400) (else 部分) 
        #
        ''' start of you code '''
    
    
    
        ''' end of you code '''
        
        if data_type == 'T':
            ''' start of you code '''
            temp = str(temp)
            return make_response(jsonify(message = "Hi, 109511207 the current temperature is " +  temp + " C"), 200)
            
            
            ''' end of you code '''
        
        elif data_type == 'H':
            ''' start of you code '''
            humidity = str(humidity)
            return make_response(jsonify(message = "Hi, 109511207 the current humidity is " +  humidity + " %"), 200)
            
            
            ''' end of you code '''
        
        else:
            ''' start of you code '''
            return make_response(jsonify(message = "Status Code = 400"),400)
            
            ''' end of you code '''

app = Flask(__name__)      
api = Api(app)

api.add_resource(MyApp, '/')

if __name__ == '__main__':
    app.run(host = '192.168.0.129', port = 9999, debug = True)