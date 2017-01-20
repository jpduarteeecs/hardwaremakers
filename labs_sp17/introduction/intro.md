# Introduction

This week we are going to make sure we are all set up in terms of software and hardware (at least with a development board) so we can go smoothly through the semester. This would be (probably) the most stressful week, please be patient, we can do it!

Most of the softwares that are indicated to be downloaded and installed are suggestions. Feel free to use the software that you think is the best for you, and let us know why- then we can all learn from it.

## Redbear Duo

This semester we will use [Redbear Duo](https://github.com/redbear/Duo) development board as a reference. The Duo has a 32-bit ARM Cortex M3 microcontroller in addition to WiFi and Bluetooth (BLE) capabilities. You can use the development board of your preference; however, you may run into few problems. For example, if you use Arduino (which is a fantastic board as well), projects can quickly reach memory and computing limits. In addition, you may need additional modules for WiFi and BLE communication.  

The RedBear Duo supports several programming languages such as Arduino, C/C++, JavaScript and Python (JavaScript and Python support is in beta and we will not be using it at this moment).

### Firmware (DO NOT DO THIS, Juan will take care of it)

Once you get your new RedBear Duo, you must update your Duo to the latest system firmware (see a simple [video](https://www.youtube.com/watch?v=RnXmkdOco4w) about firmware). This step is a little tricky; indeed, it seems that the firmware update only works well from Linux (maybe on Windows as well, in Mac not at all). I will do this for you, so once you get your Redbear Duo board please contact me and bring it to me. I will do the rest. Anyway, these are some steps to update the firmware using Linux:

1.  Install [dfu](https://github.com/redbear/Duo/blob/master/docs/dfu-util_installation_guide.md) (This works well in Linux, do not forget to add sudo before using dfu, otherwise it does not work).
2.  Using git, clone from Github the entire folder from [Duo](https://github.com/redbear/Duo) or just download [firmware files](https://github.com/redbear/Duo/tree/master/firmware).
3. In the command line, go to each folder containing the files you want to update, then install them following these [intructions](https://github.com/redbear/Duo/blob/master/docs/firmware_deployment_guide.md). “Update System Firmware” should be enough, also WiFi “Update Wi-Fi Firmware”.

### Arduino IDE

You need to install the latest Arduino IDE version available at [https://www.arduino.cc/](https://www.arduino.cc/).

Once you have installed Arduino IDE, you need to install the corresponding board package before you can use it. This can be found at [Duo: Arduino Board Package Installation Guide](https://github.com/redbear/Duo/blob/master/docs/arduino_board_package_installation_guide.md).

### Run Examples

In the Arduino IDE, go to "Files", "Examples", "Redbear_Duo", "Basics" and then try Blink and RGB examples. Note that before loading a code, you need to select, in "Tools", RedBear Duo board, and then in "Tools" as well, select a serial port.

## Create github account

We will do a lot of file sharing (not just code!) during this semester. We will try to use github to share files and to be as organized as possible. Using your educational email (It is ok to use another email, but using a .edu, you can have private repositories) create a github account in this [link](https://github.com/). Once you are set with your github account, you can request a [github education plan](https://education.github.com/), this takes a while to get approved, better you do it soon.

If you are using Mac or Windows, you can download a [github desktop](https://desktop.github.com/) that will help you with the organization of files. Linux users only need to use line command. I strongly recommend you try to use Linux, for example an Ubuntu distribution, while dealing with hardware and prototyping boards. Linux is much more reliable and simpler.

## Text editor

Everyone is free to use any text editor; however, I recommend using [atom](https://atom.io/). It is open source and can be customized. You can install the package [script](https://atom.io/packages/script), which lets you run code directly in the text editor (check website for shortcut of your operating system). This will be handy for Windows users. Command line is fine for Linux users.

## Software needed

Although the focus of this course is on hardware, we will need to use a lot of software as well. There are several installations that we need on our computers to communicate with hardware.

### Installing IPython
You can install IPython following the same instructions as in [EE16A IPython installation](http://inst.eecs.berkeley.edu/~ee16a/fa15/installation.html).

### Python libraries
For some labs, we will need to use [serial communication](https://www.youtube.com/watch?v=JJZOTtwpAjA) to connect computers with hardware. In order to do this with Python, please install [pyserial](http://pyserial.readthedocs.io/en/latest/pyserial.html).

Another library that we will need is [pydub](https://github.com/jiaaro/pydub). Using this library we can play different sound formats in python and make some fun and simple [projects](https://www.youtube.com/watch?v=dPkmSmyyr30) with it. Please be aware that pydub has some dependences, you will need [ffmpeg](http://www.ffmpeg.org/) (for Mac use `brew install ffpmeg —with-ffplay`) or libav. In addition, you may need to install [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/).

To test pyserial, upload the code [serialexample.io](https://github.com/jpduarteeecs/hardwaremakers/blob/master/python-board/serialexample/serialexample.ino) to your RedBear Duo, and then run the python code [serialexamplepython.py](https://github.com/jpduarteeecs/hardwaremakers/blob/master/python-board/serialexamplepython.py) from your atom editor. Remember to update the serial port address, it is the same as the one used in the Arduino IDE.

To test the sound, run the python code [soundexample](https://github.com/jpduarteeecs/hardwaremakers/blob/master/python-board/sound/soundexample.py), make sure to change the path to your own computer path.
