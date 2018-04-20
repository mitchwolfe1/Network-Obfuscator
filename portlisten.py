import socket
import sys
from threading import Thread
import time
import os
if(len(sys.argv) == 3):
	startPort = int(sys.argv[1])
	endPort = int(sys.argv[2])
elif(sys.argv[1] == 'stop'):
	print('Killing python process')
	os.system('killall -9 python')
else:
	print 'Usage: python ' + sys.argv[0] + '[STARTPORT] [ENDPORT]'
	sys.exit()

if((endPort - startPort) > 500):
	print 'Cannot handle that amount of ports. Please keep the amount of ports under 500'
	sys.exit()
def openPort(PORT):
	HOST = ''
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print 'Error: ' + str(msg[0]) + ' Message: ' + msg[1]
		sys.exit()

	s.listen(10)
	print 'Socket listening on port ' + str(PORT)
	while True:
		s.accept()
	sys.exit()
try:
	i = 0
	threads = []
	while(startPort <= endPort):
		threads.append(Thread(target = openPort, args=(startPort,)))
		startPort+=1
	for t in threads:
		t.start()

except KeyboardInterrupt:
	print 'KeyboardInterrupt: Stopping Now'
	sys.exit()


