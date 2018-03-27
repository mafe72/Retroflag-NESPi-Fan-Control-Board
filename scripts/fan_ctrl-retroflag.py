#####################################
# RetroFlag NESPi Control Board Script
#####################################
# Hardware:
# Board by Eladio Martinez
# http://mini-mods.com
#
#####################################
# Wiring:
#  GPIO 4  Fan on signal (OUTPUT)
#
#####################################
#  Required python libraries
#  sudo apt-get update
#  sudo apt-get install python-dev python-pip python-gpiozero
#  sudo pip install psutil pyserial
#
#####################################
# Basic Usage:
#  FAN ON
#	Fan will turn ON when temperature exceeded 55C
#  FAN OFF
#	Fan will turn OFF when temperature under 40C

import RPi.GPIO as GPIO
import time
import os
import socket
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
fan = GPIO.PWM(4, 50) #PWM frequency set to 50Hz

#Get CPU Temperature
def getCPUtemp():
	res = os.popen('vcgencmd measure_temp').readline()
	return (res.replace("temp=","").replace("'C\n",""))
	
while True:
	#Fan control
	#Adjust MIN and MAX TEMP as needed to keep the FAN from kicking
	#on and off with only a one second loop
	cpuTemp = int(float(getCPUtemp()))
	fanOnTemp = 55  #Turn on fan when exceeded
	fanOffTemp = 40  #Turn off fan when under
	if cpuTemp >= fanOnTemp:
		fan.start(40) #40% duty cycle
	if cpuTemp < fanOffTemp:
		fan.stop()
	time.sleep(1.00)
