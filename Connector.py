import socket
import time

ip = input("Enter the IP : ")
port = int(input("Enter the port number : "))

time.sleep(1)
print("-- Starting connection --")
time.sleep(1)

try :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    print("-- Connected successfully --\n")
    msg = input("Enter your message... :\n")
    s.sendall(msg.encode())
    s.close()

except Exception :
    print ("Error!!, make sure that the IP is correct \nor the server is still alive!!")





