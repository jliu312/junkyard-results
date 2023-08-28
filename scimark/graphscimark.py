import os
import re
import matplotlib.pyplot as plt
import numpy as np

# Function to extract values from the SciMark result lines
def extract_values(line):
    return [float(x) for x in re.findall(r'[-+]?\d*\.\d+|\d+', line)]

# List of SciMark result files in the directory
result_files = [filename for filename in os.listdir('.') if filename.startswith('SciMark') and filename.endswith('.txt')]

# Initialize empty dictionaries to store data
composite_scores = {}
task_scores = {task: {} for task in ['FFT', 'SOR', 'Monte Carlo', 'Sparse matmult', 'LU']}

# Iterate through each result file
for filename in result_files:
    with open(filename, 'r') as file:
        # filename = filename[7:-4]
        lines = file.readlines()
        composite_score = None
        monte_score = None
        
        for line in lines:
            if line.startswith('Composite Score:'):
                composite_score = extract_values(line)[0]
            elif line.startswith('Monte Carlo'):
                task_scores["Monte Carlo"][filename] = extract_values(line)[0]
            else:
                for task in task_scores.keys():
                    if line.startswith(task):
                        values = extract_values(line)
                        if len(values) >= 2:
                            task_scores[task][filename] = values[1]
                            if len(values) >= 3:
                                task_scores[task][filename] = values[2]
        
        if composite_score is not None:
            composite_scores[filename] = composite_score
        


print("task_scores:" + str(task_scores))
print("composite_scores" + str(composite_scores))

for k, v in task_scores.items():
    # print(task)
    print("\n\n\nV:" + str(v))
    baseline = v['SciMarkt4gLarge.txt']

    # task = [v1 / baseline for k1, v1 in v.items()]
    for k1, v1 in v.items():
        task_scores[k][k1] /= baseline
    

print("task_scores:" + str(task_scores))
print("composite_scores" + str(composite_scores))

# print(type(task_scores))


sub_benchmarks = list(task_scores.keys())

# Create a list of machine names from the result_files list
machine_names = [filename.split('.')[0] for filename in result_files]

# Create a 2D array to store the scores for each machine and each sub-benchmark
scores_matrix = np.zeros((len(machine_names), len(sub_benchmarks)))

# Populate the scores_matrix with the extracted scores
for i, machine in enumerate(machine_names):
    for j, benchmark in enumerate(sub_benchmarks):
        scores_matrix[i, j] = task_scores[benchmark].get(machine + '.txt', 0)

# Plotting

x_ticks = np.arange(len(sub_benchmarks))  # Use sub-benchmarks as x-axis tick labels
bar_width = 0.12  # Width of each bar
offsets = np.arange(len(machine_names)) * bar_width  # Offset for clustered bars

colors = plt.cm.rainbow(np.linspace(0, 1, len(machine_names)))


plt.figure(figsize=(10, 6))

# Plotting task scores for each machine as clustered bars
for i, machine in enumerate(machine_names):
    plt.bar(x_ticks + offsets[i], scores_matrix[i, :], width=bar_width, label=machine[7:], color=colors[i])

plt.axhline(y=1, color='black', linestyle='--', label='t4gLarge', linewidth=2)
            
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xlabel('Sub-Benchmark')
plt.ylabel('Scores')
plt.title('SciMark Benchmark Scores')
plt.xticks(x_ticks + bar_width * (len(machine_names) - 1) / 2, sub_benchmarks)
plt.legend()
plt.tight_layout()

plt.show()