import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime, copy, random
import statistics
from matplotlib import cm

cmap = 'coolwarm'
coolwarm = cm.get_cmap(cmap, 1000)
coolwarm = coolwarm(np.linspace(0, 1, 1000))

'''
old_data = []
with open('dfc.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    old_header = next(reader)
    for row in reader:
        old_data.append(row)

for i in range(len(old_header)):
    if old_header[i] == 'income':
        inc_r = i
    if old_header[i] == 'origin':
        o_r = i

smedia2prolific_map = {'1':'1','2':'1','3':'2','4':'3','5':'4','6':'5','7':'5','8':'6','9':'6','10':'6'}
inc = []
for i in range(len(old_data)):
    if old_data[i][o_r] == 'smedia':
        if old_data[i][inc_r] in smedia2prolific_map:
            inc.append(smedia2prolific_map[old_data[i][inc_r]])
        else:
            inc.append(old_data[i][inc_r])
    else:
        inc.append(old_data[i][inc_r])

with open('dfc2.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(old_header+['PI18'])
    for i in range(len(old_data)):
        writer.writerow(old_data[i]+[inc[i]])
        
'''

from get_data import pull_demo, pull, pull_all



mainq = 'FI01_03'
mainq = 'FI01_02'
mainq = 'FI01_01'


sc_knowledge = pull_all('IQ17_01')
v2g_knowledge = pull_all('IQ17_02')
v2g_trial = pull_all('IQ18')

charger_time = pull_all('VG03')


v2g_likely = pull_all('FI01_03')
sc_likely = pull_all('FI01_03')

vehicle_type = pull_all('V106')
vehicle_len = pull_all('V109')

def scatter(a,b):
    x = []
    y = []
    for i in range(len(a)):
        try:
            if int(a[i])>0 and int(b[i])>0:
                x.append(int(a[i])+random.random()-0.5)
                y.append(int(b[i])+random.random()-0.5)
        except:
            continue
    return x,y

def scatter_filt(a,b,c,c_filt):
    x = []
    y = []
    for i in range(len(a)):
        if c[i] != c_filt:
            continue
        try:
            if int(a[i])>0 and int(b[i])>0:
                x.append(int(a[i])+random.random()-0.5)
                y.append(int(b[i])+random.random()-0.5)
        except:
            continue
    return x,y

x,y = scatter_filt(vehicle_len,v2g_likely,vehicle_type,'4')
#x,y = scatter_filt(v2g_knowledge,v2g_likely,v2g_trial,'4')
print(np.corrcoef(x,y))
plt.figure()
plt.scatter(x,y,marker='x')
plt.xlabel('Length of EV ownership')
plt.ylabel('Likely to participate in V2G')


x,y = scatter(charger_time,v2g_likely)
#x,y = scatter_filt(v2g_knowledge,v2g_likely,v2g_trial,'4')
print(np.corrcoef(x,y))
plt.figure()
plt.scatter(x,y,marker='x')
plt.xlabel('Length of charger ownership')
plt.ylabel('Likely to participate in V2G')


x,y = scatter(v2g_knowledge,v2g_likely)
#x,y = scatter(sc_knowledge,sc_likely)
print(np.corrcoef(x,y))
plt.figure()
plt.scatter(x,y,marker='x')
plt.xlabel('Knowledge of V2G')
plt.ylabel('Likely to participate in V2G')




plt.show()


