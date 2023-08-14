import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime
import statistics

deg = []
deg_ev = []
deg_v2g = []
rng = []
rng_ev = []
rng_v2g = []
pri = []
pri_ev = []
pri_v2g = []
um = []
um_ev = []
um_v2g = []
sc = []
sc_ev = []
sc_v2g = []
v2g = []
v2g_ev = []
v2g_v2g = []


eq0901 = [0,0,0]
eq0902 = [0,0,0]
eq0903 = [0,0,0]
eq0904 = [0,0,0]
eq0905 = [0,0,0]
eq0906 = [0,0,0]

with open('dfc.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row[48] != '':
            if int(row[48]) > 0:
                deg.append(int(row[48]))
                if row[80] == '4' or row[96] == '4':
                    deg_ev.append(int(row[48]))
                if row[3] == '4':
                    deg_v2g.append(int(row[48]))
        if row[57] != '':
            if int(row[57]) >= 0:
                um.append(int(row[57]))
                if row[80] == '4' or row[96] == '4':
                    um_ev.append(int(row[57]))
                if row[3] == '4':
                    um_v2g.append(int(row[57]))
        if row[58] != '':
            if int(row[57]) >= 0:
                sc.append(int(row[58]))
                if row[80] == '4' or row[96] == '4':
                    sc_ev.append(int(row[58]))
                if row[3] == '4':
                    sc_v2g.append(int(row[58]))
        if row[59] != '':
            if int(row[57]) >= 0:
                v2g.append(int(row[59]))
                if row[80] == '4' or row[96] == '4':
                    v2g_ev.append(int(row[59]))
                if row[3] == '4':
                    v2g_v2g.append(int(row[59]))
        if row[47] != '':
            if int(row[47]) > 0:
                rng.append(int(row[47]))
                if row[80] == '4' or row[96] == '4':
                    rng_ev.append(int(row[47]))
                if row[3] == '4':
                    rng_v2g.append(int(row[48]))
        if row[134] != '':
            if int(row[134]) > 0:
                pri.append(int(row[134]))
                if row[80] == '4' or row[96] == '4':
                    pri_ev.append(int(row[134]))
                if row[3] == '4':
                    pri_v2g.append(int(row[134]))


for lst in [um,um_ev,um_v2g,sc,sc_ev,sc_v2g,v2g,v2g_ev,v2g_v2g]:
    print((sum(lst)/len(lst)-1)/4)
    print(statistics.stdev(lst)/4)
    print('')


#Battery degradation
deg_m = [0.65,0.654699427480916,0.6548964218455744,0.42168674698795183]
deg_s = [0.3,0.2597972503389549,0.2753977202985951,0.30224694828739784]

#Range anxiety
rng_m = [0.6,0.5698398576512456,0.5261989342806395,0.36494252873563215]
rng_s = [0.3,0.26666539470275846,0.27717456541711166,0.36329523378542355]

#Data concerns
pri_m=[0.5166666667,0.5680417259364627,0.5206286836935167,0.4375]
pri_s=[0.3166666667,0.26383539187843225,0.26908783955448184,0.2926689605713727]

# Unmanaged
um_m = [(5.5-1)/6,0.7020636285468616,0.641156462585034,0.5]
um_s = [(1.6)/6,0.2850429845592431,0.35061156986384334,0.36158972114370397]

# smart charging
sc_m = [(5.4-1)/6,0.841573516766982,0.9026360544217686,0.9034090909090908]
sc_s = [(1.7)/6,0.205169576784965,0.1851074282479854,0.15365199045010447]

v2g_m = [4/7,0.766981943250215,0.7593537414965987,0.9090909090909092]
v2g_s = [1.9/6,0.2873342164307587,0.33708479266743385,0.17852290727565623]


colors = ['#440154','#31688e','#35b779','#fde725']
plt.figure(figsize=(9,3.5))

plt.subplot(1,2,1)
plt.scatter(np.arange(3)-0.15,[um_m[0],sc_m[0],v2g_m[0]],label='2013',marker='x',c=colors[0],zorder=3)
plt.scatter(np.arange(3)-0.05,[um_m[1],sc_m[1],v2g_m[1]],label='2021 (all)',marker='x',c=colors[1],zorder=3)
plt.scatter(np.arange(3)+0.05,[um_m[2],sc_m[2],v2g_m[2]],label='2021 (EVs)',marker='x',c=colors[2],zorder=3)
plt.scatter(np.arange(3)+0.15,[um_m[3],sc_m[3],v2g_m[3]],label='2021 (V2G)',marker='x',c=colors[3],zorder=3)
for y in range(4):
    plt.plot([0-0.15+0.1*y,0-0.15+0.1*y],[um_m[y]-um_s[y],um_m[y]+um_s[y]],c=colors[y],zorder=2)
    plt.plot([0-0.15+0.1*y-0.02,0-0.15+0.1*y+0.02],[um_m[y]-um_s[y],um_m[y]-um_s[y]],c=colors[y],zorder=2)
    plt.plot([0-0.15+0.1*y-0.02,0-0.15+0.1*y+0.02],[min(0.999,um_m[y]+um_s[y]),min(0.999,um_m[y]+um_s[y])],c=colors[y],zorder=2)
    
    plt.plot([1-0.15+0.1*y,1-0.15+0.1*y],[sc_m[y]-sc_s[y],sc_m[y]+sc_s[y]],c=colors[y],zorder=2)
    plt.plot([1-0.15+0.1*y-0.02,1-0.15+0.1*y+0.02],[sc_m[y]-sc_s[y],sc_m[y]-sc_s[y]],c=colors[y],zorder=2)
    plt.plot([1-0.15+0.1*y-0.02,1-0.15+0.1*y+0.02],[min(0.999,sc_m[y]+sc_s[y]),min(0.999,sc_m[y]+sc_s[y])],c=colors[y],zorder=2)
    
    plt.plot([2-0.15+0.1*y,2-0.15+0.1*y],[v2g_m[y]-v2g_s[y],v2g_m[y]+v2g_s[y]],c=colors[y],zorder=2)
    plt.plot([2-0.15+0.1*y-0.02,2-0.15+0.1*y+0.02],[v2g_m[y]-v2g_s[y],v2g_m[y]-v2g_s[y]],c=colors[y],zorder=2)
    plt.plot([2-0.15+0.1*y-0.02,2-0.15+0.1*y+0.02],[min(0.999,v2g_m[y]+v2g_s[y]),min(0.999,v2g_m[y]+v2g_s[y])],c=colors[y],zorder=2)
plt.ylim(0,1)
plt.xticks(range(3),['Unmanaged Charging','Smart Charging','V2G Charging'],rotation=0)
plt.grid(zorder=0,axis='y')
plt.ylabel('How Likely Are You To Use (0-1)')
plt.legend(ncol=2)    

plt.subplot(1,2,2)
plt.scatter(np.arange(3)-0.15,[deg_m[0],rng_m[0],pri_m[0]],label='2013',marker='x',c=colors[0],zorder=3)
plt.scatter(np.arange(3)-0.05,[deg_m[1],rng_m[1],pri_m[1]],label='2021 (all)',marker='x',c=colors[1],zorder=3)
plt.scatter(np.arange(3)+0.05,[deg_m[2],rng_m[2],pri_m[2]],label='2021 (EVs)',marker='x',c=colors[2],zorder=3)
plt.scatter(np.arange(3)+0.15,[deg_m[3],rng_m[3],pri_m[3]],label='2021 (V2G)',marker='x',c=colors[3],zorder=3)
for y in range(4):
    plt.plot([0-0.15+0.1*y,0-0.15+0.1*y],[deg_m[y]-deg_s[y],deg_m[y]+deg_s[y]],c=colors[y],zorder=2)
    plt.plot([0-0.15+0.1*y-0.02,0-0.15+0.1*y+0.02],[deg_m[y]-deg_s[y],deg_m[y]-deg_s[y]],c=colors[y],zorder=2)
    plt.plot([0-0.15+0.1*y-0.02,0-0.15+0.1*y+0.02],[deg_m[y]+deg_s[y],deg_m[y]+deg_s[y]],c=colors[y],zorder=2)
    
    plt.plot([1-0.15+0.1*y,1-0.15+0.1*y],[rng_m[y]-rng_s[y],rng_m[y]+rng_s[y]],c=colors[y],zorder=2)
    plt.plot([1-0.15+0.1*y-0.02,1-0.15+0.1*y+0.02],[rng_m[y]-rng_s[y],rng_m[y]-rng_s[y]],c=colors[y],zorder=2)
    plt.plot([1-0.15+0.1*y-0.02,1-0.15+0.1*y+0.02],[rng_m[y]+rng_s[y],rng_m[y]+rng_s[y]],c=colors[y],zorder=2)
    
    plt.plot([2-0.15+0.1*y,2-0.15+0.1*y],[pri_m[y]-pri_s[y],pri_m[y]+pri_s[y]],c=colors[y],zorder=2)
    plt.plot([2-0.15+0.1*y-0.02,2-0.15+0.1*y+0.02],[pri_m[y]-pri_s[y],pri_m[y]-pri_s[y]],c=colors[y],zorder=2)
    plt.plot([2-0.15+0.1*y-0.02,2-0.15+0.1*y+0.02],[pri_m[y]+pri_s[y],pri_m[y]+pri_s[y]],c=colors[y],zorder=2)
plt.ylim(0,1)
plt.xticks(range(3),['Battery Degradation','Range Anxiety','Data Privacy$^*$'],rotation=0)
plt.grid(zorder=0,axis='y')
plt.ylabel('Level of Concern (0-1)')
#plt.legend(ncol=4)    
plt.tight_layout()
plt.savefig('compare.png',dpi=300)







plt.show()

plt.scatter(np.arange(4)-0.1,deg_m,marker='x',c='#D81B60',zorder=3,label='Battery Degradation')
for i in range(4):
    plt.plot([i-0.1,i-0.1],[deg_m[i]-deg_s[i],deg_m[i]+deg_s[i]],zorder=2,c='#D81B60',alpha=0.4)
#plt.subplot(3,1,2)
#plt.title('Range anxiety')
plt.scatter(range(4),rng_m,marker='x',c='#1E88E5',zorder=3,label='Range Anxiety')
for i in range(4):
    plt.plot([i,i],[rng_m[i]-rng_s[i],rng_m[i]+rng_s[i]],zorder=2,c='#74B0E4')
#plt.subplot(3,1,3)
#plt.title('Data privacy')
plt.scatter(np.arange(4)+0.1,pri_m,marker='x',c='#FFC107',zorder=3,label='Data Privacy*')
for i in range(4):
    plt.plot([i+0.1,i+0.1],[pri_m[i]-pri_s[i],pri_m[i]+pri_s[i]],zorder=2,c='#F3DC99')
plt.ylim(0,1)
plt.xticks(range(4),['2013 Survey','2021 Survey','2021 Survey\n(EV owners)','2021 Survey\n(V2G participants)'],rotation=0)
plt.grid(zorder=0,axis='y')
plt.legend(ncol=3)
plt.tight_layout()

plt.show()
#print(len(rng))
#print(len(rng_ev))
#plt.figure()
#plt.bar(np.arange(5)-0.2,sc,width=0.4)
#plt.bar(np.arange(5)+0.2,v2g,width=0.4)
#plt.show()