import sys
import csv
import matplotlib.pyplot as plt
fname = sys.argv[1]
mem_write_bw = []
mem_write = False
mem_read_bw = []
mem_read = False

load_lat = []
load_lat_bool = False

rand_lat = []
rand_lat_bool = False
with open(f"{fname}.txt",errors='replace') as f:
    for line in f.readlines():
        if "Memory write bandwidth" in line:
            mem_write = True
        elif "Memory read bandwidth" in line:
            mem_read = True
        elif "Memory load latency" in line:
            load_lat_bool = True
        elif "Random load latency" in line:
            rand_lat_bool = True
        elif line=='\n':
            mem_write = False
            mem_read = False
            rand_lat_bool = False
            load_lat_bool = False
        if mem_write:
            mem_write_bw.append(line)
        elif mem_read:
            mem_read_bw.append(line)
        elif load_lat_bool:
            load_lat.append(line)
        elif rand_lat_bool:
            rand_lat.append(line)

with open(f"{fname}_read.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Index","Bandwidth"])
    for item in mem_read_bw:
        splits = item.split(' ')
        if 'Memory' in splits: continue
        writer.writerow([splits[0],splits[1][:-1]])

with open(f"{fname}_write.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Index","Bandwidth"])
    for item in mem_write_bw:
        splits = item.split(' ')
        if 'Memory' in splits: continue
        writer.writerow([splits[0],splits[1][:-1]])

with open(f"{fname}_loadlat.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Index","Latency"])
    for item in load_lat:
        if "stride" in item: continue
        if "latency" in item: continue
        splits = item.split(' ')
        writer.writerow([splits[0],splits[1][:-1]])

with open(f"{fname}_randlat.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Index","Latency"])
    for item in rand_lat:
        if "stride" in item: continue
        if "latency" in item: continue
        splits = item.split(' ')
        writer.writerow([splits[0],splits[1][:-1]])
