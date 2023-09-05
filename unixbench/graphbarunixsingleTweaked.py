import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['vanilla chroot','tweaked chroot', 'vanilla KVM', 'tweaked KVM']

# Benchmarks
benchmarks = [
    'Dhrystone 2 using register variables',
    'Double-Precision Whetstone',
    'Execl Throughput',
    'File Copy 1024 bufsize 2000 maxblocks',
    'File Copy 256 bufsize 500 maxblocks',
    'File Copy 4096 bufsize 8000 maxblocks',
    'Pipe Throughput',
    'Pipe-based Context Switching',
    'Process Creation',
    'Shell Scripts (1 concurrent)',
    'Shell Scripts (8 concurrent)',
    'System Call Overhead',
    'System Benchmarks Index Score'
]

# Data for each machine's benchmark scores
data = {
    'vanilla chroot': [
        5009.1, 1505.1, 1253.3, 2561.5, 1795.8, 2970.0,
        1449.2, 243.1, 100.2, 715.0, 5803.5, 1179.0, 1295.3
    ],
    'tweaked chroot': [
        5051.8,
        1495.9,
        1195.9,
        2262.5,
        1463.6,
        3851.5,
        1673.0,
        293.2,
        533.1,
        1935.8,
        5758.1,
        1155.6,
        1643.4
    ],
    'vanilla KVM': [
        5040.7, 1497.0, 1192.6, 2323.7, 1516.0, 4022.8,
        1653.4, 286.3, 524.9, 1062.4, 6220.0, 1133.4, 1577.4
    ],
    'tweaked KVM': [
        5051.8,
        1495.9,
        1195.9,
        2262.5,
        1463.6,
        3851.5,
        1673.0,
        293.2,
        533.1,
        1935.8,
        5758.1,
        1155.6,
        1643.4
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
for idx, machine in enumerate(machines):
    normalized_scores = normalized_data[machine]
    if "chroot" in machine:
        p = -0.05
    else:
        p = 0.05
    plt.bar(x_indices + idx * (bar_width) + p, normalized_scores, bar_width, color=colors[idx], label=machine)

# plt.axhline(y=1, color='black', linestyle='--', label='Chroot', linewidth=2)  # Horizontal line at y=1
plt.xticks(x_indices + (len(machines) / 2) * bar_width + p - 0.11, benchmarks, rotation=45, ha='right')
plt.ylabel('Normalized Scores (Arbitrarily using Vanilla Chroot as the Baseline)')
plt.xlabel('Benchmarks')
plt.title('Normalized UnixBench Scores for Different Machines, Running 1 copy of tests')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
