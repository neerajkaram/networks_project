'''Author: Neeraj Date: 04/27/2016 ver:2.1 '''
import json
import socket

# address,port of the server
UDP_IP = "127.0.0.1"
UDP_SERVER_PORT = 5000

print 'I am server. My port is ' ,UDP_SERVER_PORT

# creating a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binding the address
sock.bind((UDP_IP, UDP_SERVER_PORT))

print "Server listening"

while True:
    raw_data, addr = sock.recvfrom(1024)  # recving from client and buffer size is 1024 bytes
    print "Receving message from:", str(addr)
    print ""
    print "received message:", raw_data
    data = json.loads(raw_data)
    print "Seq no. is " , data['seq_no']

# uncomment below line when you want to test that server doesn't ack for message no. 3
    # if data['seq_no'] != 3:

    print "Preparing to send ack: "
    # sending back the ack from where we were recving data
    ack_message = {'message': 'ACK', 'port_to': data['port_from'], 'port_from': data['port_to'], 'seq_no': data['seq_no']}
    sock.sendto(json.dumps(ack_message), addr)
    print "sent ack"
# print "address", addr
sock.close()
