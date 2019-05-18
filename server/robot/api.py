from flask import Blueprint, g, Response
from flask_restplus import Api, Resource, fields
from flask_restplus.reqparse import RequestParser
from flask_sse import sse

from common import app_name, app_slogan
from blockchain.blockchain import Blockchain

# Instantiate the Node
blueprint = Blueprint('robot', __name__)
api = Api(blueprint, version='1.0', title=f'{app_name} Robot API', description=app_slogan)


directionParser = RequestParser()
directionParser.add_argument('left', type=int, required=True)
directionParser.add_argument('right', type=int, required=True)

currentInstruction = 'stop'
direction = {
    'left': None,
    'right': None,
}

@api.route('/start')
class Start(Resource):

    def get(self):
        global currentInstruction

        sse.publish({"message": "Starting movement ..."}, type='chat')

        currentInstruction = 'drive'

        return {
            'status': 'ok'
        }

@api.route('/stop')
class Stop(Resource):

    def get(self):
        global currentInstruction

        sse.publish({"message": "Stopping ..."}, type='chat')

        currentInstruction = 'stop'

        return {
            'status': 'ok'
        }

@api.route('/instructions')
class Instructions(Resource):

    def get(self):
        return currentInstruction

@api.route('/direction/get')
class DirectionGet(Resource):

    def get(self):
        if direction['left'] == None or direction['right'] == None:
            return ''

        return f'{direction["left"]} {direction["right"]}'


@api.route('/direction/set')
class DirectionSet(Resource):

    @api.expect(directionParser)
    def get(self):
        global direction
        
        direction = directionParser.parse_args()
        return direction


@api.route('/direction/reset')
class DirectionReset(Resource):

    def get(self):
        global direction
        
        direction = {
            'left': None,
            'right': None,
        }

        return {}


sensesModel = api.model("Senses", {
    "current_time": fields.String(description="Time"),
    "temperature": fields.Float(description="Temperature"),
    "pressure": fields.Float(description="Pressure"),
    "humidity": fields.Float(description="Humidity"),
})

@api.route('/senses')
class Senses(Resource):

    @api.expect(sensesModel)
    def post(self):
        values = api.payload

        sse.publish(values, type='telemetry')

        return values
