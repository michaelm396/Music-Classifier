#from pytube import Youtube
from __future__ import division
from pydub import AudioSegment #(pip install pydub and ffmeg)
from pydub.playback import play #(pip install pyaudio)
import sys
from CGenre import Genre

def main():

    sound = "Single-Ladies.mp3"#AudioSegment.from_mp3("Single-Ladies.mp3")
    genre = Genre(sound)
    print(genre.loud())
    
    """
    # get the frame rate
    sample_rate = sound.frame_rate

    # get amount of bytes contained in one sample
    sample_size = sound.sample_width

    # get channels
    channels = sound.channels
    #print(channels)

    #play(sound)
    """

if __name__ == "__main__":
    main()