from flask import Flask
import librosa


app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


@app.route("/nutcracker")
def nutcracker():
    filename = librosa.example('nutcracker')
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return 'Estimated tempo: {:.2f} beats per minute'.format(tempo)


@app.route("/sweetwaltz")
def sweetwaltz():
    filename = librosa.example('sweetwaltz')
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return 'Estimated tempo: {:.2f} beats per minute'.format(tempo)

@app.route("/fishin")
def fishin():
    filename = librosa.example('fishin')
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return 'Estimated tempo: {:.2f} beats per minute'.format(tempo)
