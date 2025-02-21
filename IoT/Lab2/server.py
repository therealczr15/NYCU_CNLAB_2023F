# import package
import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port=2

# server bd_addr
server_sock.bind(("B8:27:EB:7C:05:7B", port))
# the maximum allowable number of connections is 1
server_sock.listen(1)

# get client socket and address
client_sock, address= server_sock.accept()
print "Accepted connection from ", address

data = client_sock.recv(1024)
# output received data
print "received [%s]" % data

# close connection of server and client
client_sock.close()
server_sock.close()
