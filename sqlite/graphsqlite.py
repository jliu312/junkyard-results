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
        108.28, 174.49, 241.77, 316.74
    ],
    'tweaked chroot': [
        39.56, 61.47, 74.71, 105.81
    ],
    'vanilla KVM': [
        182.83, 218.59, 278.34, 214.85
    ],
    'tweaked KVM': [
        18.13, 28.07, 39.74, 56.02
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

p = np.linspace(0, 0, len(x_indices))
for idx, machine in enumerate(machines):
    normalized_scores = data[machine]
    if "chroot" in machine:
        p = -0.03
    else:
        p = 0.03
    plt.bar(x_indices + idx * (bar_width) + p, normalized_scores, bar_width, color=colors[idx], label=machine)



# plt.axhline(y=1, color='black', linestyle='--', label='Chroot', linewidth=2)  # Horizontal line at y=1
plt.xticks(x_indices + (len(machines) / 2) * bar_width - 0.075, benchmarks)
plt.ylabel('Seconds (Fewer is better)')
plt.xlabel('Threads/Copies')
plt.title('SQLite benchmark before/after Tweaking Settings')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
