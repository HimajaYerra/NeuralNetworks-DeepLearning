import numpy as np

randvector = np.random.uniform(1,20,20)
matrix=randvector.reshape(4,5)
print(matrix)
maxvalues = np.amax(matrix,axis=1)
print(maxvalues)
result=np.where(np.isin(matrix,maxvalues),0,matrix)
print(result)
