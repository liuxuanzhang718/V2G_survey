import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime, random
import statistics


row_mapping = {}
with open('dfc.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for i in range(1,len(headers)):
        row_mapping[headers[i]] = i

def scatter(val1,val2):
    x = []
    y = []
    with open('dfc.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if (row[80] != '4' and row[96] != '4'):
                continue
            
            if row[80] == '4':
                rown = row_mapping[val1]
            else:
                rown = row_mapping['V207']
            try:
                if int(row[rown]) < 0:
                    continue
                if int(row[row_mapping[val2]]) < 0:
                    continue
            except:
                continue
            x.append(int(row[rown]))#+(random.random()-0.5))
            y.append(int(row[row_mapping[val2]]))#+(random.random()-1)*0.5)
    return x,y

x,y = scatter('V109','CN01_03')
Z = np.zeros((5,5))
for i in range(len(x)):
    try:
        Z[y[i]-1,x[i]-1] += 1
    except:
        continue
plt.figure()
plt.imshow(Z)
x,y = scatter('V109','CN01_04')
Z = np.zeros((5,5))
for i in range(len(x)):
    try:
        Z[y[i]-1,x[i]-1] += 1
    except:
        continue
plt.figure()
plt.imshow(Z)
x,y = scatter('V109','CN01_02')
Z = np.zeros((5,5))
for i in range(len(x)):
    try:
        Z[y[i]-1,x[i]-1] += 1
    except:
        continue
plt.figure()
plt.imshow(Z)
plt.show()