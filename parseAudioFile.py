from __future__ import division
from CGenre import Genre
import os
import csv
#from pydub.playback import play #pip install pyaudio

def songToFeatures(filePath,genre):

    Features = Genre(filePath)
    #maxAmplitude = Features.max_amplitude()
    loudness = (Features.loud() / 16332.0)*3
    duration_len = (Features.duration() / 374.19)
    avgChange = (Features.parseBySecond() / 4624.60137)
    avgAmpChange = (Features.amplitudePerMili() / 4751.36598)
    Energy = (Features.energy() / 55.81395349) #divide by average
    Freq = (Features.frequency_fft()/ 202.5245728)

    if ("Songs/train" in filePath):
        myFile = open('csvtrain.csv', 'a')  
        with myFile as f: 
            writer = csv.writer(f)
            writer.writerow([avgAmpChange,loudness,duration_len,avgChange,Energy,Freq])
    
    if ("Songs/test" in filePath):
        myFile = open('csvtest.csv', 'a')   
        with myFile as f:  
            writer = csv.writer(f)
            writer.writerow([avgAmpChange,loudness,duration_len,avgChange,Energy,Freq])

    resArr = [avgAmpChange,loudness,duration_len,avgChange,Energy,Freq,genre]
    #resArr = [avgAmpChange,loudness,duration_len,avgChange,genre] #returns coorectness of 74%
    #resArr = [avgAmpChange,loudness,duration_len,avgChange,genre] # returns correctness of 68%
    #resArr = [loudness,genre]
    #resArr = [Freq,genre]
    #resArr = [avgAmpChange,genre]
    print(resArr+[filePath])
    #print(avgAmpChange)

    return resArr