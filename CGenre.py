from __future__ import division
import logging

try:
		from pydub import AudioSegment #pip install pydub and ffmeg
except ImportError:
		logging.exception('"pydub" is a required Python dependency for')
		raise
from pydub.playback import play #pip install pyaudio
from pydub.silence import detect_nonsilent
#from aubio import source, tempo
import numpy.fft
import array

class Genre(object):
    """
    param: song
    creates song file to be segmentes
    """
    def __init__(self,song):
        self.sound = AudioSegment.from_mp3(song)

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
    obtains the frame_rate (sample period) of mp3 file
    """
    def frame_rate(self):
        self.framerate = self.sound.frame_rate
        self.framerate = self.framerate
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


    def amplitudePerMili(self):
        newArr = []
        for i in range(len(self.sound)):
            newArr += [(self.sound[i]).max]
        avgChange = 0
        for i in range(1,len(newArr)):
            avgChange += abs(newArr[i] - newArr[i-1])
        avgChange = avgChange/len(newArr)
        return avgChange

    """
    Calculates Energy of a song file
    """
    def energy(self):     
        maxLoudness = self.sound.dBFS # Max loundeness for threshold
        minLoudness = int(60000 / 240.0) # Minimum threshold for sound (detect_silence documentation) (every 60 seconds) (240 frq)
        nonsilent_times = detect_nonsilent(self.sound, minLoudness, maxLoudness) #calulates when sound is active
        soundBetweenBeats = []
        val = nonsilent_times[0][0]         
                                     
        for peak in nonsilent_times[1:]:
            soundBetweenBeats.append(peak[0] - val)
            val = peak[0]

        soundBetweenBeats = sorted(soundBetweenBeats)
        space = soundBetweenBeats[len(soundBetweenBeats) // 2] # Median energy between sound 
        energy = 60000 / space #energy per minute (milliseconds)
        return energy

    """
    sum = []
    var = 0
    for peak in nonsilent_times:
        for block in peak:
            var = var + block
        sum.append(var)
        var = 0
    avg = 0
    for i in range(len(nonsilent_times)):
        avg = avg + sum[i]
    avgEnergy = avg/len(nonsilent_times)
    return avgEnergy
    """
    
    """
    Calculates the DFT using fast fourier transform algorithm (https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/)
        Returns: Average frequency coefficient over the time interval
    """
    def frequency_fft(self):
        signal = self.sound.get_array_of_samples() #returns the raw_data as an array of samples (signal) in milliseconds
        shiftedsignal = numpy.right_shift(signal, 1) #reduces ampltitude of samples in order to equalize the sound
        shiftedsignalarray = array.array(self.sound.array_type, shiftedsignal)
        numberofsignals = len(shiftedsignalarray)
        Fk = numpy.fft.fft(shiftedsignalarray)/numberofsignals #returns normalized FFT
        nK = numpy.fft.fftfreq(numberofsignals)
        idx = numpy.argmax(numpy.abs(Fk)) #peak of frequency coefficient
        nK = nK[idx]
        freq_in_hertz = abs(nK * self.sound.frame_rate)
        return freq_in_hertz

    """
    plays song file (on PC)
    """
    def play_song(self):
        play(self.sound)




