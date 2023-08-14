import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime
import statistics
from sklearn import linear_model
from sklearn.preprocessing import normalize

row_mapping = {}
with open('dfc.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for i in range(1,len(headers)):
        row_mapping[headers[i]] = i
        
target_variable = 'FI01_03'
input_variables = ['PI15','PI16','PI18','PI17','IQ17_02','CN01_03','CN01_04','IC01_09','V112_01','PI20','V106']
vmin = [1,1,1,1,1,1,1,1,0,-1,1]
vmax = [8,2,6,11,5,5,5,5,np.inf,3,4]
# age, gender, income, education, knowledge of v2g, range anxiety, battery degradation, V2G helps reduce my carbon emissions, annual mileage, number of vehicles, primary vehicle type

target_variable = 'FI01_03'
input_variables = ['PI15','PI18','PI17','IQ17_02','CN01_03','CN01_04','IC01_06','IC01_07','IC01_09','V112_01','PI20','V106']
vmin = [1,1,1,1,1,1,1,1,1,0,-1,1]
vmax = [8,6,11,5,5,5,5,5,5,np.inf,3,4]
# age, income, education, knowledge of v2g, range anxiety, battery degradation, V2G contributes to a stable electricity network, V2G allows me to use my EV for back-up power, V2G helps reduce my carbon emissions, Vannual mileage, number of vehicles, primary vehicle type


target_variable = 'FI01_03'
input_variables = ['PI15','PI18','CN01_03','CN01_04','IC01_06','IC01_07','IC01_09','V112_01','PI20','V106']
vmin = [1,1,1,1,1,1,1,0,-1,1]
vmax = [8,6,5,5,5,5,5,np.inf,3,4]
# age, income, range anxiety, battery degradation, V2G contributes to a stable electricity network, V2G allows me to use my EV for back-up power, V2G helps reduce my carbon emissions, Vannual mileage, number of vehicles, primary vehicle type

target_variable = 'FI01_03'
input_variables = ['PI15','PI18','CN01_03','CN01_04','IC01_06','IC01_07','IC01_09','PI20','V106']
vmin = [1,1,1,1,1,1,1,-1,1]
vmax = [8,6,5,5,5,5,5,3,4]
# age, income, range anxiety, battery degradation, V2G contributes to a stable electricity network, V2G allows me to use my EV for back-up power, V2G helps reduce my carbon emissions, number of vehicles, primary vehicle type

target_variable = 'FI01_03'
input_variables = ['PI15','PI18','V106','CN01_03','CN01_04','IC01_06','IC01_07','IC01_09','AT01_01','AT01_02','AT01_03']
vmin = [1,1,1,1,1,1,1,1,1,1,1]
vmax = [8,6,4,5,5,5,5,5,5,5,5]


# age, income, range anxiety, battery degradation, V2G contributes to a stable electricity network, V2G allows me to use my EV for back-up power, V2G helps reduce my carbon emissions, number of vehicles, primary vehicle type

y = []
X = []
with open('dfc.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        try:
            if int(row[row_mapping[target_variable]]) > 0:
                val = int(row[row_mapping[target_variable]])
        except:
            continue
        _x = []
        good = True
        for i in range(len(input_variables)):
            
            v = input_variables[i]
            try:
                var = int(row[row_mapping[v]])
            except:
                var = -9
            if var < vmin[i]:
                if vmax[i] == 5:
                    if var in [-1,-9]:
                        var = 3
                    else:
                        good = False
                elif vmax[i] == 4:
                    if var == -1:
                        var = 0
                    else:
                        good = False
                else:
                    good = False
            elif var > vmax[i]:
                var = np.nan
                good = False
            _x.append(var)
        if good is True:
            X.append(_x)
            y.append(val)

X = np.array(X)
X = normalize(X, axis=0, norm='max')
y = np.array(y)
print(len(y))

#for i in range(len(y)):
#    print(X[i,8])
    
regr = linear_model.LinearRegression()
#regr = linear_model.Ridge()
#regr = linear_model.LogisticRegression(solver='liblinear',penalty='l1')
regr = linear_model.LogisticRegression()
regr.fit(X, y)

print(regr.coef_)
print(regr.score(X,y))

Z = regr.coef_
plt.figure(figsize=(8,10))
plt.imshow(Z,cmap='coolwarm',vmin=-2,vmax=2)
plt.xticks(range(11),['Age','Income','My primary vehicle is electric','I fear the battery is not sufficiently\ncharged when I want to start a trip',"I'm afraid the battery life could be shortened\nby the frequent charging and discharging",'V2G contributes to a stable electricity network for all','V2G allows me to use my EV\nfor back-up power for my home','V2G helps reduce my carbon emissions','V2G is as reliable as other charging technologies','I believe using V2G is very easy','I believe V2G can extend the EV battery life'],rotation=90)
plt.ylabel('Would you use V2G chargers?')
plt.yticks(range(5),['Definitely not','Unlikely','Neutral','Likely','Definitely'])
plt.tight_layout()
plt.show()