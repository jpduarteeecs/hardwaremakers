#Juan Duarte
#Reference
#https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
import tkinter as tk
import time

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.clock = tk.Label(self, text="")
        self.clock.pack()

        # start the clock "ticking"
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S" , time.gmtime())
        self.clock.configure(text=now)
        # call this function again in one second
        self.after(1000, self.update_clock)

if __name__== "__main__":
    app = SampleApp()
    app.mainloop()


'''import tkinter as tk
from PIL import ImageTk, Image

home_dir = "/home/juan/research"
path = home_dir+"/hardwaremakers/labs_sp17/pressuresensor/png/2_of_clubs.png"
path2 = home_dir+"/hardwaremakers/labs_sp17/pressuresensor/png/3_of_clubs.png"


root = tk.Tk()

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

def callback(e):
    img2 = ImageTk.PhotoImage(Image.open(path2))
    panel.configure(image = img2)
    panel.image = img2

root.bind("<Return>", callback)
root.mainloop()'''

#This creates the main window of an application
'''window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

home_dir = "/home/juan/research"
path = home_dir+"/hardwaremakers/labs_sp17/pressuresensor/png/2_of_clubs.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()'''
