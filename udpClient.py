'''Author: Neeraj Date: 04/27/2016 ver:2.1 '''
import json
import socket

import time

import select

import CONSTANTS
# address ad port
UDP_IP = "127.0.0.1"
UDP_CLIENT_PORT_1 = 5001
UDP_CHANNEL_PORT = CONSTANTS.UDP_CHANNEL_PORT
SENDING_TO_SERVER_PORT1 = 5000
# creating UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)

# binding
sock.bind((UDP_IP, UDP_CLIENT_PORT_1))
# sock.timeo
print 'I am client. My port is ', UDP_CLIENT_PORT_1

# take the number of msgs to send to server
n = int(raw_input("enter number of msgs "))
messages = {}
for i in range(int(n)):
    messages[i] = 'Hello World '+str(i)

# take input for size of stop and wait window
w = int(raw_input("Window size "))
if n < w:
    w=n
window_starts = 0
window_ends = w-1
seq = 0
acked_messages = []
window = messages.keys()[0:w]
while (messages):
    # if len(messages) < w:
    #     w = len(messages)
    for i in window:
        print window
        msg = {'message': messages[i], 'port_to': SENDING_TO_SERVER_PORT1, 'port_from': UDP_CLIENT_PORT_1, 'seq_no': i}
        print 'Sending '+ messages[i] + ' to ' +  str(SENDING_TO_SERVER_PORT1)
        # sending to server port
        sock.sendto(json.dumps(msg), (UDP_IP, CONSTANTS.UDP_CHANNEL_PORT))


    # time.sleep(5)
    input = [sock]

    # inputready,outputready,exceptready = select.select(input,[],[])
    # for s in inputready:
    try:
        for i in range(len(window)):
            receivedbytes = sock.recv(1024)
            ack_data = json.loads(receivedbytes)
            print ack_data
            acked_messages.append(ack_data['seq_no'])
            window.remove(int(ack_data['seq_no']))
            window_ends = window_ends+1
            if window_ends<n:
                window.append(window_ends)
            messages.pop(ack_data['seq_no'])
            print "Ack received for", ack_data['seq_no']
    except Exception as e:
        print e.message

    print 'Remaining messages\n'
    print window
    if len(window) is 0:
        print 'last run'
        print messages
        break



# seq = 0
# for i in range(0, int(n), 1):
#     seq = seq + i
#     msg = {'message': "Hello world " + str(i), 'port_to':5000, 'port_from': 145, 'seq_no': seq+1}
#     # sending to server port
#     sock.sendto(json.dumps(msg), (UDP_IP, CONSTANTS.UDP_CHANNEL_PORT))
#
#     data, addr = sock.recvfrom(1024)
#     print "Ack received" + data

# closing the connection
sock.close()
