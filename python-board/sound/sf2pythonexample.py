#https://pypi.python.org/pypi/sf2utils/
fname = "/home/juan/research/hardwaremakers/python-board/sound/Arumba-1.0.sf2"
from sf2utils.sf2parse import Sf2File
with open(fname, 'rb') as sf2_file:
    sf2 = Sf2File(sf2_file)
print(sf2.raw.info)
print(sf2.raw.pdta)
