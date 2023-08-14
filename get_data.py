import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime
import statistics

row_mapping = {}
with open('dfc.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for i in range(1,len(headers)):
        row_mapping[headers[i]] = i

def pull(question_id,evs_only=False,v2g_only=False,r_map=None):
    if question_id not in row_mapping:
        print('Invalid question ID')
        return None
    res = {}
    rown = row_mapping[question_id]
    with open('dfc.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if evs_only is True and (row[80] != '4' and row[96] != '4'):
                continue
            if v2g_only is True and row[3] != '4':
                continue
            if row[rown] == '':
                continue
            if r_map is None:
                ans = row[rown]
            else:
                if row[rown] not in r_map:
                    continue
                ans = r_map[row[rown]]
            if ans not in res:
                res[ans] = 0
            res[ans] += 1
    return res

def pull_demo(question_id,demo_id,demo_val):
    if question_id not in row_mapping:
        print('Invalid question ID')
        return None
    res = {}
    rown = row_mapping[question_id]
    demon = row_mapping[demo_id]
    with open('dfc.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[demon] != demo_val and row[demon] not in demo_val:
                continue
            if row[rown] == '':
                continue
            ans = row[rown]
            if ans not in res:
                res[ans] = 0
            res[ans] += 1
    return res

def pull_all(question_id):
    if question_id not in row_mapping:
        print('Invalid question ID')
        return None
    rown = row_mapping[question_id]
    res = []
    with open('dfc.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            res.append(row[rown])
    return res