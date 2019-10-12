from bot import GEN
from flask import Flask, request
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    word = request.args.get('w')
    return GEN.generateText(6, word)
