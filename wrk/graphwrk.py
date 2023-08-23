import os
import re
import matplotlib.pyplot as plt

# Get a list of result file names
result_files = [filename for filename in os.listdir('.') if filename.startswith('wrk') and filename.endswith('.txt')]

# Initialize dictionaries to store parsed data
latency_data = {}
req_per_sec_data = {}
transfer_per_sec_data = {}  # Added for Transfer/sec data

# Regular expressions to extract relevant data
latency_pattern = r'Latency\s+([\d.]+)ms'
req_per_sec_pattern = r'Req/Sec\s+([\d.]+)'
transfer_per_sec_pattern = r'Transfer/sec:\s+([\d.]+[KMGT]?B)'

# Loop through each result file
for filename in result_files:
    machine_name = filename.split('.')[0]  # Extract machine name from filename
    with open(filename, 'r') as file:
        content = file.read()

        # Extract latency data
        latency_match = re.search(latency_pattern, content)
        if latency_match:
            latency = float(latency_match.group(1))
            latency_data[machine_name] = latency

        # Extract requests per second data
        req_per_sec_match = re.search(req_per_sec_pattern, content)
        if req_per_sec_match:
            req_per_sec = float(req_per_sec_match.group(1))
            req_per_sec_data[machine_name] = req_per_sec

        # Extract Transfer/sec data
        transfer_per_sec_match = re.search(transfer_per_sec_pattern, content)
        if transfer_per_sec_match:
            transfer_per_sec = transfer_per_sec_match.group(1)
            transfer_per_sec_data[machine_name] = transfer_per_sec
            print(f"Debug: Parsed Transfer/sec for {machine_name}: {transfer_per_sec}")  # Debug statement

# Create graphs
plt.figure(figsize=(10, 9))  # Adjusted figure size for the additional graph

# Latency graph
plt.subplot(3, 1, 1)
plt.bar(latency_data.keys(), latency_data.values(), color='blue')
plt.title('Latency')
plt.ylabel('Latency (ms)')

# Requests per second graph
plt.subplot(3, 1, 2)
plt.bar(req_per_sec_data.keys(), req_per_sec_data.values(), color='green')
plt.title('Requests per Second')
plt.ylabel('Requests/sec')

# Transfer per second graph
plt.subplot(3, 1, 3)
transfer_labels = list(transfer_per_sec_data.keys())
transfer_values = [float(re.search(r'([\d.]+)', value).group(1)) for value in transfer_per_sec_data.values()]
plt.bar(transfer_labels, transfer_values, color='orange')
plt.title('Transfer per Second')
plt.ylabel('Transfer/sec (MB)')

plt.tight_layout()
plt.show()
