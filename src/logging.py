import socket
import os
from struct import *
from tkinter import *
from tkinter.font import Font
import threading
import time
import sys

cols = [
    'total_time',
    'lap_time',
    'lap_distance',
    'total_distance',
    'position_x',
    'position_y',
    'position_z',
    'speed',
    'velocity_x',
    'velocity_y',
    'velocity_z',
    'left_dir_x',
    'left_dir_y',
    'left_dir_z',
    'forward_dir_x',
    'forward_dir_y',
    'forward_dir_z',
    'suspension_position_bl',
    'suspension_position_br',
    'suspension_position_fl',
    'suspension_position_fr',
    'suspension_velocity_bl',
    'suspension_velocity_br',
    'suspension_velocity_fl',
    'suspension_velocity_fr',
    'wheel_patch_speed_bl',
    'wheel_patch_speed_br',
    'wheel_patch_speed_fl',
    'wheel_patch_speed_fr',
    'throttle_input',
    'steering_input',
    'brake_input',
    'clutch_input',
    'gear',
    'gforce_lateral',
    'gforce_longitudinal',
    'lap',
    'engine_rate',
    'native_sli_support',
    'race_position',
    'fuel_in_tank',
    'race_sector',
    'sector_time_1',
    'sector_time_2',
    'brake_temp_bl',
    'brake_temp_br',
    'brake_temp_fl',
    'brake_temp_fr',
    'laps_completed',
    'total_laps',
    'track_length',
    'last_lap_time',
    'max_rpm',
    'idle_rpm',
    'max_gears'
]

def logging_thread():
    global running, input_field

    while True:
        if input_field.get() is not None and running:
            with open('Logs/' + input_field.get(), 'w') as f: 
                print('Starting Logs')

                for c in cols:
                    f.write(c + ',')

                f.write('\n')

                while running:
                    try:
                        d, a = s.recvfrom(1024)

                        data = unpack('66f', d)

                        for x in data:
                            f.write('{},'.format(x))

                        f.write('\n')
                    except:
                        continue

                print('Finishing Logs')

def start_button_cb():
    global running

    running = True

def stop_button_cb():
    global running

    running = False

ip = "127.0.0.1"
port = 20777
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0)

if not os.path.exists('Logs'):
    os.mkdir('Logs')

thread = threading.Thread(target=logging_thread)
thread.daemon = True

running = False

w = Tk()

start_button = Button(w, text='Start', command=start_button_cb, background='green', width=10, height=2, font=Font(family="Helvetica",size=36,weight="bold"))
start_button.grid(column=1, row=3, padx=10, pady=10)

stop_button = Button(w, text='Stop', command=stop_button_cb, background='red', width=10, height=2, font=Font(family="Helvetica",size=36,weight="bold"))
stop_button.grid(column=2, row=3, padx=10, pady=10)

input_label = Label(w, text='Filename: ', font=Font(family="Helvetica",size=36,weight="bold"))
input_label.grid(column=1, row=1, padx=10, pady=10)

str_var = StringVar()
str_var.set('logs.csv')
input_field = Entry(w, textvariable=str_var, width=17, font=Font(family="Helvetica",size=24,weight="bold"))
input_field.grid(column=2, row=1, padx=10, pady=10)

s.bind((ip, port))
thread.start()
mainloop()