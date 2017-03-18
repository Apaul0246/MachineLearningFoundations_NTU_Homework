'''
Python code - Naive PLA
Data: https://www.csie.ntu.edu.tw/~htlin/course/ml15fall/hw1/hw1_15_train.dat
Packages required: Numpy, Pandas
'''

import numpy as np
import pandas as pd

def read_data(path):

    df = pd.read_csv(path,sep='\s+',header=None)
    x0 = np.ones((len(df.index),1))
    df.insert(0,'x0',x0)
    return df
	
def PLA_naive(df):

	w0 = np.zeros((len(df.columns)-1))
	update = 0
	New_Y = np.zeros((len(df.index)))
	
	while (sum(New_Y != df.iloc[:,-1])>0):
		for i in range(len(df.index)):
			if sum(New_Y != df.iloc[:,-1])==0:
				print 'Best separating hyperplane found'
				print w0
				break 
			if New_Y[i] == df.iloc[:,-1][i]:
				pass
			else:
				w0 += np.dot(df.iloc[:,-1][i],df.iloc[i,:-1])
				New_Y = np.sign(np.dot(w0,df.iloc[:,:-1].T))
				update += 1
				print 'update %d times' %(update)
	return w0

df = read_data("C:\Users\user\OneDrive\Code\hw1_15_train.dat")
w = PLA_naive(df)
