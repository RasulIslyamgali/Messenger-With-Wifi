import os
from socket import *

import pygame
from pygame import mixer

addr = ('10.0.0.206', 13000)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

mixer.init()
print('Waiting to receive messages...')

while True:
    (data, addr) = UDPSock.recvfrom(1024)
    if addr[0] == '10.0.0.206':
        pygame.mixer.music.load('new_message_tone.mp3')
        pygame.mixer.music.play(0)
        print('Rasul: ', data.decode('utf-8'))
    elif addr[0] == '172.16.208.187':
        pygame.mixer.music.load('new_message_tone.mp3')
        pygame.mixer.music.play(0)
        print('Nursultan: ', data.decode('utf-8'))
    elif addr[0] == '10.0.0.104':
        pygame.mixer.music.load('new_message_tone.mp3')
        pygame.mixer.music.play(0)
        print('Dimash: ', data.decode('utf-8'))

    if data.decode('utf-8').lower() == 'exit':
        break

UDPSock.close()

os._exit(0)
