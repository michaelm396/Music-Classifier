from __future__ import division
from CGenre import Genre
import os

#from pydub.playback import play #pip install pyaudio

def songToFeatures(filePath,genre):

    Features = Genre(filePath)
    maxAmplitude = Features.max_amplitude()
    loudness = Features.loud()
    duration_len = Features.duration()
    avgChange = Features.parseBySecond()

    resArr = [maxAmplitude,loudness,duration_len,avgChange,genre]
    print(resArr)

    return resArr