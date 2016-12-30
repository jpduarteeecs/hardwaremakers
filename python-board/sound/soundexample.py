#https://github.com/jiaaro/pydub
from pydub import AudioSegment
from pydub.playback import play

#fname = "/home/juan/Downloads/Angklung.mp3"

fname = "/home/juan/research/hardwaremakers/python-board/sound/do_open.mp3"
do = AudioSegment.from_mp3(fname)
fname = "/home/juan/research/hardwaremakers/python-board/sound/re.mp3"
re = AudioSegment.from_mp3(fname)
fname = "/home/juan/research/hardwaremakers/python-board/sound/mi.mp3"
mi = AudioSegment.from_mp3(fname)
fname = "/home/juan/research/hardwaremakers/python-board/sound/fa.mp3"
fa = AudioSegment.from_mp3(fname)

#play(do+re+mi+mi+mi+fa)
#print(do.duration_seconds)
play(do+do+do+do+re+re+do+do+fa+fa+mi+mi)
play(do+do+do+do+re+re+do+do+fa+fa+mi+mi)
