from __future__ import division
from CGenre import Genre
import os

#from pydub.playback import play #pip install pyaudio

def songToFeatures(filePath,genre):
    #song = '/Songs/Single-Ladies.mp3' 
    #path = os.path.dirname(os.getcwd()) + song
    #song = songToFeatures(path,"pop")
    #sound = AudioSegment.from_mp3(filePath)
    Features = Genre(filePath)
    maxAmplitude = Features.max_amplitude()
    loudness = Features.loud()
    duration_len = Features.duration()
    frame_rate = Features.frame_rate()
    sample_size = Features.sample_size()
    resArr = [maxAmplitude,loudness,duration_len,frame_rate,sample_size,genre]
    print resArr
    return resArr