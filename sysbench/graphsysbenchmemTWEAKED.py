import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['vanilla chroot','tweaked chroot', 'vanilla KVM', 'tweaked KVM']

# Benchmarks
benchmarks = [
    'Write (1)',
    'Write (2)', 
    'Write (4)', 
    'Write (8)',
    'Read (1)',
    'Read (2)',
    'Read (4)',
    'Read (8)'
]

# Data for each machine's benchmark scores
data = {
    'vanilla chroot': [
        4833088.4785, 5475926.4165, 8126509.9272, 12625897.0088,
        5040339.0421, 7567328.1383, 11215545.2468, 12092702.2461
    ],
    'tweaked chroot': [
        5101349.92,
        6158750.82,
        9094981.78,
        12776065.07,
        5295092.01,
        8274660.66,
        12225895.60,
        12437416.15
    ],
    'vanilla KVM': [
        4896290.2110,
        5504727.2887,
        8128455.5561,
        12673959.3570,
        4406112.6820,
        6580500.2812,
        10120932.8930,
        12377014.1382
    ],
    'tweaked KVM': [
        4536083.05,
        6040116.73,
        8940503.33,
        13183078.13,
        4634644.92,
        7158300.15,
        10752340.69,
        12578977.69
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
plt.title('Normalized Sysbench Memory Events per Second')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
