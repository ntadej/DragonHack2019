from flask import Flask

from blockchain.api import blueprint as blockchain
from robot.api import blueprint as robot

app = Flask(__name__, static_url_path='/static', static_folder='../static/public')
app.register_blueprint(blockchain, url_prefix='/api/blockchain')
app.register_blueprint(robot, url_prefix='/api/robot')
