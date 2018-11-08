from __future__ import division
try:
        from pydub import AudioSegment #pip install pydub and ffmeg
except ImportError:
        logger.exception('"pydub" is a required Python dependency for')
        raise
#from pydub.playback import play #pip install pyaudio

def songToFeatures(filePath,genre):
    sound = AudioSegment.from_mp3(filePath)

    maxAmplitude = sound.max
    loudness = sound.rms
    durationlen = len(sound) / 1000.0
    frameRate = sound.frame_rate
    sample_size = sound.sample_width

    resArr = [maxAmplitude,loudness,durationlen,frameRate,sample_size,genre]
    return resArr