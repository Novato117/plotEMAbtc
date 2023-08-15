import matplotlib.pyplot as plt
import pandas as pd 
import pandas_datareader.data as wb
import numpy as np


assets=['BTC-USD']
data=wb.DataReader(assets,'yahoo','2018-1-1')['Adj Close']


short_window=30
long_window=100

signal=pd.DataFrame(index=data.index)
#print(data.head())
signal['signals']=0

signal['short']=data.rolling(short_window).mean()
signal['long']=data.rolling(long_window).mean()

#signal['ewm_sort']=data.rolling(short_window).mean()
#signal['ewm_long']=data.rolling(long_window).mean()

signal['signals']=np.where(signal['short'] > signal['long'],1,0)
#signal['signal']=np.where(signal['ewm_short'] > signal['ewm_long'],1,0)

signal['positions']=signal['signals'].diff()#cuando se produc ele cruce

fig=plt.figure()
ax1=fig.add_subplot(111, ylabel='BTC/USD')

data.plot(ax=ax1,color='k',lw=1.2)
signal[['short','long']].plot(ax=ax1,lw=1.2)

ax1.plot(signal['short'][signal['positions']==1],'^',markersize=8,color='g')
ax1.plot(signal['short'][signal['positions']==-1],'v',markersize=8,color='r')

plt.title("cruce de medias")
plt.show()