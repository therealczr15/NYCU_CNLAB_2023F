# -*- coding: utf-8 -*-
import os
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:7788")

print('Worker %s is running ...' % os.getpid())

while True:
    # Receive a, b from the client
    # 此處會用到的 function
    #   1. socket.recv_multipart()
    ''' start of you code '''
    list = socket.recv_multipart()
    print('Compute ' + list[0] +  ' + ' +  list[1] + ' and send response')
    ''' end of you code '''

    # Return the result back to the client
    # 此處會用到的 function
    #   1. socket.send_string(....)
    ''' start of you code '''
    ans = int(list[0]) + int(list[1])
    socket.send_string(str(ans) + ' ( from worker %s)' % os.getpid() )
    ''' end of you code '''



