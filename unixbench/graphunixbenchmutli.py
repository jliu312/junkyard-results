import matplotlib.pyplot as plt

# Data for each machine
machines = ['t4gXLarge (4)', 't4gLarge (2)',
             'KVM (8)', 'Chroot (8)', 'Native (8)']

index_values = {
    'Dhrystone 2 using register variables': [13532.4, 6768.0, 15420.4, 16533.5, 16052.0],
    'Double-Precision Whetstone': [5239.8, 2610.6, 7201.2, 7674.0, 7282.5],
    'Execl Throughput': [1683.9, 858.1, 3551.7, 3429.8, 3252.9],
    'File Copy 1024 bufsize 2000 maxblocks': [7867.5, 3743.0, 6834.5, 7060.2, 6866.8],
    'File Copy 256 bufsize 500 maxblocks': [5928.4, 2860.6, 5113.0, 5420.0, 5098.0],
    'File Copy 4096 bufsize 8000 maxblocks': [10485.9, 5273.0, 10719.7, 9194.5, 10335.9],
    'Pipe Throughput': [4282.9, 2123.8, 6009.4, 5279.4, 4731.5],
    'Pipe-based Context Switching': [1233.5, 703.4, 3124.3, 535.4, 905.8],
    'Process Creation': [1350.7, 726.5, 1660.9, 1734.6, 2025.1],
    'Shell Scripts (1 concurrent)': [4664.4, 2391.8, 6943.8, 7446.7, 7693.9],
    'Shell Scripts (8 concurrent)': [4494.2, 2267.0, 6473.1, 6226.4, 7120.6],
    'System Call Overhead': [2439.6, 1218.6, 4943.3, 4818.4, 4193.0],
    'System Benchmarks Index Score': [4080.5, 2068.6, 5634.4, 4846.0, 5048.8]
}


# Create the line graph
plt.figure(figsize=(10, 6))

for benchmark, values in index_values.items():
    if benchmark == 'System Benchmarks Index Score':
        plt.plot(machines, values, marker='o', label=benchmark,linestyle='dotted', linewidth=5, color = 'yellow')
    else:
        plt.plot(machines, values, marker='o', label=benchmark)

plt.xlabel('Machines (N)')
plt.ylabel('Index Values')
plt.title('UnixBench Index Values for Different Machines (Running N parallel copies of test on N CPUs)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
