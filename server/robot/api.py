from flask import Blueprint, g, Response
from flask_restplus import Api, Resource, fields
from flask_restplus.reqparse import RequestParser

from common import app_name, app_slogan
from blockchain.blockchain import Blockchain

# Instantiate the Node
blueprint = Blueprint('robot', __name__)
api = Api(blueprint, version='1.0', title=f'{app_name} Robot API', description=app_slogan)


directionParser = RequestParser()
directionParser.add_argument('left', type=int, required=True)
directionParser.add_argument('right', type=int, required=True)


direction = {
    'left': None,
    'right': None,
}


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


messages = ['test']

@blueprint.route('/stream')
def stream():
    def eventStream():
        while True:
            import time
            time.sleep(1)
            # Poll data from the database
            # and see if there's a new message
            if len(messages):
                yield f'data: {messages[0]}\n\n'
    
    return Response(eventStream(), mimetype="text/event-stream")
