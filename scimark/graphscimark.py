import os
import re
import matplotlib.pyplot as plt

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
        lines = file.readlines()
        composite_score = None
        
        for line in lines:
            if line.startswith('Composite Score:'):
                composite_score = extract_values(line)[0]
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

# Plotting
x_ticks = [i + 1 for i in range(len(result_files))]

plt.figure(figsize=(10, 6))

# Plotting task scores
for task, scores in task_scores.items():
    task_data = [scores.get(filename, 0) for filename in result_files]
    plt.plot(x_ticks, task_data, marker='o', label=task)

# Plotting composite scores
composite_data = [composite_scores[filename] for filename in result_files]
plt.plot(x_ticks, composite_data, marker='o', label='Composite Score', linewidth=2, linestyle='dashed')

plt.xticks(x_ticks, result_files, rotation=45)
plt.xlabel('Machines')
plt.ylabel('Scores')
plt.title('SciMark Benchmark Results')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
