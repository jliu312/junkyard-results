import matplotlib.pyplot as plt

# Data for each machine
machines = ['t4gXLarge', 't4gLarge', 'KVM', 'Chroot', 'Native']

index_values = {
    'Dhrystone 2 using register variables': [3385.1, 3394.1, 5040.7, 5009.1, 5047.6],
    'Double-Precision Whetstone': [1307.7, 1307.2, 1497.0, 1505.1, 1502.8],
    'Execl Throughput': [483.6, 478.8, 1192.6, 1253.3, 1135.6],
    'File Copy 1024 bufsize 2000 maxblocks': [2002.5, 1925.3, 2323.7, 2561.5, 2408.1],
    'File Copy 256 bufsize 500 maxblocks': [1505.4, 1366.9, 1516.0, 1795.8, 1610.7],
    'File Copy 4096 bufsize 8000 maxblocks': [2925.8, 2689.8, 4022.8, 2970.0, 4082.3],
    'Pipe Throughput': [1069.0, 1063.3, 1653.4, 1449.2, 1251.7],
    'Pipe-based Context Switching': [108.7, 107.9, 286.3, 243.1, 315.8],
    'Process Creation': [336.0, 332.6, 524.9, 100.2, 398.5],
    'Shell Scripts (1 concurrent)': [1654.6, 1502.2, 1062.4, 715.0, 2532.2],
    'Shell Scripts (8 concurrent)': [4126.3, 2201.6, 6220.0, 5803.5, 6867.1],
    'System Call Overhead': [610.1, 609.6, 1133.4, 1179.0, 864.2],
    'System Benchmarks Index Score': [1098.0, 1012.2, 1577.4, 1295.3, 1618.4]
}

# Create the line graph
plt.figure(figsize=(10, 6))

for benchmark, values in index_values.items():
    if benchmark == 'System Benchmarks Index Score':
        plt.plot(machines, values, marker='o', label=benchmark,linestyle='dotted', linewidth=5, color = 'yellow')
    else:
        plt.plot(machines, values, marker='o', label=benchmark)

plt.xlabel('Machines')
plt.ylabel('Index Values')
plt.title('UnixBench Index Values for Different Machines (Running 1 parallel copy of test)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
