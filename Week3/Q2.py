import numpy as np

#creates a vector of len 20 with float values ranging between 1-20
randvector = np.random.uniform(1,20,20)
#reshape the 1d vector into matrix
matrix=randvector.reshape(4,5)
print(matrix)
#list of max values along axis
maxvalues = np.amax(matrix,axis=1)
print(maxvalues)
#replaces values based on condition provided
result=np.where(np.isin(matrix,maxvalues),0,matrix)
print(result)
