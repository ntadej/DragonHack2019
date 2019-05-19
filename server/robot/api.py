from flask import Blueprint, g, Response
from flask_restplus import Api, Resource, fields
from flask_restplus.reqparse import RequestParser
from flask_sse import sse

from common import app_name, app_slogan
from blockchain.blockchain import Blockchain


class RobotWithBlockchain(Blueprint):

    def __init__(self, name, underscore_name, blockchain=None):

        super(RobotWithBlockchain, self).__init__(name, underscore_name)

        self.blockchain = blockchain

# Instantiate the Node
blueprint = RobotWithBlockchain('robot', __name__)
api = Api(blueprint, version='1.0', title=f'{app_name} Robot API', description=app_slogan)


directionParser = RequestParser()
directionParser.add_argument('left', type=int, required=True)
directionParser.add_argument('right', type=int, required=True)

dropParser = RequestParser()
dropParser.add_argument('enable', type=int, required=True)

statusParser = RequestParser()
statusParser.add_argument('state', type=str, required=True)
statusParser.add_argument('timestamp', type=str, required=True)

dropState = 0
currentInstruction = 'stop'
direction = {
    'left': None,
    'right': None,
}
lastStatus = None
lastOrientation = None

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

@api.route('/obstacle')
class Obstacle(Resource):

    def get(self):
        sse.publish({"message": "Obstacle found!"}, type='chat')
        sse.publish({"obstacle": True, "orientation": lastOrientation}, type='robot')
        return currentInstruction

@api.route('/status')
class Status(Resource):

    @api.expect(statusParser)
    def get(self):
        global lastStatus

        status = statusParser.parse_args()

        if lastStatus:
            diff = int(status['timestamp']) - int(lastStatus['timestamp'])
            delta = diff
            if status['state'] == 'stopped' and lastStatus['state'] == 'stopped':
                pass
            elif status['state'] == 'stopped' or lastStatus['state'] == 'stopped':
                sse.publish({"delta": delta/2, "orientation": lastOrientation}, type='robot')
            else:
                sse.publish({"delta": delta, "orientation": lastOrientation}, type='robot')
        lastStatus = status
        if currentInstruction == "drive":
            return "1 1"
        else:
            return "0 0"


@api.route('/drop/get')
class DropGet(Resource):

    def get(self):
        return f'{dropState}'


@api.route('/drop/set')
class DropSet(Resource):

    @api.expect(dropParser)
    def get(self):
        global dropState

        dropState = dropParser.parse_args()
        return direction


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
        global lastOrientation

        values = api.payload

        blueprint.blockchain.add_transaction(values)

        lastOrientation = values['orientation']

        sse.publish(values, type='telemetry')

        return values


@api.route('/history')
class DataHistory(Resource):

    def get(self):
        try:
            return blueprint.blockchain.getDataHistory()
        except:
            return []
