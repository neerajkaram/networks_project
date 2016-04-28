'''Author: Neeraj Date: 04/27/2016 ver:2.1 '''

import socket

#address,port of the server
UDP_IP = "127.0.0.1"
UDP_PORT = 5000

#creating a UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

#binding the address
sock.bind((UDP_IP, UDP_PORT))


print "Server listening"

while True:
	data, addr = sock.recvfrom(1024) # recving from client and buffer size is 1024 bytes
	print "Receving message from:",str(addr)
	print ""
	print "received message:", data
	seq, addr = sock.recvfrom(1024)
	print "Seq no. is " +seq
	print "Preparing to send ack: " + seq
	#sending back the ack from where we were recving data
	sock.sendto(str(seq),addr)
	print "sent ack"
	#print "address", addr
sock.close()


