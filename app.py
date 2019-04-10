from flask import *
import Action
import ActionClose
from Action import openRackOne
from Action import openRackTwo
from ActionClose import closeRackOne
from ActionClose import closeRackTwo
import PiMotor
import time

app = Flask(__name__) # Runs app

@app.route('/') # base website 
def unlockRack():
    return render_template('EDDSite.html') #calls html

@app.route('/openRackOne.html')
def openingRackOne():
   Action.openRackOne()
   print('success')
   return render_template('openRackOne.html') 

@app.route('/openRackTwo.html')
def openingRackTwo():
    Action.openRackTwo()
    print('success')
    return render_template('openRackTwo.html')

@app.route('/closingRackOne.html')
def closeRackOne():
    ActionClose.closeRackOne()
    print('success')
    return render_template('closingRackOne.html')
    
@app.route('/closingRackTwo.html')
def closingRackTwo():
    ActionClose.closeRackTwo()
    print('success')
    return render_template('closingRackTwo.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
