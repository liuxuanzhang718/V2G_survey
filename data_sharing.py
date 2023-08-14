import matplotlib.pyplot as plt
import numpy as np
import time, csv, datetime
import statistics

from get_data import pull


eq0901 = pull('EQ09_01')
eq0901_ev = pull('EQ09_01',evs_only=True)
eq0901_vg = pull('EQ09_01',v2g_only=True)

eq0902 = pull('EQ09_02')
eq0902_ev = pull('EQ09_02',evs_only=True)
eq0902_vg = pull('EQ09_02',v2g_only=True)

eq0903 = pull('EQ09_03')
eq0903_ev = pull('EQ09_03',evs_only=True)
eq0903_vg = pull('EQ09_03',v2g_only=True)

eq0904 = pull('EQ09_04')
eq0904_ev = pull('EQ09_04',evs_only=True)
eq0904_vg = pull('EQ09_04',v2g_only=True)

eq0905 = pull('EQ09_05')
eq0905_ev = pull('EQ09_05',evs_only=True)
eq0905_vg = pull('EQ09_05',v2g_only=True)

eq0906 = pull('EQ09_06')
eq0906_ev = pull('EQ09_06',evs_only=True)
eq0906_vg = pull('EQ09_06',v2g_only=True)

colors = ['#31688e','#35b779','#fde725']
fig,ax = plt.subplots(figsize=(7,4))
plt.bar(np.arange(6)-0.2,[(eq0901['1']+eq0901['2'])/(eq0901['1']+eq0901['2']+eq0901['-1']),
                          (eq0902['1']+eq0902['2'])/(eq0902['1']+eq0902['2']+eq0902['-1']),
                          (eq0903['1']+eq0903['2'])/(eq0903['1']+eq0903['2']+eq0903['-1']),
                          (eq0904['1']+eq0904['2'])/(eq0904['1']+eq0904['2']+eq0904['-1']),
                          (eq0905['1']+eq0905['2'])/(eq0905['1']+eq0905['2']+eq0905['-1']),
                          (eq0906['1']+eq0906['2'])/(eq0906['1']+eq0906['2']+eq0906['-1'])],width=0.2,color=colors[0],edgecolor='k',zorder=2,label='All surveyed')
plt.bar(np.arange(6)-0.2,[(eq0901['1'])/(eq0901['1']+eq0901['2']+eq0901['-1']),
                          (eq0902['1'])/(eq0902['1']+eq0902['2']+eq0902['-1']),
                          (eq0903['1'])/(eq0903['1']+eq0903['2']+eq0903['-1']),
                          (eq0904['1'])/(eq0904['1']+eq0904['2']+eq0904['-1']),
                          (eq0905['1'])/(eq0905['1']+eq0905['2']+eq0905['-1']),
                          (eq0906['1'])/(eq0906['1']+eq0906['2']+eq0906['-1'])],width=0.2,color=colors[0],edgecolor='k',zorder=2,hatch='//')
plt.bar(np.arange(6)-0.,[(eq0901_ev['1']+eq0901_ev['2'])/(eq0901_ev['1']+eq0901_ev['2']+eq0901_ev['-1']),
                          (eq0902_ev['1']+eq0902_ev['2'])/(eq0902_ev['1']+eq0902_ev['2']+eq0902_ev['-1']),
                          (eq0903_ev['1']+eq0903_ev['2'])/(eq0903_ev['1']+eq0903_ev['2']+eq0903_ev['-1']),
                          (eq0904_ev['1']+eq0904_ev['2'])/(eq0904_ev['1']+eq0904_ev['2']+eq0904_ev['-1']),
                          (eq0905_ev['1']+eq0905_ev['2'])/(eq0905_ev['1']+eq0905_ev['2']+eq0905_ev['-1']),
                          (eq0906_ev['1']+eq0906_ev['2'])/(eq0906_ev['1']+eq0906_ev['2']+eq0906_ev['-1'])],width=0.2,color=colors[1],edgecolor='k',zorder=2,label='EV owners')
plt.bar(np.arange(6)-0.,[(eq0901_ev['1'])/(eq0901_ev['1']+eq0901_ev['2']+eq0901_ev['-1']),
                          (eq0902_ev['1'])/(eq0902_ev['1']+eq0902_ev['2']+eq0902_ev['-1']),
                          (eq0903_ev['1'])/(eq0903_ev['1']+eq0903_ev['2']+eq0903_ev['-1']),
                          (eq0904_ev['1'])/(eq0904_ev['1']+eq0904_ev['2']+eq0904_ev['-1']),
                          (eq0905_ev['1'])/(eq0905_ev['1']+eq0905_ev['2']+eq0905_ev['-1']),
                          (eq0906_ev['1'])/(eq0906_ev['1']+eq0906_ev['2']+eq0906_ev['-1'])],width=0.2,color=colors[1],edgecolor='k',hatch='//',zorder=2)
plt.bar(np.arange(6)+0.2,[(eq0901_vg['1']+eq0901_vg['2'])/(eq0901_vg['1']+eq0901_vg['2']+eq0901_vg['-1']),
                          (eq0902_vg['1']+eq0902_vg['2'])/(eq0902_vg['1']+eq0902_vg['2']+eq0902_vg['-1']),
                          (eq0903_vg['1']+eq0903_vg['2'])/(eq0903_vg['1']+eq0903_vg['2']+eq0903_vg['-1']),
                          (eq0904_vg['1']+eq0904_vg['2'])/(eq0904_vg['1']+eq0904_vg['2']+eq0904_vg['-1']),
                          (eq0905_vg['1']+eq0905_vg['2'])/(eq0905_vg['1']+eq0905_vg['2']+eq0905_vg['-1']),
                          (eq0906_vg['1']+eq0906_vg['2'])/(eq0906_vg['1']+eq0906_vg['2']+eq0906_vg['-1'])],width=0.2,color=colors[2],edgecolor='k',zorder=2,label='V2G participants')
plt.bar(np.arange(6)+0.2,[(eq0901_vg['1'])/(eq0901_vg['1']+eq0901_vg['2']+eq0901_vg['-1']),
                          (eq0902_vg['1'])/(eq0902_vg['1']+eq0902_vg['2']+eq0902_vg['-1']),
                          (eq0903_vg['1'])/(eq0903_vg['1']+eq0903_vg['2']+eq0903_vg['-1']),
                          (eq0904_vg['1'])/(eq0904_vg['1']+eq0904_vg['2']+eq0904_vg['-1']),
                          (eq0905_vg['1'])/(eq0905_vg['1']+eq0905_vg['2']+eq0905_vg['-1']),
                          (eq0906_vg['1'])/(eq0906_vg['1']+eq0906_vg['2']+eq0906_vg['-1'])],width=0.2,color=colors[2],edgecolor='k',hatch='//',zorder=2)
plt.xticks(range(6),['Vehicle\n location','Mobile phone\n location','Charging\n locations','State of\n charge','Departure and\n arrival times','Daily\nmileage'],rotation=0)
plt.yticks([0,0.2,0.4,0.6,0.8,1.],[0,20,40,60,80,100])
plt.ylabel('Percent willing to share information')
plt.grid(zorder=0,axis='y')
plt.legend()
plt.tight_layout()

p = plt.Rectangle((3.53, 0.83), 1.9, 0.13, fill=False,edgecolor='silver')
ax.add_patch(p)
p2 = plt.Rectangle((3.6, 0.85), 0.27, 0.0275, fill=False,edgecolor='k')
ax.text(3.99,0.85,'Provider only')
ax.add_patch(p2)
p3 = plt.Rectangle((3.6, 0.91), 0.27, 0.0275, fill=False,edgecolor='k',hatch='//')
ax.text(3.99,0.91,'Provider + partners')
ax.add_patch(p3)
plt.show()