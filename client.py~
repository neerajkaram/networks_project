'''Write a sockets program in which a client and server communicate point-to-point using UDP. N clients should be able to talk to a single server, and a single client should be able to talk to M servers'''

''' Extend (a) to a window-base protocol. You should be able to progress from stopand-wait
(window size = 1) to a window size =W.'''
import socket
import sys

print 'Number of clients:', len(sys.argv)-1, 'Clients.'
print 'List:', (sys.argv)[1:]

num_msg=input('Enter number of msgs ')

#importing port number from argumet list

port_list=[]
for port in (sys.argv[1:]):
	port_list.append(port)
print port_list


sockets={}
i = 0
for p in port_list:
	sockets.update({p:socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
})


#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Sockets created'
#packet_size = random._urandom(10240)
server_ip =  "localhost"
seq=0
for p  in sockets.keys():	
	msg="CSE networks msg from "+p
	seq=seq+1
	for  num_msg in sockets.keys(): #  in sockets.keys:
		sockets[p].sendto(msg, (server_ip,int(p)))
		sockets[p].sendto(str(seq), (server_ip,int(p)))
		print "message sent"
		#ack=sockets[p].recvfrom(1024)
		print "ack recived " #+ack
	#sockets[p].sendto("1", (server_ip,int(p)))
