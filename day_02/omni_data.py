import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import sys

f = open ("omniweb.gsfc.nasa.gov_staging_omni_min_def_aoOecEheHP.lst.txt")
line = f.readline()
f.close()

with open("omniweb.gsfc.nasa.gov_staging_omni_min_def_aoOecEheHP.lst.txt") as f:
        for line in f:
            print(line)
nLines = 3                                 
with open("omniweb.gsfc.nasa.gov_staging_omni_min_def_aoOecEheHP.lst.txt") as f:
    
    year= []
    day= []
    hour= []
    minute= []
    symh= []
    times= []
    
    # Part 1:
    # skip lines 1-3
    for i in range(nLines):
        print(f.readline())
    
    # Part 2: 
    # read line 4: read in variables line and 
    # convert to variable names 
    header = f.readline() 
    vars = header.split()
    print(vars)
    
    # Part 3:
    # read in data line by line, convert to numerical values  
    for line in f:
        tmp = line.split()
        
        #store variables to lists
        year.append(int(tmp[0]))
        day.append(int(tmp[1]))
        hour.append(int(tmp[2]))
        minute.append(int(tmp[3]))
        symh.append(int(tmp[4]))
        
        datetime1 = dt.datetime(int(tmp[0]),1,1,int(tmp[2]),int(tmp[3])) + dt.timedelta(days=int(tmp[1])-1)
        print(datetime1)
        times.append(datetime1)
        #sys.exit('check')
        
print(hour)
print(minute)

plt.plot(times, symh)
plt.xlabel('time')
plt.ylabel('symh (nT)')
plt.title('Geomagnetic storm on 17th March 2013')
plt.show()


    
    

        