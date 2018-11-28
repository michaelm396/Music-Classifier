from __future__ import division
from CGenre import Genre
import os

#from pydub.playback import play #pip install pyaudio

def songToFeatures(filePath,genre):

    Features = Genre(filePath)
    #maxAmplitude = Features.max_amplitude()
    loudness = (Features.loud() / 16332.0)*3
    duration_len = (Features.duration() / 374.19)
    avgChange = (Features.parseBySecond() / 4624.60137)
    avgAmpChange = (Features.amplitudePerMili() / 4751.36598)

    resArr = [avgAmpChange,loudness,duration_len,avgChange,genre]
    #resArr = [avgAmpChange,genre]
    print(resArr+[filePath])
    #print(avgAmpChange)

    return resArr