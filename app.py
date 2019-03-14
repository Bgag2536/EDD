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

@app.route('/openingrackone')
def openingRackOne():
   return render_template('openRackOne.html') 

@app.route('/openingracktwo')
def openingRackTwo():
   return render_template('openRackTwo.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    
