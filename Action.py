import PiMotor
import time


def openRackOne():
    m1 = PiMotor.Motor("MOTOR1",1) # defines motor

    x=1
    try:
        while (x==1):
            print("it worked")

            x = x-1
                            # code to control motors for rack one
            m1.forward(50)
            time.sleep(.5)
            m1.stop

    except:
        print('you goofed up')
        
def openRackTwo():
    m2 = PiMotor.Motor("MOTOR2",1) # defines motor

    x=1
    try:
        while (x==1):
            print("it worked")

            x = x-1
                            # code to control motors for rack one           
            m2.forward(50)
            time.sleep(.5)
            m2.stop

    except:
        print('you goofed up')        

