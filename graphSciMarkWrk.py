import matplotlib.pyplot as plt
import numpy as np

# Data for t4g.Large AWS Instance
labels = ['Dhrystone (integer ops)', 'Whetstone (floating ops)', 'File Copy 1024', 'File Copy 256', 'Pipe Throughput', 'Process Creation']
values_t4g_large = [3394.1, 1307.2, 1925.3, 1366.9, 1063.3, 332.6]

# Data for t4g.xLarge AWS Instance
values_t4g_xlarge = [13532.4, 5239.8, 7867.5, 5928.4, 4282.9, 1350.7]

# Data for ChrootonAndroid
values_chroot_android = [5009.1, 1505.1, 2561.5, 1795.8, 1449.2, 100.2]

x = np.arange(len(labels))

# Create subplots
fig, axs = plt.subplots(1, 1, figsize=(10, 15))

# Plot for t4g.Large AWS Instance
axs.bar(x - 0.3, values_t4g_large, width=0.3, label='t4g.Large AWS Instance', color='blue')
axs.set_xticks(x)
axs.set_xticklabels(labels)
axs.set_ylabel('Index Score')
axs.set_title('Performance Comparison: t4g.Large AWS Instance')

# Plot for t4g.xLarge AWS Instance
axs.bar(x, values_t4g_xlarge, width=0.3, label='t4g.xLarge AWS Instance', color='green')
axs.set_xticks(x)
axs.set_xticklabels(labels)
axs.set_ylabel('Index Score')
axs.set_title('Performance Comparison: t4g.xLarge AWS Instance')

# Plot for ChrootonAndroid
axs.bar(x + 0.3, values_chroot_android, width=0.3, label='ChrootonAndroid', color='orange')
axs.set_xticks(x)
axs.set_xticklabels(labels)
axs.set_ylabel('Index Score')
axs.set_title('Performance Comparison: ChrootonAndroid')

# Adjust layout
plt.tight_layout()

plt.legend()

# Display the plots
plt.show()

