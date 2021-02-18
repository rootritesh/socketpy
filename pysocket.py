import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ipsys=input("Enter the System IP: ")
portsys=int(input("Enter the System Port: "))

iprec=input("Enter the Client IP: ")
portrec=int(input("Enter the Client Port: "))

s.bind((ipsys,portsys))
def sender():
    while True:
        text=input("\nEnter the message: ")
        s.sendto(text.encode(), (iprec, portrec))
        print(s)

def rec():
    while True:
        x=s.recvfrom(1024)
        print("\nMessage from Client: " + x[0].decode())

        
t1=threading.Thread(target=rec)
t2=threading.Thread(target=sender)

t1.start()
t2.start()


