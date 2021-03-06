from flask import Flask
from flask_cors import CORS
from flask_sse import sse

from blockchain.api import blueprint, blockchain
from robot.api import blueprint as robot

robot.blockchain = blockchain

app = Flask(__name__, static_url_path='/static', static_folder='../static/public')

CORS(app)

app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/api/stream')
app.register_blueprint(blueprint, url_prefix='/api/blockchain')
app.register_blueprint(robot, url_prefix='/api/robot')
