import PiMotor
import time


def openRackOne():
    m1 = PiMotor.Motor("MOTOR1",1) # defines motor
    ab = PiMotor.Arrow(1)
    af = PiMotor.Arrow(3) 
    x=1
    try:
        while (x==1):
            print("it worked")

            x = x-1
                            # code to control motors for rack one
            af.on()
            m1.forward(100)
            time.sleep(.5)
            af.off()
            ab.on()
            m1.reverse(100)
            time.sleep(.5)
            ab.off()
            m1.stop 
    except:
        print('you fucked up')

def openRackTwo():
    m2 = PiMotor.Motor("MOTOR2",1)
    ab = PiMotor.Arrow(1)
    af = PiMotor.Arrow(3) 
    x=1
    try:
        while (x==1):
            print("it worked")

            x = x-1
                            # code to control motors for rack two
            af.on()
            m2.forward(100)
            time.sleep(.5)
            af.off()
            ab.on()
            m2.reverse(100)
            time.sleep(.5)
            ab.off()
            m1.stop 
    except:
        print('you fucked up')
        