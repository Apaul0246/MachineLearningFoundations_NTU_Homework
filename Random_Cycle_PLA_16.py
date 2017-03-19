'''
Python code - Naive PLA by visiting examples in fixed pre-determined random cycles
Data: https://www.csie.ntu.edu.tw/~htlin/course/ml15fall/hw1/hw1_15_train.dat
Packages required: Numpy, Pandas
'''

import numpy as np
import pandas as pd
import seaborn as sns

def read_data(path):
    df = pd.read_csv(path,sep='\s+',header=None)
    x0 = np.ones((len(df.index),1))
    df.insert(0,'x0',x0)
    return df

def PLA_naive(df,eta):

	w0 = np.zeros((len(df.columns)-1))
	update = 0
	New_Y = np.zeros((len(df.index)))
	
	dataindex = list(range(len(df.index)))
	np.random.shuffle(dataindex)

	while (sum(New_Y != df.iloc[:,-1])>0):
		for i in range(len(df.index)):
			if sum(New_Y != df.iloc[:,-1]) == 0:
				break 
			if New_Y[dataindex[i]] == df.iloc[:,-1][dataindex[i]]:
				pass
			else:
				w0 += eta*np.dot(df.iloc[:,-1][dataindex[i]],df.iloc[dataindex[i],:-1])
				New_Y = np.sign(np.dot(w0,df.iloc[:,:-1].T))
				update += 1
	return update,w0

def run_PLA(df,t):
	update_set = []
	w_set = []
	for i in range(t):
		update,w = PLA_naive(df,0.5)
		update_set.append(update)
		w_set.append(w)
	sns.distplot(update_set)
	sns.plt.show()
	print np.average(update_set)

df = read_data("C:\Users\user\OneDrive\Code\hw1_15_train.dat")
run_PLA(df,2000)