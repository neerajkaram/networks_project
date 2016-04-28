'''Author: Neeraj Date: 04/27/2016 ver:2.1 '''

import socket

#address ad port
UDP_IP = "127.0.0.1"
UDP_PORT = 5001

#creating UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

#binding 
sock.bind((UDP_IP, UDP_PORT))


#take the number of msgs to send to server
n=raw_input("enter number of msgs ")

#take input for size of stop and wait window
w=raw_input("Window size ")

seq=0
for i in range(0,int(n),1):
    msg="Hello world "+str(i)
    seq=seq+i
    #sending to server port
    sock.sendto(msg, (UDP_IP, 5000))
    sock.sendto(str(seq), (UDP_IP, 5000))
    data, addr = sock.recvfrom(1024)
    print "Ack recived"+data

#closing the connection
sock.close()


