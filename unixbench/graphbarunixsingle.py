import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['t4g2XLarge','t4gXLarge', 't4gLarge', 'KVM', 'Chroot', 'Native']

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
        3234.8, 1307.4, 475.7, 1925.3, 1468.1, 3092.3, 
        1060.5, 105.0, 321.1, 1598.5, 7153.3, 609.1, 1131.0
    ],
    't4gXLarge': [
        3385.1, 1307.7, 483.6, 2002.5, 1505.4, 2925.8,
        1069.0, 108.7, 336.0, 1654.6, 4126.3, 610.1, 1098.0
    ],
    't4gLarge': [
        3394.1, 1307.2, 478.8, 1925.3, 1366.9, 2689.8,
        1063.3, 107.9, 332.6, 1502.2, 2201.6, 609.6, 1012.2
    ],
    'KVM': [
        5040.7, 1497.0, 1192.6, 2323.7, 1516.0, 4022.8,
        1653.4, 286.3, 524.9, 1062.4, 6220.0, 1133.4, 1577.4
    ],
    'Chroot': [
        5009.1, 1505.1, 1253.3, 2561.5, 1795.8, 2970.0,
        1449.2, 243.1, 100.2, 715.0, 5803.5, 1179.0, 1295.3
    ],
    'Native': [
        5047.6, 1502.8, 1135.6, 2408.1, 1610.7, 4082.3,
        1251.7, 315.8, 398.5, 2532.2, 6867.1, 864.2, 1618.4
    ]
}

# Normalize data relative to t4gLarge
t4gLarge_scores = data['t4gLarge']
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

plt.axhline(y=1, color='black', linestyle='--', label='t4gLarge', linewidth=2)  # Horizontal line at y=1
plt.xticks(x_indices + (len(machines) / 2) * bar_width + p, benchmarks, rotation=45, ha='right')
plt.ylabel('Normalized Scores')
plt.xlabel('Benchmarks')
plt.title('Normalized UnixBench Scores for Different Machines, Running 1 copy of tests')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
