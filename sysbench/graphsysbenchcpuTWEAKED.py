import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['vanilla chroot','tweaked chroot', 'vanilla KVM', 'tweaked KVM']

# Benchmarks
benchmarks = [
    '1', '2', '4', '8'
]

# Data for each machine's benchmark scores
data = {
    'vanilla chroot': [
        1830.28, 3680.05, 8744.08, 12222.20
    ],
    'tweaked chroot': [
        3192.1393, 6484.0204, 11576.3880, 15062.7579
    ],
    'vanilla KVM': [
        3196.08, 6412.48, 11451.42, 14908.06
    ],
    'tweaked KVM': [
        3212.2673, 6434.0505, 11527.9900, 15071.6060
    ]

}

# Normalize data relative to t4gLarge
t4gLarge_scores = data['vanilla chroot']
normalized_data = {machine: [score / t4gLarge for score, t4gLarge in zip(scores, t4gLarge_scores)]
                   for machine, scores in data.items()}

# Set up colors for each machine
colors = plt.cm.rainbow(np.linspace(0, 1, len(machines)))

# Create a bar graph
plt.figure(figsize=(10, 6))

bar_width = 0.15  # Width of each bar
x_indices = np.arange(len(benchmarks))

p = np.linspace(0, 2, len(x_indices))
p = 0
for idx, machine in enumerate(machines):
    normalized_scores = normalized_data[machine]
    if "chroot" in machine:
        p = -0.05
    else:
        p = 0.05
    plt.bar(x_indices + idx * (bar_width) + p, normalized_scores, bar_width, color=colors[idx], label=machine)

# plt.axhline(y=1, color='black', linestyle='--', label='t4g2XLarge', linewidth=2)  # Horizontal line at y=1
plt.xticks(x_indices + (len(machines) / 2) * bar_width - 0.075, benchmarks)
plt.ylabel('Normalized Scores')
plt.xlabel('Operation (# Threads)')
plt.title('Normalized Sysbench CPU Events per Second')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
