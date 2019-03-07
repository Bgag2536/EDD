from tkinter import *
import tkinter.messagebox
import PiMotor
import time
root = Tk()
tkinter.messagebox.showinfo("It worked!","Youre a genius aka can follow youtube videos")

root.mainloop()

def openRackOne():
    m1 = PiMotor.Motor("MOTOR1",1)
    ab = PiMotor.Arrow(1)
    al = PiMotor.Arrow(2)
    af = PiMotor.Arrow(3) 
    ar = PiMotor.Arrow(4)
    x=1
    try:
        while (x==1):
            print("it worked")

            x = x-1

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
        