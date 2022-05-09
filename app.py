from flask import Flask, jsonify
from flask_cors import CORS

import librosa


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Home"


@app.route("/nutcracker")
def nutcracker():
    filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    response = {
        'title': 'Nutcracker',
        'tempo': tempo,
        'key': 'C Major'
    }
    return jsonify(response)


@app.route("/sweetwaltz")
def sweetwaltz():
    filename = librosa.example('sweetwaltz')
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    response = {
        'title': 'Sweet Waltz',
        'tempo': tempo,
        'key': 'C Major'
    }
    return jsonify(response)


@app.route("/fishin")
def fishin():
    filename = librosa.example('fishin')
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    response = {
        'title': 'Fishin',
        'tempo': tempo,
        'key': 'C Major'
    }
    return jsonify(response)
