from pydub import AudioSegment
from pydub.playback import play
import time

def play_alarm():
		sound = AudioSegment.from_file('TF027.WAV')
		play(sound)
