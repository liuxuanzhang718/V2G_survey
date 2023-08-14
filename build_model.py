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
        
    
def corr(x,y,num_v,v_min,v_max):
    v1 = num_v[x]
    v2 = num_v[y]

    _x = []
    _y = []
    with open('dfc.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            try:
                var1 = int(row[row_mapping[v1]])
            except:
                var1 = -9
            try:
                var2 = int(row[row_mapping[v2]])
            except:
                var2 = -9
            if var1 < v_min[v1] or var1 > v_max[v1]:
                continue
            if var2 < v_min[v2] or var2 > v_max[v2]:
                continue
            _x.append(var1)
            _y.append(var2)
        return np.corrcoef(_x,_y)[0,1]
        
def score(input_variables,target_variable,v_min,v_max,avs,keep_bad=False):
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
                if var < v_min[v]:
                    if v_max[v] == 5 and v_min[v] == 1:
                        if var in [-1,-9]:
                            var = 3
                        else:
                            var = avs[v]
                            good = False
                    elif v == 'PI20':
                        if var == -1:
                            var = 0
                        else:
                            var = avs[v]
                            good = False
                    else:
                        var = avs[v]
                        good = False
                elif var > v_max[v]:
                    var = avs[v]
                    good = False
                _x.append(var)
            if keep_bad is True or good is True:
                X.append(_x)
                y.append(val)
                
    X = np.array(X)
    X = normalize(X, axis=0, norm='max')
    y = np.array(y)

    regr = linear_model.LinearRegression()
    regr = linear_model.LogisticRegression(solver='liblinear')
    regr = linear_model.LogisticRegression(solver='liblinear',penalty='l1')
    #regr = linear_model.Ridge()
    regr.fit(X, y)

    return regr.score(X,y), regr.coef_

def score_within1(input_variables,target_variable,v_min,v_max,avs,keep_bad=False):
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
                if var < v_min[v]:
                    if v_max[v] == 5 and v_min[v] == 1:
                        if var in [-1,-9]:
                            var = 3
                        else:
                            var = avs[v]
                            good = False
                    elif v == 'PI20':
                        if var == -1:
                            var = 0
                        else:
                            var = avs[v]
                            good = False
                    else:
                        var = avs[v]
                        good = False
                elif var > v_max[v]:
                    var = avs[v]
                    good = False
                _x.append(var)
            if keep_bad is True or good is True:
                X.append(_x)
                y.append(val)
                
    X = np.array(X)
    X = normalize(X, axis=0, norm='max')
    y = np.array(y)

    regr = linear_model.LogisticRegression(solver='liblinear',penalty='l1')
    regr.fit(X, y)
    
    y0 = regr.predict(X)
    
    correct = 0
    within1 = 0
    wrong = 0
    for i in range(len(y)):
        if y0[i] == y[i]:
            correct += 1
        elif abs(y0[i]-y[i]) == 1:
            within1 += 1
        else:
            wrong += 1
    
    return (correct+within1)/(correct+within1+wrong)
