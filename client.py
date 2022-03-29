import os
from socket import *

UDPSock = socket(AF_INET, SOCK_DGRAM)

contacts = ['10.0.0.104', '10.0.0.206', '172.16.208.187']
while True:
    data = input("Enter message to send or type 'exit': ")
    print(data)
    for contact in contacts:
        UDPSock.sendto(bytes(data, 'utf-8'), (contact, 13000))
    if data.lower() == 'exit':
        break


UDPSock.close()
os._exit(0)
