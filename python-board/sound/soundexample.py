#https://github.com/jiaaro/pydub
from pydub import AudioSegment
from pydub.playback import play

fname = "/home/juan/Downloads/Angklung.mp3"
mysong = AudioSegment.from_mp3(fname)
play(mysong)
