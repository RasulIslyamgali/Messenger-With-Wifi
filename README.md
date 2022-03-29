# Messenger-With-Wifi

Simple messenge for recognition with desktops in same wifi network


requirements:
- pygame


how launch:
pip install pygame (forgot make pip freeze > requirements.txt)

and in one terminal launch server with below command:
python server.py

in another terminal launch client with command:
python client.py

Could be replace the line ```addr = ('10.0.0.206', 13000)``` with your own ipv4 address.

You can check your ipv4 address with command:
on windows:
ipconfig /all

on ubuntu:
ip a
