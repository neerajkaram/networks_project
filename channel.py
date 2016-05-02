'''Author: Neeraj Date: 04/27/2016 ver:2.1 '''
#assuming  high loss rate to be 60% and low loss rate to be 10%
#high loss rate regime : 5 packets, low loss rate regime: 10 packets
import json
import random
import socket
import copy



# address,port of the channel
import math

IP = "127.0.0.1"
CHANNEL_PORT = 5002

print 'I am channel. My port is ', CHANNEL_PORT
mode = int(raw_input("Enter 1,2 or 3 for choice of normal mode, random loss mode or bursty loss mode: "))


high_loss_packet = [1,1,0,0,0]
low_loss_packet = [1,1,1,1,1,1,1,1,1,0]


def choose_0_or_1_randomly():
    choice = random.random()
    return bool(round(choice))

def choose_regime_randomly():
    first_choice = choose_0_or_1_randomly()
    if first_choice:
        random.shuffle(high_loss_packet)
        print 'choosing high loss regime'
        return high_loss_packet
    else:
        random.shuffle(low_loss_packet)
        return low_loss_packet
        print 'choosing low loss regime'



class BurstPacket():
    def __init__(self):
        self.packet_pointer = 0
        self.regime = choose_regime_randomly()

    def packet_to_lose(self):
        if self.packet_pointer == len(self.regime)-1:
            self.regime = choose_regime_randomly()
            self.packet_pointer = 0
        else:
            self.packet_pointer = self.packet_pointer+1
        return bool(self.regime[self.packet_pointer])


# creating a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if mode == 3:
    bp = BurstPacket()
# binding the address
sock.bind((IP, CHANNEL_PORT))











print "Channel on"

while True:
    if mode ==3:
        bp = BurstPacket()

    data, addr = sock.recvfrom(1024)  # recving from client and buffer size is 1024 bytes
    new_data = json.loads(data)
    print "Passing message from:", str(new_data['port_from'])
    print "received message:", new_data['message']
    print 'seq_no', new_data['seq_no']
    print 'to ' + str(new_data['port_to'])
    if mode == 1:
        sock.sendto(data, (IP, new_data['port_to']))
    elif mode == 2:
        choice = choose_0_or_1_randomly()
        if choice:
            sock.sendto(data, (IP, new_data['port_to']))
        else:
            print('dropping this packet')
    elif mode == 3:
        choice = bp.packet_to_lose()
        if choice:
            sock.sendto(data, (IP, new_data['port_to']))
        else:
            print('dropping this packet')

sock.close()
