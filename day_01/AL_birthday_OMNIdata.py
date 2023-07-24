import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1)
plt.plot(x, np.exp(x)) #plottling x vs the exponential of x
plt.xlabel('$0 \leq x < 1$') 
plt.ylabel('$e^x$')
plt.title('Exponential function')
plt.show()


from datetime import datetime

from swmfpy.web import get_omni_data

from matplotlib.pyplot import figure

start_time = datetime(1998, 10, 16) #assigning the start time as my birthday

end_time = datetime(1998, 10 , 17) #assigning the end time as the end of my birthday

data = get_omni_data(start_time, end_time) #getting data from OMNI

data.keys() #getting all the keys from the dictionary to find the AL values
al = data['al'] #getting the AL values during my birthday
times = data['times'] #getting the date and time values during my birthday

plt.plot(times, al) #plotting the AL during my birthday
plt.xlabel('date and time')#labeling the x-axis
plt.ylabel('AL') #labeling the y-axis
plt.title('AL during my birthday') #Giving a title to the plot
figure(figsize=(30,28), dpi=200)
plt.show()
