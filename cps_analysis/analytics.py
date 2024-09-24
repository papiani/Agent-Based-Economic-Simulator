import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

# data from https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html
df = pd.read_csv('cps_analysis/aug24pub.csv')
'''
ionc = df['hefaminc']
buckets = {x + 1: 0 for x in range(16)}
invalids = 0
valids = 0
for id,data in ionc.items() :
    if data < 1 :
        invalids+=1
    else:
        buckets[data] = buckets[data] +1
        valids +=1
print(buckets)
print(f'invalids: {invalids}\nvalids: {valids}')

# plotting below
plt.figure(figsize=(10, 5))
plt.bar(buckets.keys(), buckets.values(), color='skyblue')
plt.xlabel('Buckets')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')
plt.show()
'''

df = pd.read_csv('cps_analysis/aug24pub.csv')
ionc = df['hrhhid','hrnumhou']
buckets = {x + 1: 0 for x in range(16)}
invalids = 0
valids = 0
for row,id,data in ionc.items() :
    if data < 1 :
        invalids+=1
    else:
        buckets[data] = buckets[data] +1
        valids +=1
print(buckets)
print(f'invalids: {invalids}\nvalids: {valids}')

# plotting below
plt.figure(figsize=(10, 5))
plt.bar(buckets.keys(), buckets.values(), color='skyblue')
plt.xlabel('Buckets')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')
plt.show()
