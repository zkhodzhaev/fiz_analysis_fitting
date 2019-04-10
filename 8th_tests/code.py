#!/usr/bin/env python
# coding: utf-8
#Zulfidin Khodzhaev/ zulfidin@inbox.ru

# #for this to work, first 2 lines are deleted##because the number of column is less than number columns#######
# #Reading Grams weight
# #2019:4:3

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("ChocoWeightden8c.txt", delim_whitespace=True)

df.columns = ['time','weight','temp_inside','temp_top','pressure']

df = df.reset_index(drop=True)

df.time = pd.to_timedelta(df.time)

l_array=len(df)
time_array=np.arange(l_array)

n=0
for i in time_array:
    time_array[n]=datetime.timedelta.total_seconds(df.time[n]-df.time[0])
    n=n+1
    

time_array=pd.DataFrame(data=time_array)

df_array=pd.concat([time_array,df],axis=1)

df_array = df_array.drop("time", axis=1)

df_array.columns = ['time','weight','temp_inside','temp_top','pressure']



# create the plot space upon which to plot the data
fig, ax = plt.subplots(figsize = (8,8))
slope, intercept, r_value, p_value, std_err = stats.linregress(df_array.time,df_array['weight'])
line = slope*df_array.time+intercept

# add the x-axis and the y-axis to the plot
ax.plot(df_array.time, df_array['weight'],'o', label='original data')
ax.plot(df_array.time, line, label='$y=%.3fx + (%.2f$), [$R^2=%.2f$]' % (slope, intercept, r_value**2))

# rotate tick labels
plt.setp(ax.get_xticklabels(), rotation=45)


# set title and labels for axes
ax.set(xlabel="Time[s]",
       ylabel="Weight[g]",
       title="ChocoWeightden8c.txt");
ax.legend(loc='best')
plt.savefig('ChocoWeightden8c.png', dpi=600)



