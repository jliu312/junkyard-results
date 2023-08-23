#!/usr/bin/env python3
import argparse
import os
import json
import csv
NAMES={
    'fio_t4gsmall.json': 'AWS-t4g.small',
    'fio_t4glarge.json': 'AWS-t4g.large',    
    'fio_kvm_app.json': 'KVM-App',
    'fio_t4g2xlarge.json': 'AWS-t4g.2xlarge',
    'coremark_kvm_app.json': 'KVM-App',
    'coremark_t4gsmall.json': 'AWS-t4g.small',
    'coremark_t4glarge.json': 'AWS-t4g.large'
}
FIO_METRIC=['sequential_write','sequential_read','random_write_test','random_read_test','random_read_test_parallel']
PERCENTILES=['p1','p5','p10','p20','p30','p40','p50','p60','p70','p80','p90','p95','p99','p99.5','p99.9','p99.95','p99.99']
def parse_fio():
    directory = 'fio'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            with open(f) as jf:
                js = json.load(jf)
                name = NAMES[filename]
                to_csv_fio(js,name)
def to_csv_fio(json_file,name):
    for metric in FIO_METRIC:
        filtered = [o for o in json_file if metric==o['metric'].split(':')[0]]
        with open(f'fio_{name}_{metric}.csv', 'w+', newline='') as file:
             writer = csv.writer(file)
             writer.writerow(["Test","R/W", "Metric","Value type","Value","Percentile","Units"])
             for obj in filtered:
                 val=''
                 value=obj['value']
                 unpacked=obj['metric'].split(':')
                 unit=obj['unit']
                 if len(unpacked)==4:
                     test,rw,metric,val=unpacked
                 else:
                     test,rw,val=unpacked
                 if val in PERCENTILES:
                     percentile=val[1:]
                     writer.writerow([test,rw,metric,val,value,percentile,unit])
                 else:
                     writer.writerow([test,rw,metric,val,value,-1,unit])    

def parse_coremark():
    directory = 'coremark'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            with open(f) as jf:
                js = json.load(jf)
                name = NAMES[filename]
                to_csv_coremark(js,name)
def to_csv_coremark(json_file,name):
    print(name)
    for obj in json_file:
        if obj['metric']=="Coremark Score":
            print(obj)
            print("------------")
def main(args):
    if args.all:
        pass
    elif args.benchmark=='fio':
        parse_fio()
    elif args.benchmark=='coremark':
        parse_coremark()
    elif args.benchmark=='lmbench':
        parse_lmbench()
    else:
        print("No known benchmark specified")
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("benchmark", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-a", "--all", action="store_true", default=False)
    
    args = parser.parse_args()
    main(args)
