import time
import PiMotor

def closeRackOne():
	m1 = PiMotor.Motor("MOTOR1",1) # defines motor
	x=1
	
	try:
		while(x==1):
			print("it worked")

			x = x-1

			m1.reverse(100)
			time.sleep(.12)
			m1.stop
	except:
		print('you goofed up')

def closeRackTwo():
	m2 = PiMotor.Motor("MOTOR2",1)
	x=1
	try:
		while(x==1):
			print("it worked")

			x = x-1
                            # code to control motors for rack two
			m2.reverse(100)
			time.sleep(.35)
			m2.stop 
	except:
		print('you goofed up')
