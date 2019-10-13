from bot import GEN
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def hello_world():
    word = request.args.get('w')
    return GEN.generateText(6, word)
