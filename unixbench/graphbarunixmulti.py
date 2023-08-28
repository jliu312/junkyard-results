import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['t4g2XLarge', 'KVM', 'Chroot', 'Native']

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
    't4g2XLarge':[
        25800.7, 10458.5, 3145.4, 15394.7, 11448.7, 24123.9, 
        8477.6, 2442.9, 2548.6, 8704.8, 8437.9, 4877.3, 7995.3
    ],
    'KVM': [
        15420.4, 7201.2, 3551.7, 6834.5, 5113.0, 10719.7, 6009.4, 
        3124.3, 1660.9, 6943.8, 6473.1, 4943.3, 5634.4
    ],
    'Chroot': [
        16533.5, 7674.0, 3429.8, 7060.2, 5420.0, 9194.5, 
        5279.4, 535.4, 1734.6, 7446.7, 6226.4, 4818.4, 4846.0
    ],
    'Native': [
        16052.0, 7282.5, 3252.9, 6866.8, 5098.0, 10335.9, 
        4731.5, 905.8, 2025.1, 7693.9, 7120.6, 4193.0, 5048.8
    ]
}

# Normalize data relative to t4gLarge
t4g2XLarge_scores = data['t4g2XLarge']
normalized_data = {machine: [score / t4g2XLarge for score, t4g2XLarge in zip(scores, t4g2XLarge_scores)]
                   for machine, scores in data.items()}

# Set up colors for each machine
colors = plt.cm.rainbow(np.linspace(0, 1, len(machines)))

# Create a bar graph
plt.figure(figsize=(10, 6))

bar_width = 0.15  # Width of each bar
x_indices = np.arange(len(benchmarks))

for idx, machine in enumerate(machines):
    normalized_scores = normalized_data[machine]
    plt.bar(x_indices + idx * bar_width, normalized_scores, bar_width, color=colors[idx], label=machine)

plt.axhline(y=1, color='black', linestyle='--', label='t4g2XLarge', linewidth=2)  # Horizontal line at y=1
plt.xticks(x_indices + (len(machines) / 2) * bar_width, benchmarks, rotation=45, ha='right')
plt.ylabel('Normalized Scores')
plt.xlabel('Benchmarks')
plt.title('Normalized UnixBench Scores for Different Machines, Running 8 Parallel Tests for 8')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
