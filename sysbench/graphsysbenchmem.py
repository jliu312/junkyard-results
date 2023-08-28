import matplotlib.pyplot as plt
import numpy as np

# Machines
machines = ['t4g2XLarge','t4gXLarge', 't4gLarge', 'KVM', 'Chroot', 'Native']

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
    't4g2XLarge':[
        4592741.1740,
        3304478.1614,
        5607931.4569,
        8885675.7682,
        4101389.6700,
        5730649.9202,
        9431606.0500,
        10637436.8559
    ],
    't4gXLarge': [
        4570202.3138,
        2862001.9019,
        5130898.3872,
        4959698.3500,
        4756087.0837,
        5870828.0962,
        8565950.8836,
        8479111.4630
    ],
    't4gLarge': [
        4602365.0850,
        3221854.5751,
        3151927.6525,
        3287083.1099,
        4770324.3684,
        5507667.2390,
        5671954.3482,
        5960201.4899
    ],
    'KVM': [
        4896290.2110,
        5504727.2887,
        8128455.5561,
        12673959.3570,
        4406112.6820,
        6580500.2812,
        10120932.8930,
        12377014.1382
    ],
    'Chroot': [
        4833088.4785, 5475926.4165, 8126509.9272, 12625897.0088,
        5040339.0421, 7567328.1383, 11215545.2468, 12092702.2461
    ],
    'Native': [
        4896290.2110,
        5504727.2887,
        8128455.5561,
        12673959.3570, 
        5070643.6782,
        7656178.1575,
        11216523.3843,
        12095219.3927
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
plt.xlabel('Operation (# Threads)')
plt.title('Normalized Sysbench Memory Events per Second')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the graph
plt.show()
