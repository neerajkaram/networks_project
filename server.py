'''Write a sockets program in which a client and server communicate point-to-point using UDP. N clients should be able to talk to a single server, and a single client should be able to talk to M servers'''

#server

import socket
import sys


print 'Number of Servers:', len(sys.argv)-1, 'Servers'
print 'List:', (sys.argv)[1:]

port_list=[]
for port in (sys.argv[1:]):
        port_list.append(port)
print "Ports to reach"
print port_list


sockets={}
i = 0
for p in port_list:
        sockets.update({p:socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
})


#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Socket created'

server_ip =  "localhost"


for p  in sockets.keys():
	addr=(server_ip,int(p))
	sockets[p].bind(addr)
	msg=sockets[p].recvfrom(1024)

	print "Msg recived:",msg
	msg1=sockets[p].recvfrom(1024)
	print "seq:",msg1
	print "seq recived"
	print "sending ack"
	sockets[p].sendto(str(msg1), (server_ip,int(p)))
	print "ack sent"
