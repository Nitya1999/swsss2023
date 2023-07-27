"""
author: Nitya Agarwala
email: nityaagarwala@yahoo.in

"""

import netCDF4 as nc
import matplotlib.pyplot as plt

def plot_tec(dataset, figsize=(12,6)):
    
    """ 
        Defining a function to plot the total electron content (TEC) 
        n from the WAM-IPE model forecast  on the Space Weather Prediction 
        Center website
    
       dataset: this is a netCDF file containing space weather data on
       25th July 2023
       
    """

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=figsize) 
    
   
    lat = dataset['lat'] #getting the latitude data from teh dataset
    lon = dataset['lon'] #getting the longitude data from teh dataset
    tec = dataset['tec'] #getting the tec data from teh dataset
    
    plt.pcolormesh(lon, lat, tec) #using colormesh to make the plot
    cbar = plt.colorbar() #getting a colorbar
    cbar.ax.set_ylabel(str('tecU')) #giving a title to the color bar
    
    return fig, ax

def save_figure(dataset_name):
    
    """
        defining a function of save plots in png format
    
    """
    dataset = nc.Dataset(dataset_name)
    plot_tec(dataset)
    filename = dataset_name + '.png'
    plt.savefig(filename, format = 'png')  
    
if __name__ == '__main__':
    dataset = nc.Dataset("wfs.t06z.ipe05.20230725_052000.nc")
    plot_tec(dataset)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Contour plot of Total electron content (TEC)')
    plt.show() #plotting the data'
    
    dataset_name = "wfs.t06z.ipe05.20230725_052000.nc"
    save_figure(dataset_name)
    
   
    
   
    
   
    
   
    
   
    
   
    
    
   #dataset = nc.Dataset("wfs.t06z.ipe05.20230725_052000.nc") 
   #plot_NmF2(dataset)
   #plt.xlabel('Latitude')
   #plt.ylabel('Longitude')
   #plt.title('Contour plot NmF2')
   #plt.show() #plotting the data
    
   #dataset = nc.Dataset("wfs.t06z.ipe05.20230725_052000.nc") 
   #plot_HmF2(dataset)
   #plt.xlabel('Latitude')
   #plt.ylabel('Longitude')
   #plt.title('Contour plot of HmF2')
   #plt.show() #plotting the data
   
  #def plot_NmF2(dataset, figsize=(12,6)):
       
      #fig, ax = plt.subplots(nrows=1,ncols=1,figsize=figsize) 
       
      
       #lat = dataset['lat'] #getting the latitude data from teh dataset
       #lon = dataset['lon'] #getting the longitude data from teh dataset
       #NmF2 = dataset['NmF2']
      
       #plt.pcolormesh(lon, lat, NmF2) #using colormesh to make the plot
       #cbar = plt.colorbar() #getting a colorbar
       #cbar.ax.set_ylabel(str('tecU')) #giving a title to the color bar 

       #return fig, ax

   #def plot_HmF2(dataset, figsize=(12,6)):
       
       #fig, ax = plt.subplots(nrows=1,ncols=1,figsize=figsize) 
       
      
       #lat = dataset['lat'] #getting the latitude data from teh dataset
       #lon = dataset['lon'] #getting the longitude data from teh dataset
       #HmF2 = dataset['HmF2']
      
       #plt.pcolormesh(lon, lat, HmF2) #using colormesh to make the plot
       #cbar = plt.colorbar() #getting a colorbar
       #cbar.ax.set_ylabel(str('tecU')) #giving a title to the color bar 

      # return fig, ax