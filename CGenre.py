from __future__ import division
import logging
try:
		from pydub import AudioSegment #pip install pydub and ffmeg
except ImportError:
		logging.exception('"pydub" is a required Python dependency for')
		raise
from pydub.playback import play #pip install pyaudio

class Genre(object):
    """
    param: song
    creates song file to be segmentes
    """
    def __init__(self,song):
        self.sound = AudioSegment.from_mp3(song)
        #print(self.sound.raw_data)

    """
    obtains maximum aplitude of mp3 song file
    """
    def max_amplitude(self):
        self.max = self.sound.max
        return self.max
    
    """
    obtains average loundness of mp3 song file
    """
    def loud(self):
        self.loudness = self.sound.rms
        return self.loudness

    """
    obtains duration of mp3 song file
    """
    def duration(self):
        self.durationlen = len(self.sound) / 1000.0
        return self.durationlen

    """
    obtains the frame_rate of mp3 file
    """
    def frame_rate(self):
        self.framerate = self.sound.frame_rate
        return self.framerate

    """
    obtains file size of the mp3 file
    """
    def sample_size(self):
        self.samplesize = self.sound.sample_width
        return self.samplesize

    def parseBySecond(self):
        newArr = []
        for i in range(len(self.sound)):
            newArr += [(self.sound[i]).rms]
        avgChange = 0
        for i in range(1,len(newArr)):
            avgChange += abs(newArr[i] - newArr[i-1])
        avgChange = avgChange/len(newArr)
        return avgChange
    #def raw_data(self):
    #    self.rawdata = self.sound.raw_data
    #    return self.rawdata

    """
    plays song file (on PC)
    """
    def play_song(self):
        play(self.sound)




