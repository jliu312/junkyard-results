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
        16533.5, 7674.0, 3429.8, 7060.2, 5420.0, 9194.5, 
        5279.4, 535.4, 1734.6, 7446.7, 6226.4, 4818.4, 4846.0       
    ],
    'tweaked chroot': [
        14963.8,
        6668.4,
        2544.4,
        5652.9,
        4819.6,
        8477.4,
        4389.4,
        531.0,
        1405.5,
        6361.9,
        6024.3,
        4789.1,
        4255.4
    ],
    'vanilla KVM': [
        15420.4, 7201.2, 3551.7, 6834.5, 5113.0, 10719.7, 6009.4, 
        3124.3, 1660.9, 6943.8, 6473.1, 4943.3, 5634.4       
    ],
    'tweaked KVM': [
       14622.6,
        6629.0,
        3280.3,
        5246.4,
        4845.4,
        9781.2,
        5211.2,
        2921.9,
        1478.6,
        5619.6,
        5977.1,
        4660.6,
        5055.4
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
plt.xticks(x_indices + (len(machines) / 2) * bar_width + p - 0.1, benchmarks, rotation=45, ha='right')
plt.ylabel('Normalized Scores (Arbitrarily using Vanilla Chroot as the Baseline)')
plt.xlabel('Benchmarks')
plt.title('Normalized UnixBench Scores for Different Machines, Running 8 copy of tests')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
