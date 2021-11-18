from enum import Enum
import socket
from struct import unpack

class DirtRally2Values():
    def __init__(self):
        self.values = {
            'total_time': 0,
            'lap_time': 1,
            'lap_distance': 2,
            'total_distance': 3,
            'position_x': 4,
            'position_y': 5,
            'position_z': 6,
            'speed': 7,
            'velocity_x': 8,
            'velocity_y': 9,
            'velocity_z': 10,
            'left_dir_x': 11,
            'left_dir_y': 12,
            'left_dir_z': 13,
            'forward_dir_x': 14,
            'forward_dir_y': 15,
            'forward_dir_z': 16,
            'suspension_position_bl': 17,
            'suspension_position_br': 18,
            'suspension_position_fl': 19,
            'suspension_position_fr': 20,
            'suspension_velocity_bl': 21,
            'suspension_velocity_br': 22,
            'suspension_velocity_fl': 23,
            'suspension_velocity_fr': 24,
            'wheel_patch_speed_bl': 25,
            'wheel_patch_speed_br': 26,
            'wheel_patch_speed_fl': 27,
            'wheel_patch_speed_fr': 28,
            'throttle_input': 29,
            'steering_input': 30,
            'brake_input': 31,
            'clutch_input': 32,
            'gear': 33,
            'gforce_lateral': 34,
            'gforce_longitudinal': 35,
            'lap': 36,
            'engine_rate': 37,
            'native_sli_support': 38,
            'race_position': 39,
            'fuel_in_tank': 40,
            'race_sector': 41,
            'sector_time_1': 42,
            'sector_time_2': 43,
            'brake_temp_bl': 44,
            'brake_temp_br': 45,
            'brake_temp_fl': 46,
            'brake_temp_fr': 47,
            'laps_completed': 48,
            'total_laps': 49,
            'track_length': 50,
            'last_lap_time': 51,
            'max_rpm': 52,
            'idle_rpm': 53,
            'max_gears': 54
        }

    def get(self, v):
        return self.values[v]

class DirtRally2Decoder():
    def __init__(self, extradata):
        self.extradata = extradata
        self.DV = DirtRally2Values()

    def open_game(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.settimeout(2.0)
        self.s.bind((self.ip, int(self.port)))

    def close_game(self):
        self.s.close()

    def sample_game(self, values):
        try:
            d, a = self.s.recvfrom(1024)
            data = unpack('66f', d)
            ret = {}
            for v in values:
                ret[v] = data[self.DV.get(v)]

            return ret
        except socket.timeout:
            return None


    