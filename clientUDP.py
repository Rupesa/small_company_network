import socket
import signal
import sys
import time
import psutil

def signal_handler(sig, frame):
	print('\nDone!')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

ip_addr = "0.0.0.0"
udp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cont = 0
while True:
	cont +=1
	sock.sendto((str(cont) + ':').encode(), (ip_addr, udp_port))
	sock.sendto(('CPU used: ' + str(psutil.cpu_percent())).encode(), (ip_addr, udp_port))
	sock.sendto(('Memory used: ' + str(psutil.virtual_memory()[2])).encode(), (ip_addr, udp_port))
	time.sleep(5)
