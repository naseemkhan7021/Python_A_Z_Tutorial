import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 54321
s.bind((host,port))
s.listen()
print("Listening for new connection")

while True:
        #conn communicate and addr is finding client ip address and port no.
	conn, addr = s.accept()   # accept() inbuilt methot reterne to value to cammunicate and reciev ip address of client
	#print(cs)
	#print(addr)
	print("Connection recieved from  ",addr[0])
	msg = "Thank you for connecting"
	conn.send(msg.encode("UTF-8"))
	while True:
		msg2 = conn.recv(1024)
		if msg2:
			print(msg2.decode("UTF-8"))
		
		msg1 = input("Type message for client => ")
		if msg1:
			conn.send(msg1.encode("UTF-8"))
		
		
