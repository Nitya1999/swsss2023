import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

def read_ascii_file_my(filename,index,starttime,endtime):
  
 data = {'time':[],
         'symh':[]}
 time = []
 symh = []
   
 with open(filename) as f:
    for line in f:
        print(line)                                 
    
        # Part 3:
        # read in data line by line, convert to numerical values  
        for line in f:
            tmp = line.split()
        
            #store variables to lists
            data['symh'].append(float(tmp[index]))
        
            datetime1 = dt.datetime(int(tmp[0]),1,1,int(tmp[2]),int(tmp[3])) + dt.timedelta(days=int(tmp[1])-1)
            data['time'].append(datetime1)
       
        time = np.array(data['time'])
        lp = (time>starttime)&(time<endtime)
        time_sel = time[lp]
        
        symh = np.array(data['symh'])
        symh_sel = symh[lp]
        
        data['symh'] = symh_sel
        data['time'] = time_sel
        return data
        
if __name__ == '__main__':
    filename = 'omniweb.gsfc.nasa.gov_staging_omni_min_3q8zspSDgQ.lst.txt'
    index = 4
    starttime = dt.datetime(2003,1,1) #assigning the start time
    endtime = dt.datetime(2013,12,31) #assigning the end time 
    
    file_data = (read_ascii_file_my(filename,index,starttime,endtime))
    fig = plt.figure()
    plt.plot(file_data['time'], file_data['symh'])
    plt.xlabel('time')
    plt.ylabel('symh (nT)')
    plt.title('')
    plt.show()
    
    storm_counter=0
    
    for s in file_data['symh']==-100:
        for s1 in file_data['symh']>-100:
            storm_counter = storm_counter+1
    print (storm_counter)
        
        
        