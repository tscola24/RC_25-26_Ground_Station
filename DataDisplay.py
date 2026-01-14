import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from pathlib import Path

csv_file_path_name = Path(Path.cwd(), 'data', 'data.csv')

measures = ['air_pressure', 'altitude','acceleration','payload_temp','rotation_rate', 'descent_rate']
units = ['Hgin', 'ft', 'ft/s sqaured','degrees', 'rotations per second', 'ft/s']
n_rows = 2
n_columns = round((len(measures)/n_rows))

fig, axes = plt.subplots(nrows=n_rows, ncols=n_columns, figsize=(12,8))
fig.set_facecolor("#AAC2E7")

def updateDisplay(frame_number):
    try:
        data = pd.read_csv(csv_file_path_name)
    except Exception:
        return 
    if data.empty:
        return
    
    for i, measure in enumerate(measures):
        row = i // n_columns
        col = i % n_columns

        ax = axes[row][col]
        ax.cla()
        ax.plot(data['time'], data[measure], color='red', linewidth=2)

        ax.set_title(f'{measure}')
        ax.set_ylabel(f'{units[i]}')
        ax.set_xlabel('Time (seconds)')
        
    plt.tight_layout()


updatedDisplay = FuncAnimation(fig, updateDisplay, interval=500, cache_frame_data=False)

plt.show()