import RPi.GPIO as GPIO
import time
from time import sleep
from gpiozero import PWMLED
GPIO.setwarnings(False)

from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)


def ping():
	"""Get reading from HC-SR04"""
	GPIO.setmode(GPIO.BCM)
	 
	TRIG = 23 
	ECHO = 18
	 
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	
	GPIO.output(TRIG, False)
	time.sleep(1)
	
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	
	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()
	  
	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	 
	distance = pulse_duration * 17150
	 
	distance = round(distance, 2)
	distance_in_m = distance / 100
	distance_in_m = round(distance_in_m , 2)
	print("Distance: "+ str(distance) + "cm")
	print("Distance: "+ str(distance_in_m) + "m")
	led.pulse()
	led.value = 1 - distance_in_m
	sleep(0.001)
	

print(" Reading distance " )

while True:
    ping()
    
    

    
