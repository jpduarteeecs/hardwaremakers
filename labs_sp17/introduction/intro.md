# Introduction

This week we are going to make sure we are all set up in terms of software and hardware (at least with a prototype board) so we can go smoothly through the semester.

## Software needed

Although the focus of this course is on hardware, we will need to use a lot of software as well. There are several installations that we need to do so we can run them on our computers and use them to communicate with hardware as well.

### Installing IPython (Introduction from [EE16A](http://inst.eecs.berkeley.edu/~ee16a/fa15/installation.html))
IPython, together with the required packages for the course, can be installed as follows.

**Linux**

Download [linux installer](http://inst.eecs.berkeley.edu/~ee16a/fa15/install/linux_installer.sh). Open a terminal and change directory to the folder you have downloaded the installation script. Run the terminal command:

`bash linux_installer.sh && source ~/.bashrc`

This operation does not require admin privileges. After the script completes, restart the terminal. In the terminal, run the command

`conda update pip -y`

You can verify installation as described in validating installation.
OSX
Download osx installer. Open a terminal and change directory to the folder you have downloaded the installation script. Run the terminal command:
bash osx_installer.sh && source ~/.bash_profile
This operation does not require admin privileges. After the script completes, restart the terminal (be sure to quit the terminal, and not just hide). In the terminal, run the command
conda update pip -y
You can verify installation as described in validating installation.
What the Linux and OSX Installers do:
Create a directory for all EE16A files in ~/ee16a
Download and run the Anaconda installer
Install additional packages using the conda package manager
Install packages not available through conda using pip
Download and install PyAudio from source
Run the version check script to verify all packages were installed successfully.
NOTE: By default Anaconda is installed to the home directory of each user.
Windows
Download windows installer. Right click on the file windows_installer.bat and run it with admin privilages. Open the command line by searching cmdon your PC. In the command line, run
conda update pip -y
You can verify installation as described in validating installation.
What the Windows installer does:
Create a directory for all EE16A files in the C:\EE16A
Download the program unzip.exe to unzip files because you can't do that in a batch file.
Download a zip file with Anaconda, more scripts
Unzip the installation files and delete the zip archive and the unzip utility.
Run the anaconda setup to install in the default directory C:\Anaconda
Run a VB script to update environment variables because this also can't be done any other way in a batch file.
Update packages using conda
Install new packages using conda
Use pip to install packages not available via conda
Run the PyAudio installer
Validating Installation
Download and run the program check_version.py using Python 3 to verify that the proper versions of each of the packages below are installed:
Python- 3.4.3 64 bit (Anaconda)
Anaconda- 2.3.0
conda- 3.15.1
conda-env- 2.3.0
pip- 7.1.0
setuptools- 18.0.1
ipython- 3.2.1
ipython-notebook- 3.2.1
jinja2- 2.8
mistune- 0.7
tornado- 4.2.1
jsonschema- 2.4.0
pyqt- 4.10.4
matplotlib 1.4.3
numpy- 1.9.2
pyserial- 2.7
scipy- 0.16.0-np19
portaudio- 19
pyaudio- 0.2.8
pyrtlsdr- 0.2.0
