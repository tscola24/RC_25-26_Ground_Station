import csv
import random
import time
from pathlib import Path
import sys

csv_file_path_name = Path(Path.cwd(), 'data', 'data.csv')

print(f"Current Working Directory: {Path.cwd()}")
print(f"Target File Path: {csv_file_path_name}")

try: 
    csv_file_path_name.parent.mkdir(parents=True, exist_ok=True)
except Exception as err:
    print(err)
    sys.exit()

#Declare default vals
header_column_names = ['time','air_pressure', 'altitude','acceleration','payload_temp','rotation_rate', 'descent_rate']
time_ = 0
air_pressure = 30
altitude = 500
acceleration = 20
payload_temp = 20
rotation_rate = 6
descent_rate = -10


#Creates new csv file in the data folder
with open(csv_file_path_name, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=header_column_names)
    csv_writer.writeheader()

while True:

    with open(csv_file_path_name, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=header_column_names)

        info = {
            'time' : time_,
            'air_pressure' : air_pressure,
            'altitude' : altitude,
            'acceleration' : acceleration,
            'payload_temp' : payload_temp,
            'rotation_rate' : rotation_rate,
            'descent_rate' : descent_rate
        }
        # Adds new data to the csv file
        csv_writer.writerow(info)
        print(time_,air_pressure, altitude,acceleration,payload_temp,rotation_rate, descent_rate)

        
        time_ += 0.5
        air_pressure += random.randint(-1, 1)
        altitude += random.randint(3, 9)
        acceleration += random.randint(-3, 3)
        payload_temp += random.randint(-1, 1)
        rotation_rate += random.randint(-1, 1)
        descent_rate += random.randint(-3, 3)

    time.sleep(0.5)