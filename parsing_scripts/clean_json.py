#!/usr/bin/env python3
import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()
    ols = []
    L = len(lines)
    print(lines)
    for i in range(L):
        line = lines[i]
        if i==0 and line[0]!='[':
            line = '['+line
        if line[-2]=='}':
            line = line[:-1]+','+line[-1]
        if i==L-1 and line[-2]!=']':
            line = line[:-2]+']'+line[-1]
        ols.append(line)
    #print(ols)
    with open(sys.argv[2],'w+') as outf:
        outf.writelines(ols)
