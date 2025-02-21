# import package
import bluetooth

# server bd_addr
bd_addr = "DC:A6:32:10:C5:AB"

port = 2

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# connect bd_addr and port
sock.connect((bd_addr, port))

# send data
sock.send("client_109511207 & server_109511094")

# close socket
sock.close()
