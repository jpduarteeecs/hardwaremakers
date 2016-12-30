#https://github.com/jiaaro/pydub
from pydub import AudioSegment
from pydub.playback import play
from time import sleep

path = "/home/juan/research/hardwaremakers/python-board/sound/"
#fname = "/home/juan/Downloads/Angklung.mp3"
#Mina Azhar (Juan's wife) did all the mp3 conversion, thank you!
fname = path+"low_do_long.mp3"
dol = AudioSegment.from_mp3(fname)
fname = path+"re_long.mp3"
re = AudioSegment.from_mp3(fname)
fname = path+"mi_long.mp3"
mi = AudioSegment.from_mp3(fname)
fname = path+"fa_long.mp3"
fa = AudioSegment.from_mp3(fname)
fname = path+"so_long.mp3"
so = AudioSegment.from_mp3(fname)
fname = path+"la_long.mp3"
la = AudioSegment.from_mp3(fname)
fname = path+"si_long.mp3"
si = AudioSegment.from_mp3(fname)
fname = path+"high_do_long.mp3"
doh = AudioSegment.from_mp3(fname)
#play(do+re+mi+mi+mi+fa)
#print(do.duration_seconds)
#play(dol+re+mi+fa+so+la+si+doh)
print(re.duration_seconds)
play(dol+re[:int(re.duration_seconds*1000/3)]+mi+dol[:int(dol.duration_seconds*1000/3)]+mi[:int(dol.duration_seconds*1000/2)]+dol[:int(dol.duration_seconds*1000/2)]+mi)
#dol+a+deer,+a+female+deer+
sleep(.3)
play(re+mi[:int(mi.duration_seconds*1000/3)]+fa[:int(fa.duration_seconds*1000/3)]+fa[:int(fa.duration_seconds*1000/3)]+mi[:int(mi.duration_seconds*1000/3)]+re[:int(re.duration_seconds*1000/3)]+fa)
#re+a+drop+of+golden+sun+
'''play(mi+fa+so+mi+so+mi+so)
#me+a+name+i+call+myself+
play(fa+so+la+la+so+fa+la)
#fa,+a+long+long+way+to+run+
play(so+dol+re+mi+fa+so+la)
#sew,+a+needle+pulling+thread+
play(la+re+mi+fa+so+la+si)
#la,+a+note+to+follow+sol+
play(si+mi+fa+so+la+si+doh)
#ti,+a+drink+with+jam+and+bread+
play(si+la+la+fa+si+so+doh+so+mi+re)
#and+that+brings+us+back+to+dol.
'''
