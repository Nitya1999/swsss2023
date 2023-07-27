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
        nLines = 3                                 
    
        # Part 3:
        # read in data line by line, convert to numerical values  
        for line in f:
            tmp = line.split()
        
            #store variables to lists
            data['symh'].append(float(tmp[index]))
        
            datetime1 = dt.datetime(int(tmp[0]),1,1,int(tmp[2]),int(tmp[3])) + dt.timedelta(days=int(tmp[1])-1)
            data['time'].append(datetime1)
       
        time = np.array(data['time'])
        lp = (time>start_time)&(time<end_time)
        time_sel = time[lp]
        
        symh = np.array(data['symh'])
        symh_sel = symh[lp]
        
        data['symh'] = symh_sel
        data['data'] = time_sel
        return data
        
if __name__ == '__main__':
    filename = 'omniweb.gsfc.nasa.gov_staging_omni_min_def_aoOecEheHP.lst.txt'
    index = 4
    start_time = dt.datetime(2013, 3, 17) #assigning the start time
    end_time = dt.datetime(2013, 3, 21) #assigning the end time 
    
    file_data = (read_ascii_file_my(filename,index,start_time,end_time))
    fig = plt.figure()
    plt.plot(file_data['time'], file_data['symh'])
    plt.xlabel('time')
    plt.ylabel('symh (nT)')
    plt.title('')
    plt.show()
