import matplotlib.pyplot as plt
import numpy as np
import itertools
import time, csv, datetime
import statistics
from sklearn import linear_model
from sklearn.preprocessing import normalize
from build_model import score, corr, score_within1
from matplotlib import cm

cmap = 'coolwarm'
cmap = 'RdBu'
coolwarm = cm.get_cmap(cmap, 1000)
coolwarm = coolwarm(np.linspace(1, 0, 1000))


cmap = 'PiYG'
pg = cm.get_cmap(cmap, 1000)
pg = pg(np.linspace(1, 0, 1000))

row_mapping = {}
with open('dfc.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for i in range(1,len(headers)):
        row_mapping[headers[i]] = i
        
        
        
# ok first let's start with a list of the potential candiates
input_variables = ['PI15','PI18','PI17','IQ17_02','CN01_03','CN01_04','IC01_06','IC01_07','IC01_09','V112_01','PI20','V106']

v_name = {'PI15':'Age',
          'PI16':'Gender',
          'PI18':'Income',
          'PI17':'Education',
          'IQ17_02':'How much do you know about V2G?',
          'CN01_03':'I fear the battery is not sufficiently\ncharged when I want to start a trip',
          'CN01_04':"I'm afraid the battery life could be shortened\nby the frequent charging and discharging.",
          'IC01_06':'V2G contributes to a stable electricity network for all',
          'IC01_07':'V2G allows me to use my EV for back-up power for my home',
          'IC01_08':'V2G helps me integrate my EV with my solar PV system',
          'IC01_09':'V2G helps reduce my carbon emissions',
          #'V112_01':'Annual Mileage',
          'PI20':'Number of Vehicles',
          'V106':"What's the type of your primary vehicle?\n(ICE, HEV, PHEV, BEV)",
          'CN01_02':'I would need to adapt my driving patterns',
          'IQ21_01':'Household has a smart energy meter',
          'IQ21_02':'Household has solar panels',
          #'IQ21_03':'Household has solar water heaters',
          'IQ21_04':'Household has a home battery',
          'IQ21_05':'Household has a green energy tariff',
          'IQ21_06':'Household has a EV specific tariff',
          'EQ10_09':'As a result of using V2G I feel that information about\nme is out there that could invade my privacy'}

v_min = {'PI15':1,'PI16':1,'PI18':1,'PI17':1,'IQ17_02':1,'CN01_02':1,'CN01_03':1,'CN01_04':1,'IC01_06':1,'IC01_07':1,'IC01_08':1,'IC01_09':1,'V112_01':0,'PI20':1,'V106':1,
         'IQ21_05':1,'IQ21_01':1,'IQ21_02':1,'IQ21_03':1,'IQ21_04':1,'IQ21_06':1,'EQ10_09':1}
v_max = {'PI15':8,'PI16':2,'PI18':10,'PI17':11,'IQ17_02':5,'CN01_02':5,'CN01_03':5,'CN01_04':5,'IC01_06':5,'IC01_07':5,'IC01_08':5,'IC01_09':5,'V112_01':np.inf,'PI20':4,'V106':4,
         'IQ21_05':2,'IQ21_01':2,'IQ21_02':2,'IQ21_03':2,'IQ21_04':2,'IQ21_06':2,'EQ10_09':5}




# first assign each variable a number
v_num = {}
num_v = {}
n = 0
for v in v_name:
    v_num[v] = n
    num_v[n] = v
    n += 1
    
Nvar = n

# now find the average variable for each variables
avs = {}
for v in v_name:
    _x = []
    with open('dfc.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            try:
                var = int(row[row_mapping[v]])
            except:
                continue
            if var >= v_min[v] and var <= v_max[v]:
                _x.append(var)
    avs[v] = sum(_x)/len(_x)
            

# plot cross-correlation
#'''
Z = np.zeros((n,n))
for x in range(n):
    for y in range(x,n):
        if x == y:
            Z[x,y] = None
            continue
            
        Z[x,y] = corr(x,y,num_v,v_min,v_max)*-1
        Z[y,x] = Z[x,y]

# reflect Z in the y axis

Z2 = np.zeros((n,n))
for x in range(n):
    for y in range(n):
        Z2[x,y] = Z[x,n-1-y]


        
plt.figure()
plt.imshow(Z2,cmap='PiYG',vmin=-0.5,vmax=0.5)
plt.yticks(range(20),np.arange(20,0,-1))
plt.xticks(range(20),range(1,21))
for x in range(n):
    print(x,end=': ')
    print(v_name[num_v[x]])
plt.colorbar()
#plt.show()
#'''

# now trying to build the best predictive model
target_variable = 'FI01_03'

# this method will find the best variable at a time
'''
best = None
f_max = 0

chosen = []
improving = True

while improving == True and len(chosen) < Nvar-2:
    for i in range(Nvar):
        if num_v[i] in chosen:
            continue
        input_variables = chosen + [num_v[i]]
        f, coef = score(input_variables,target_variable,v_min,v_max,avs,keep_bad=False)
        if f > f_max:
            f_max = f
            best = num_v[i]
    if best is not None:
        print('best new variable is '+str(v_name[best])+' with a score of '+str(f_max))
        chosen.append(best)
        best = None
        f_max = f_max#*1.00001 # new variable must imporve score by more than 0.01%
    else:
        print('no imporvement found with any variable')
        improving = False
        
#'''

# this method will find the best subset of varaibles for each number
'''
best = None
f_max = 0
improving = True
n_var = 1

while n_var < Nvar and improving == True:
    combinations = itertools.combinations(range(Nvar), n_var)
    for s in combinations:
        input_variables = [num_v[s[i]] for i in range(len(s))]
        f, coef = score(input_variables,target_variable,v_min,v_max,avs,keep_bad=False)
        if f > f_max:
            f_max = f
            best = input_variables

    if best is not None:
        print('For '+str(n_var)+' variables the best combination was: ')
        for v in best:
            print('-- '+str(v_name[v]))
        print('Which gave a score of '+str(f_max))
        chosen = best
        best = None
        n_var += 1

    else:
        print('no imporvement found with any additional variable')
        improving = False
#'''

# with logistic regression (normal)
#chosen = ['CN01_03','IC01_06','IC01_08','IC01_09','V106','IQ21_02','IQ21_06']

# with l1 penalty
#chosen = ['PI15','PI16','PI18','CN01_03','IC01_06','IC01_08','IC01_09','PI20','V106','IQ21_06']

# with l1 penalty 1 at a time
chosen = ['IC01_06', 'V106', 'CN01_04', 'EQ10_09', 'CN01_02', 'IQ21_01', 'PI17', 'PI20', 'IC01_09']

'''
For 7 variables the best combination was: 
-- Income
-- I fear the battery is not sufficiently
charged when I want to start a trip
-- V2G contributes to a stable electricity network for all
-- V2G helps me integrate my EV with my solar PV system
-- V2G helps reduce my carbon emissions
-- What's the type of your primary vehicle?
(ICE, HEV, PHEV, BEV)
-- Household has a EV specific tariff
Which gave a score of 0.52892131318395
'''

print(chosen)
print(score_within1(chosen,target_variable,v_min,v_max,avs,keep_bad=False))
f, coef = score(chosen,target_variable,v_min,v_max,avs,keep_bad=False) 

print(f)
Z = coef*-1
plt.figure(figsize=(8,10))
plt.imshow(Z,cmap='RdBu',vmin=-3,vmax=3)
plt.xticks(range(len(chosen)),[v_name[v] for v in chosen],rotation=90)
plt.ylabel('Would you use V2G chargers?')
plt.yticks(range(5),['Definitely not','Unlikely','Neutral','Likely','Definitely'])
plt.tight_layout()
plt.savefig('logit_model.png',dpi=300)


plt.figure()
plt.axis('off')
for i in range(1000):
    plt.plot([0,0],[i,i+1],c=coolwarm[i],lw=10)
plt.text(0.003,0-10,'-3.0')
plt.text(0.003,1000-10,'+3.0')
plt.text(0.003,500-10,' 0.0')
plt.text(0.003,1000/6*4-10,'+1.0')
plt.text(0.003,1000/6*5-10,'+2.0')
plt.text(0.003,1000/6*2-10,'-1.0')
plt.text(0.003,1000/6*1-10,'-2.0')
'''
plt.text(0.003,0-10,'-2.5')
plt.text(0.003,1000-10,'+2.5')
plt.text(0.003,500-10,' 0.0')
plt.text(0.003,700-10,'+1.0')
plt.text(0.003,900-10,'+2.0')
plt.text(0.003,300-10,'-1.0')
plt.text(0.003,100-10,'-2.0')
'''
plt.savefig('logit_scale.png',dpi=300)
plt.show()


'''
best score with sequential:
best new variable is V2G contributes to a stable electricity network for all with a score of 0.45988175675675674
best new variable is What's the type of your primary vehicle? (ICE, HEV, PHEV, BEV) with a score of 0.5022222222222222
best new variable is Annual Mileage with a score of 0.50497949619215
best new variable is I fear the battery is not sufficiently charged when I want to start a trip with a score of 0.5120093731693028
best new variable is V2G allows me to use my EV for back-up power for my home with a score of 0.5202108963093146
best new variable is V2G helps me integrate my EV with my solar PV system with a score of 0.5254833040421792
best new variable is Income with a score of 0.5269016697588126
best new variable is Gender with a score of 0.5285714285714286
best new variable is Household has a smart energy meter with a score of 0.5329192546583851
'''