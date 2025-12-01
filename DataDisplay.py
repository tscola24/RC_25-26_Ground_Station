import matplotlib.pyplot as plt
import pandas as pd
import random 

measures = ['air_pressure', 'altitude','acceleration','payload_temp','rotation_rate', 'descent_rate']
units = ['psi', 'ft', 'ft/s sqaured','degrees', 'rotations per second', 'ft/s']
random_ints = []
for i in range(0,18):
    random_ints.append(random.randint(0,100))

data_dict = {
    'air_pressure' : random_ints[0:3],
    'altitude' : random_ints[3:6],
    'acceleration' : random_ints[6:9],
    'payload_temp' : random_ints[9:12],
    'rotation_rate' : random_ints[12:15],
    'descent_rate' : random_ints[15:18],
    'time' : [0,1,2]
}

data = pd.DataFrame(data_dict)

n_rows = 2
n_columns = round((len(measures)/n_rows))

fig, axes = plt.subplots(nrows=n_rows, ncols=n_columns, figsize=(12,8))
fig.set_facecolor("#AAC2E7")

for i, measure in enumerate(measures):
    row = i // (n_rows+1)
    col = i % n_columns

    ax = axes[row][col]
    ax.plot(data['time'], data[measure], color='red', linewidth=2)

    ax.set_title(f'{measure}')
    ax.set_ylabel(f'{units[i]}')
    ax.set_xlabel('Time (seconds)')
    ax.title.set_color('black')

plt.tight_layout()
plt.show()