                            #import all neccesary items
rom flask import *
import Action
import ActionClose
from Action import openRackOne
from Action import openRackTwo
from ActionClose import closeRackOne    
from ActionClose import closeRackTwo
import PiMotor
import time

app = Flask(__name__) # Runs app

@app.route('/') #home of website 
def unlockRack():
    return render_template('EDDSite.html') #calls html

@app.route('/openRackOne.html') #creates site url
def openingRackOne():
   Action.openRackOne() #calls the opening function
   print('success')
   return render_template('openRackOne.html') #calls html site

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
    app.run(host="0.0.0.0", debug=True)  #sets the website address to 0.0.0.0
