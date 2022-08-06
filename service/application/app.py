from flask import Flask, jsonify, request
from .produce import send_messages_in_kafka
from .models import Route
from threading import Thread

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route('/route', methods=['POST'])
def Export():
    try:
        data = {
            'route_id':request.args.get('route_id'),
            'client_id':request.args.get('client_id')
        }
        thread = Thread(target=send_messages_in_kafka, args=[data])
        thread.start()

        return jsonify({
            "status": "ok",
            "message": "System is running on thread"
        })
    except Exception as err:
        return jsonify({
            "error": err.args
        })