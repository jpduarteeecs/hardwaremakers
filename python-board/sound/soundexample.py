#https://github.com/jiaaro/pydub
from pydub import AudioSegment
from pydub.playback import play

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

play(si+mi+so+la+so+mi+si+la+so+la+si)#+I+took+my+baby+on+a+Saturday+bang+
play(si+si+mi+so+la+so+mi+si+la+so+la+si)#+Boy+is+that+girl+with+you?+Yes,+we’re+one+and+the+same+
play(si+si+do+do+mi+mi+fa+mi+mi)#+Now+I+believe+in+miracles+
play(mi+mi+do+do+mi+mi+fa+mi+fa+so)#+And+a+miracle+has+happened+tonight+
play(si+fa+fa+fa+fa+so+fa+mi)#+But,+if+you’re+thinkingabout+my+baby+
play(mi+mi+do+mi+mi+do+fa+mi+mi)#+It+don’t+matter+if+you’re+black+or+white+
play(si+mi+so+la+so+mi+si+la+so+la+si)#+They+print+my+message+in+the+Saturday+Sun+
play(si+si+mi+so+la+so+mi+si+la+so+la+si)#+I+had+to+tell+them+i+ain’t+second+to+none+
play(si+si+do+do+mi+mi+fa+mi+mi)#+And+I+told+about+equality+
'''mi+mi+do+do+mi+mi+fa+mi+fa+so)#+An+it’s+true,+either+you’re+wrong+or+you’re+right+
si+fa+fa+fa+fa+so+fa+mi)#+But,+if+you’re+thinkingabout+my+baby+
mi+mi+do+mi+mi+do+fa+mi+mi)#+It+don’t+matter+if+you’re+black+or+white+
do+do+mi+mi+fa+mi+mi)#+Don’t+tell+me+you+agree+with+me+
mi+mi+do+do+mi+mi+fa+mi+fa+so)#+When+I+saw+you+kicking+dirt+in+my+ey+
si+fa+fa+fa+fa+so+fa+mi)#+But,+if+you’re+thinkingabout+my+baby+
mi+mi+do+mi+mi+do+fa+mi+mi)#+It+don’t+matter+if+you’re+black+or+white+
si+fa+fa+fa+fa+so+fa+mi)#+But,+if+you’re+thinkingabout+my+baby+
mi+mi+do+mi+mi+do+fa+mi+mi)#+It+don’t+matter+if+you’re+black+or+white+
si+fa+fa+fa+fa+so+fa+mi)#+But,+if+you’re+thinkingabout+my+baby+
mi+mi+do+mi+mi+do+fa+mi+mi)#+It+don’t+matter+if+you’re+black+or+white'''
