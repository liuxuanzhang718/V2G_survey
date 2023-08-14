import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime
import statistics

from get_data import pull

r_map = {'5': 1, '4': 0.5, '2': -0.5, '3': 0, '1': -1}

m = []
m_ev = []
m_vg = []

s = []
s_ev = []
s_vg = []
'''
gi = pull('GI01_01',r_map=r_map)
gi_ev = pull('GI01_01',evs_only=True,r_map=r_map)
gi_vg = pull('GI01_01',v2g_only=True,r_map=r_map)

temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))
'''
gi = pull('GI01_02',r_map=r_map)
gi_ev = pull('GI01_02',evs_only=True,r_map=r_map)
gi_vg = pull('GI01_02',v2g_only=True,r_map=r_map)

temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))

gi = pull('GI01_04',r_map=r_map)
gi_ev = pull('GI01_04',evs_only=True,r_map=r_map)
gi_vg = pull('GI01_04',v2g_only=True,r_map=r_map)

temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))

gi = pull('GI01_06',r_map=r_map)
gi_ev = pull('GI01_06',evs_only=True,r_map=r_map)
gi_vg = pull('GI01_06',v2g_only=True,r_map=r_map)

temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))

gi = pull('GI01_09',r_map=r_map)
gi_ev = pull('GI01_09',evs_only=True,r_map=r_map)
gi_vg = pull('GI01_09',v2g_only=True,r_map=r_map)

temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))

m = np.array(m)
m_ev = np.array(m_ev)
m_vg = np.array(m_vg)
s = np.array(s)
s_ev = np.array(s_ev)
s_vg = np.array(s_vg)


colors = ['#31688e','#35b779','#fde725']
plt.figure(figsize=(10,8))
plt.subplot(1,2,1)
plt.xticks(range(4),['A financial reward makes it more attractive for me\nto make my EV available for charge management',"I don't need to receive a financial reward for\nmy contribution to a stable electricity network","In an emergency, I allow an operator to stop my charger\nfor up to 1 hour to prevent electric grid issues.","I would pay an extra cost to be able to charge my\nEV regularly at peak times (7-9am and 4-7pm)"],rotation=90)
plt.ylim(-1.05,1.05)
plt.yticks([-1,-0.5,0,0.5,1],['Strongly disagree','Disagree','Neither','Agree','Strongly agree'])

plt.scatter(np.arange(4)-0.2,m,label='All',marker='x',c=colors[0],zorder=3)
plt.scatter(np.arange(4)+0.0,m_ev,label='EVs',marker='x',c=colors[1],zorder=3)
plt.scatter(np.arange(4)+0.2,m_vg,label='V2G',marker='x',c=colors[2],zorder=3)
for q in range(4):
    plt.plot([q-0.2,q-0.2],[m[q]-s[q],min(m[q]+s[q],1)],c=colors[0],zorder=2)
    plt.plot([q-0.2-0.05,q-0.2+0.05],[m[q]-s[q],m[q]-s[q]],c=colors[0],zorder=2)
    plt.plot([q-0.2-0.05,q-0.2+0.05],[min(m[q]+s[q],1),min(m[q]+s[q],1)],c=colors[0],zorder=2)
    
    plt.plot([q-0.,q-0.],[m_ev[q]-s_ev[q],min(m_ev[q]+s_ev[q],1)],c=colors[1],zorder=2)
    plt.plot([q-0.-0.05,q-0.+0.05],[m_ev[q]-s_ev[q],m_ev[q]-s_ev[q]],c=colors[1],zorder=2)
    plt.plot([q-0.-0.05,q-0.+0.05],[min(m_ev[q]+s_ev[q],1),min(m_ev[q]+s_ev[q],1)],c=colors[1],zorder=2)
    
    plt.plot([q+0.2,q+0.2],[m_vg[q]-s_vg[q],min(m_vg[q]+s_vg[q],1)],c=colors[2],zorder=2)
    plt.plot([q+0.2-0.05,q+0.2+0.05],[m_vg[q]-s_vg[q],m_vg[q]-s_vg[q]],c=colors[2],zorder=2)
    plt.plot([q+0.2-0.05,q+0.2+0.05],[min(m_vg[q]+s_vg[q],1),min(m_vg[q]+s_vg[q],1)],c=colors[2],zorder=2)

plt.grid(zorder=1)
plt.legend(ncol=3)


plt.subplot(1,2,2)

m = []
m_ev = []
m_vg = []

s = []
s_ev = []
s_vg = []

gi = pull('IC03_01',r_map=r_map)
gi_ev = pull('IC03_01',evs_only=True,r_map=r_map)
gi_vg = pull('IC03_01',v2g_only=True,r_map=r_map)
temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))

gi = pull('IC03_02',r_map=r_map)
gi_ev = pull('IC03_02',evs_only=True,r_map=r_map)
gi_vg = pull('IC03_02',v2g_only=True,r_map=r_map)
temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))

gi = pull('IC03_03',r_map=r_map)
gi_ev = pull('IC03_03',evs_only=True,r_map=r_map)
gi_vg = pull('IC03_03',v2g_only=True,r_map=r_map)
temp = []
for r in gi:
    temp += [r]*gi[r]
m.append(sum(temp)/len(temp))
s.append(statistics.stdev(temp))
temp = []
for r in gi_ev:
    temp += [r]*gi_ev[r]
m_ev.append(sum(temp)/len(temp))
s_ev.append(statistics.stdev(temp))
temp = []
for r in gi_vg:
    temp += [r]*gi_vg[r]
m_vg.append(sum(temp)/len(temp))
s_vg.append(statistics.stdev(temp))


m = np.array(m)
m_ev = np.array(m_ev)
m_vg = np.array(m_vg)
s = np.array(s)
s_ev = np.array(s_ev)
s_vg = np.array(s_vg)

plt.xticks(range(3),['I would participate in V2G with no savings','I would participate in V2G with 5% energy bill savings','I would participate in V2G with 10% energy bill savings'],rotation=90)
plt.ylim(-1.05,1.05)
plt.yticks([-1,-0.5,0,0.5,1],['Strongly disagree','Disagree','Neither','Agree','Strongly agree'])

plt.scatter(np.arange(3)-0.2,m,label='All',marker='x',c=colors[0],zorder=3)
plt.scatter(np.arange(3)+0.0,m_ev,label='EVs',marker='x',c=colors[1],zorder=3)
plt.scatter(np.arange(3)+0.2,m_vg,label='V2G',marker='x',c=colors[2],zorder=3)
for q in range(3):
    plt.plot([q-0.2,q-0.2],[m[q]-s[q],min(m[q]+s[q],1)],c=colors[0],zorder=2)
    plt.plot([q-0.2-0.05,q-0.2+0.05],[m[q]-s[q],m[q]-s[q]],c=colors[0],zorder=2)
    plt.plot([q-0.2-0.05,q-0.2+0.05],[min(m[q]+s[q],1),min(m[q]+s[q],1)],c=colors[0],zorder=2)
    
    plt.plot([q-0.,q-0.],[m_ev[q]-s_ev[q],min(m_ev[q]+s_ev[q],1)],c=colors[1],zorder=2)
    plt.plot([q-0.-0.05,q-0.+0.05],[m_ev[q]-s_ev[q],m_ev[q]-s_ev[q]],c=colors[1],zorder=2)
    plt.plot([q-0.-0.05,q-0.+0.05],[min(m_ev[q]+s_ev[q],1),min(m_ev[q]+s_ev[q],1)],c=colors[1],zorder=2)
    
    plt.plot([q+0.2,q+0.2],[m_vg[q]-s_vg[q],min(m_vg[q]+s_vg[q],1)],c=colors[2],zorder=2)
    plt.plot([q+0.2-0.05,q+0.2+0.05],[m_vg[q]-s_vg[q],m_vg[q]-s_vg[q]],c=colors[2],zorder=2)
    plt.plot([q+0.2-0.05,q+0.2+0.05],[min(m_vg[q]+s_vg[q],1),min(m_vg[q]+s_vg[q],1)],c=colors[2],zorder=2)
plt.grid(zorder=1)
plt.legend(ncol=3)
plt.tight_layout()
plt.show()

#IC03_01 No energy bill savings IC03_02 5% energy bill savings IC03_03 10% energy bill savings



