import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['t4g2XLarge','t4gXLarge', 't4gLarge', 'KVM', 'Chroot', 'Native']

# Benchmarks
benchmarks = [
    '1',
    '2',
    '4',
    '8',
    '16'
]

# Data for each machine's benchmark scores
data = {
    't4g2XLarge':[4.1681, 7.9693, 15.8541, 30.5604, 30.4858],
    't4gXLarge': [4.1699, 7.7449, 15.6006, 15.6338, 15.8766],
    't4gLarge': [4.1638, 7.9925, 7.9712, 8.0316, 8.0395],
    'KVM': [3.1760, 7.5573, 14.8247, 18.6494, 19.1093, 20.9710],
    'Chroot': [3.5267, 8.7190, 15.2858, 18.4195, 21.1589],
    'Native': [5.2044, 10.4775, 13.8727, 18.4428, 21.9376]
}

# Normalize data relative to t4gLarge
t4gLarge_scores = data['t4gXLarge']
normalized_data = {machine: [score / t4gLarge for score, t4gLarge in zip(scores, t4gLarge_scores)]
                   for machine, scores in data.items()}

# Set up colors for each machine
colors = plt.cm.rainbow(np.linspace(0, 1, len(machines)))

# Create a bar graph
plt.figure(figsize=(10, 6))

bar_width = 0.15  # Width of each bar
x_indices = np.arange(len(benchmarks))

p = np.linspace(0, 2, len(x_indices))
for idx, machine in enumerate(machines):
    normalized_scores = normalized_data[machine]
    plt.bar(x_indices + idx * (bar_width) + p, normalized_scores, bar_width, color=colors[idx], label=machine)

plt.axhline(y=1, color='black', linestyle='--', label='t4gXLarge', linewidth=2)  # Horizontal line at y=1
plt.xticks(x_indices + (len(machines) / 2) * bar_width + p, benchmarks, ha='right')
plt.ylabel('Normalized Scores')
plt.xlabel('# Threads')
plt.title('Normalized Sysbench Mutex Throughput Events per Second')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
