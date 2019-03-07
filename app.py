from flask import Flask, request, render_template, jsonify  
from flask_restful import Resource, Api
import Action
from Action import openRackOne
import PiMotor
import time

app = Flask(__name__)
api = Api(app)

@app.route('/')
def unlockRack():
    return render_template('EDDSite.html')

@app.route('/Action')
def openingRack():
   return openRackOne()

# class CallPythonFile(Resource):
#   def get(file):
#     return {'data': Action.__package__}
    
#   api.add_resource(sumNumbers, '/sumtwonumbers/<first_number>/<second_number>')
# api.add_resource(Action, '/<')

# moobar
    
# if __name__ == '__main__':
#     app.run(debug=True)
#, method="post"
