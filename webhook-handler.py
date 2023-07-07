from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json)
    return Response(status=200)

if __name__ == '__main__':
    app.run(port=5000)
