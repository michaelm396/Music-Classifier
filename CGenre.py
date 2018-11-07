from __future__ import division
try:
		from pydub import AudioSegment #pip install pydub and ffmeg
except ImportError:
		logger.exception('"pydub" is a required Python dependency for')
		raise
from pydub.playback import play #pip install pyaudio

class Genre(object):
    def __init__(self,song):
        self.sound = AudioSegment.from_mp3(song)

    def max_amplitude(self):
        self.max = self.sound.max
        return self.max
    
    def loud(self):
        self.loudness = self.sound.rms
        return self.loudness

    def duration(self):
        self.durationlen = len(self.sound) / 1000.0

    def play_song(self):
        play(self.sound)




