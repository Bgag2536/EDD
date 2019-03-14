from flask import *
import Action
from Action import openRackOne
from Action import openRackTwo
import PiMotor
import time

app = Flask(__name__) # Runs app

@app.route('/') # base website 
def unlockRack():
    return render_template('EDDSite.html') #calls html

@app.route('/OpeningRackOne') # opens site not generated yet but sends command and opens rack
def openingRackOne():
   return openRackOne() # defined in action.py with code to activate motors

@app.route('/OpeningRackTwo')
def OpeningRackTwo():
   return openRackOne()


