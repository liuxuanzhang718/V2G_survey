import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime, copy
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

from get_data import pull_demo, pull

d = [0]*41+[1]*67+[2]*351+[3]*846+[5]*594
mean0 = np.mean(d)
std0 = np.std(d)

def average(dic):
    tot = 0
    n = 0
    for i in range(1,6):
        try:
            tot += (i-1)*dic[str(i)]
            n += dic[str(i)]
        except:
            continue
    if n > 0:
        print(tot/n)
        print(mean0)
        print((std0/np.sqrt(n)))
        return ((tot/n)-mean0)/(std0/np.sqrt(n))
    else:
        return np.nan
def merge(d1,d2):
    new = copy.deepcopy(d1)
    for k in d2:
        if k not in new:
            new[k] = 0
        new[k] += d2[k]
    return new

def n(d):
    t = 0
    for k in d:
        t += d[k]
    return t

def mstd(dic):
    lst = []
    for i in range(1,6):
        if str(i) in dic:
            lst += [i-1]*dic[str(i)]
    return np.mean(lst), np.std(lst)

mainq = 'FI01_03'
#mainq = 'FI01_02'
#mainq = 'FI01_01'

male = pull_demo(mainq,'PI16','1')
female = pull_demo(mainq,'PI16','2')
mean0, std0 = mstd(merge(male,female))

print('Gender')
survey = np.array([n(male), n(female)])
uka = np.array([97.75,100])
survey = survey/sum(survey)
uka = uka/sum(uka)

plt.figure()
plt.title('Gender')

plt.bar(np.arange(2)-0.2,survey,width=0.4)
plt.bar(np.arange(2)+0.2,uka,width=0.4)
plt.xticks([0,1],['Male','Female'])
plt.ylabel('Percentage')

urban = pull_demo(mainq,'PI14','1')
rural = pull_demo(mainq,'PI14','2')


age1 = pull_demo(mainq,'PI15','1')
age2 = pull_demo(mainq,'PI15','2')
age3 = pull_demo(mainq,'PI15','3')
age4 = pull_demo(mainq,'PI15','4')
age5 = pull_demo(mainq,'PI15','5')
age6 = pull_demo(mainq,'PI15',['6','7','8'])


print('Age')
print(n(pull_demo(mainq,'PI15','2')))
print(n(pull_demo(mainq,'PI15','3')))
print(n(pull_demo(mainq,'PI15','4')))
print(n(pull_demo(mainq,'PI15','5')))
print(n(pull_demo(mainq,'PI15','6')))
print(n(pull_demo(mainq,'PI15','7')))
print(n(pull_demo(mainq,'PI15','8')))

survey = np.array([n(pull_demo(mainq,'PI15','1')),
                   n(pull_demo(mainq,'PI15','2')),
                   n(pull_demo(mainq,'PI15','3')),
                   n(pull_demo(mainq,'PI15','4')),
                   n(pull_demo(mainq,'PI15','5')),
                   n(pull_demo(mainq,'PI15','6')),
                   n(pull_demo(mainq,'PI15','7')),
                   n(pull_demo(mainq,'PI15','8'))])
uka = np.array([9.4,6.8+6.6,6.7+7.3,7.3+6.4,5.7+6.0,4.8+3.9,3.2+2.4,2.2])
survey = survey/sum(survey)
uka = uka/sum(uka)

plt.figure()
plt.title('Age')
plt.bar(np.arange(8)-0.2,survey,width=0.4,label='Survey')
plt.bar(np.arange(8)+0.2,uka,width=0.4,label='UK av.')
plt.legend()
plt.xticks(range(8),['18-25','26-35','36-45','46-55','56-65','66-75','76-85','85+'])
plt.ylabel('Percentage')

ed2 = pull_demo(mainq,'PI17',['1','2'])
ed3 = pull_demo(mainq,'PI17','3')
ed4 = pull_demo(mainq,'PI17',['7','8'])
ed5 = pull_demo(mainq,'PI17','9')
ed6 = pull_demo(mainq,'PI17','10')
ed7 = pull_demo(mainq,'PI17','11')

uka = np.array([18.2,9.6+13.4,16.9,5.3,33.8])
survey = np.array([n(pull_demo('FI01_03','PI17','1')),n(pull_demo('FI01_03','PI17','2')),
                   n(pull_demo('FI01_03','PI17','3')),n(pull_demo('FI01_03','PI17',['7','8'])),
                   n(pull_demo('FI01_03','PI17',['9','10','11']))])

survey = survey/sum(survey)
uka = uka/sum(uka)
print('Education')
print(n(pull_demo(mainq,'PI17','1')))
print(n(pull_demo(mainq,'PI17','2')))
print(n(pull_demo(mainq,'PI17','3')))
print(n(pull_demo(mainq,'PI17','7')))
print(n(pull_demo(mainq,'PI17','8')))
print(n(pull_demo(mainq,'PI17','9')))
print(n(pull_demo(mainq,'PI17','10')))
print(n(pull_demo(mainq,'PI17','11')))

plt.figure()
plt.title('Education')
plt.bar(np.arange(5)-0.2,survey,width=0.4,label='Survey')
plt.bar(np.arange(5)+0.2,uka,width=0.4,label='UK av.')
plt.legend()
plt.xticks(range(5),['Primary','GCSEs','A-levels','Vocational','Degree'])
plt.ylabel('Percentage')

veh0 = pull_demo(mainq,'PI20','-1')
veh1 = pull_demo(mainq,'PI20','1')
veh2 = pull_demo(mainq,'PI20','2')
veh3 = pull_demo(mainq,'PI20',['3','4'])

dr1 = pull_demo(mainq,'V106','1')
dr2 = pull_demo(mainq,'V106','2')
dr3 = pull_demo(mainq,'V106','3')
dr4 = pull_demo(mainq,'V106','4')

own1 = pull_demo(mainq,'V107','1')
own2 = pull_demo(mainq,'V205','1')
own3 = pull_demo(mainq,'V301','1')

own = merge(own1,own2)
own = merge(own,own3)

lea1 = pull_demo(mainq,'V107','2')
lea2 = pull_demo(mainq,'V205','2')
lea3 = pull_demo(mainq,'V301','2')

lea = merge(lea1,lea2)
lea = merge(lea,lea3)

co1 = pull_demo(mainq,'V107','3')
co2 = pull_demo(mainq,'V205','3')
co3 = pull_demo(mainq,'V301','3')

co = merge(co1,co2)
co = merge(co,co3)


inc1 = pull_demo(mainq,'PI18','1')
inc2 = pull_demo(mainq,'PI18','2')
inc3 = pull_demo(mainq,'PI18','3')
inc4 = pull_demo(mainq,'PI18','4')
inc5 = pull_demo(mainq,'PI18','5')
inc6 = pull_demo(mainq,'PI18','6')

vmin = -2
vmax = 2

plt.figure(figsize=(5,13))
plt.subplot(9,1,1)
plt.title('Gender',weight='bold')
z = [[np.nan]*6]

z[0][0] = average(male)
z[0][1] = average(female)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks([0,1],['Male','Female'])
plt.yticks([],[])

plt.subplot(9,1,2)
plt.title('Residential Location',weight='bold')
z = [[np.nan]*6]
mean0, std0 = mstd(merge(urban,rural))
z[0][0] = average(urban)
z[0][1] = average(rural)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks([0,1],['Urban','Rural'])
plt.yticks([],[])

plt.subplot(9,1,3)
z = [[np.nan]*6]
plt.title('Age',weight='bold')
mean0, std0 = mstd(merge(merge(merge(merge(merge(age1,age2),age3),age4),age5),age6))
z[0][0] = average(age1)
z[0][1] = average(age2)
z[0][2] = average(age3)
z[0][3] = average(age4)
z[0][4] = average(age5)
z[0][5] = average(age6)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks([0,1,2,3,4,5],['18-25','26-35','36-45','46-55','56-65','66+'])
plt.yticks([],[])


plt.subplot(9,1,4)
z = [[np.nan]*6]
plt.title('Education',weight='bold')
mean0, std0 = mstd(merge(merge(merge(merge(merge(ed2,ed3),ed4),ed5),ed6),ed7))
z[0][0] = average(ed2)
z[0][1] = average(ed3)
z[0][2] = average(ed4)
z[0][3] = average(ed5)
z[0][4] = average(ed6)
z[0][5] = average(ed7)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks([0,1,2,3,4,5],['GCSEs','A-levels','Higher','Bachelors','Masters','PhD'])
plt.yticks([],[])



plt.subplot(9,1,5)
plt.title('Vehicles',weight='bold')
z = [[np.nan]*6]
mean0, std0 = mstd(merge(merge(merge(veh0,veh1),veh2),veh3))
z[0][0] = average(veh0)
z[0][1] = average(veh1)
z[0][2] = average(veh2)
z[0][3] = average(veh3)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks([0,1,2,3],['0','1','2','3'])
plt.yticks([],[])

plt.subplot(9,1,6)
z = [[np.nan]*6]
plt.title('Main Vehicle',weight='bold')
mean0, std0 = mstd(merge(merge(merge(dr1,dr2),dr3),dr4))
z[0][0] = average(dr1)
z[0][1] = average(dr2)
z[0][2] = average(dr3)
z[0][3] = average(dr4)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks([0,1,2,3],['ICE','Hybrid','PHEV','BEV'])
plt.yticks([],[])

plt.subplot(9,1,7)
z = [[np.nan]*6]
plt.title('Vehicle Ownership',weight='bold')
mean0, std0 = mstd(merge(merge(own,lea),co))
z[0][0] = average(own)
z[0][1] = average(lea)
z[0][2] = average(co)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks([0,1,2],['Owned','Leased','Company'])
plt.yticks([],[])

plt.subplot(9,1,8)
z = [[np.nan]*6]
plt.title('Income',weight='bold')
mean0, std0 = mstd(merge(merge(merge(merge(merge(inc1,inc2),inc3),inc4),inc5),inc6))
z[0][0] = average(inc1)
z[0][1] = average(inc2)
z[0][2] = average(inc3)
z[0][3] = average(inc4)
z[0][4] = average(inc5)
z[0][5] = average(inc6)
plt.imshow(z,vmin=vmin,vmax=vmax,cmap=cmap)
plt.xticks(range(6),['<20k','20-30k','30-40k','40-50k','50-70k','>70k'])
plt.yticks([],[])

plt.subplot(8,1,8)
plt.title('Scale',weight='bold')
z = []
for i in range(100):
    z.append(i/100)
plt.imshow([z],vmin=0,vmax=1,cmap=cmap,aspect=2)
plt.yticks([],[])
plt.xticks([0,99],[vmin,vmax])
plt.savefig('v2g.png')

plt.show()
