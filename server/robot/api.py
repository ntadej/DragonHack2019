from flask import Blueprint, g
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
        response = direction

        return response


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
