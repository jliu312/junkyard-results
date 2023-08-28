import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['t4g2XLarge','t4gXLarge', 't4gLarge', 'KVM', 'Chroot', 'Native']

# Benchmarks
benchmarks = [
    '1',
    '2',
    '4',
    '8'
]

# Data for each machine's benchmark scores
data = {
    't4g2XLarge':[
        2628.46, 5675.79, 11355.45, 22713.90
    ],
    't4gXLarge': [
        2814.00, 5673.93, 11348.83, 11357.16
    ],
    't4gLarge': [
        2843.95, 5653.88, 5674.17, 5661.93
    ],
    'KVM': [
        3196.08, 6412.48, 11451.42, 14908.06
    ],
    'Chroot': [
        1830.28, 3680.05, 8744.08, 12222.20
    ],
    'Native': [
         3247.94, 6486.73, 11570.89, 15074.82
    ]
}

# Normalize data relative to t4gLarge
t4gLarge_scores = data['t4g2XLarge']
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

plt.axhline(y=1, color='black', linestyle='--', label='t4g2XLarge', linewidth=2)  # Horizontal line at y=1
plt.xticks(x_indices + (len(machines) / 2) * bar_width + p, benchmarks, ha='right')
plt.ylabel('Normalized Scores')
plt.xlabel('# Threads')
plt.title('Normalized Sysbench CPU Events per Second')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
