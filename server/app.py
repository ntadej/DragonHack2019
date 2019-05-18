from flask import Flask

from blockchain.api import blueprint as blockchain
from robot.api import blueprint as robot

app = Flask(__name__)
app.register_blueprint(blockchain, url_prefix='/api/blockchain')
app.register_blueprint(robot, url_prefix='/api/robot')

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)