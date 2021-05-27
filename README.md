# Dirt Rally 2.0 Logging

## Introduction
\
I am currently working on a way to export the game data from [Dirt Rally 2.0](https://dirtrally2.dirtgame.com/) via UDP so that people can use the race data log to import into a program like MegaLog Viewer

## Requirements
\
There are 2 ways to run this program. The first is using the executable file which does not require any setup. The second is using python itself. If the user wants to use python itself the install requirements are below. Otherwise there are no setup requirements!

This program requires Python 3.7+ in order to run. As such it will require the following modules (some of which come with the install).

- socket - Used to read from the UDP socket in the game
- struct - Used to decode the binary string the game exports
- tkinter (tk) - Used for the front end logging window
- threading - Used to keep the tkinter window open and still allow logging
- os - Used to put the logs inside of a 'Logs' folder

To enable logging inside of Dirt you will need to follow the steps below. I followed [this](https://motionsystems.eu/2020/03/dirt-udp-proxy-fana-leds-2/) guide to figure out what needed to be done. 

1) Go to Documents\My Games\DiRT Rally 2.0\hardwaresettings
2) Open hardware_settings_config.xml in notepad
3) Under the <motion_platform> XML section change:\
 **&lt;udp enabled="false" extradata="1" ip="127.0.0.1" port="20777" delay="1" /&gt;**\
 to:\
 **&lt;udp enabled="true" extradata="3" ip="127.0.0.1" port="20777" delay="1" /&gt;**
 \
 <img src="lib/img.jpeg">

 ## Usage

 To use this program is very simple. Simply open Dirt Rally 2.0 and run logging.exe in this folder.

 ### Start
 - The start command runs the logging file. When pressed it creates the file in the input field and eports the game to it. ***WARNING: THIS WILL OVERWRITE EXISTING DATA IN THAT FILE***

 ### Stop
 - The stop command will stop the program from logging and save the data to an excel file. ***WARNING: CLOSING THE LOGGING WINDOW WITHOUT STOPPING THE LOG COULD CAUSE DATA TO BE LOST***

 ### Filename
 - The filename input field is so that the user can input a logging file to be used. This file will be created as a CSV file where the columns are the data catagories the game is outputting and the rows are exports from the game. This filename can be anything you want but will always export a comma seperated text document.