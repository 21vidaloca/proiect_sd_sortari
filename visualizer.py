import json
import matplotlib.pyplot as plt
import numpy as np
import os

class Visualizer:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            self.data = json.load(f)

    def plot_averages(self, save_folder='./plots_avg'):
        os.makedirs(save_folder, exist_ok=True)

        for title, tests in self.data.items():
            sort_times = {}

            # Collect all times
            for test_no, sortings in tests.items():
                for sort_name, time in sortings.items():
                    if sort_name not in sort_times:
                        sort_times[sort_name] = []
                    sort_times[sort_name].append(time)

            # Compute averages
            avg_times = {sort_name: np.mean(times) for sort_name, times in sort_times.items()}

            # Sort by average time (fastest first)
            sorted_avg_times = dict(sorted(avg_times.items(), key=lambda item: item[1]))

            sort_names = list(sorted_avg_times.keys())
            times = list(sorted_avg_times.values())

            # Plot
            plt.figure(figsize=(14, 8))
            plt.bar(sort_names, times, color='skyblue')
            plt.ylabel('Average Time (seconds)')
            plt.title(f'Average Sorting Times - {title}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            # Save as PNG
            filename = os.path.join(save_folder, f'{title[7:]}_average.png')
            plt.savefig(filename)
            plt.close()

if __name__ == '__main__':
    vis = Visualizer('results/data.json')
    vis.plot_averages('./results')