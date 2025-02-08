from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import piplates.MOTORplate as MT

MT.dcCONFIG(0,1, 'ccw', 50.0, 2.5)
MT.dcCONFIG(0,2, 'ccw', 50.0, 2.5)
MT.dcCONFIG(0,3, 'ccw', 50.0, 2.5)
MT.dcCONFIG(0,4, 'ccw', 50.0, 2.5)

factory = PiGPIOFactory()

servo = AngularServo(18, min_angle=-180, max_angle=180, min_pulse_width=0.001, 
	max_pulse_width=0.002,pin_factory=factory)

while (True):
	servo.angle=150
	MT.dcSTART(0,1)
	MT.dcSTART(0,2)
	MT.dcSTART(0,3)
	MT.dcSTART(0,4)	
	sleep(2)
	MT.dcSPEED(0,1,100.0)
	MT.dcSPEED(0,2,100.0)
	MT.dcSPEED(0,3,100.0)
	MT.dcSPEED(0,4,100.0)

	servo.angle=0
	sleep(2)
	servo.angle=-180
	sleep(2)

	MT.dcSTOP(0,1)
	MT.dcSTOP(0,2)
	MT.dcSTOP(0,3)
	MT.dcSTOP(0,4)

servo.angle=0


