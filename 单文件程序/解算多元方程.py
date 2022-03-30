import numpy as np
x=[0.4,0.5,0.8,1.0,2]
y=[  2, 15, 10, 12,4]
l=[]
for j in range(len(x)):
    i=x[j]
    print(j,i)
    l.append([i**4,i**3,i**2,i,1])
    
a=np.mat(l)
b=np.mat(y).T
print('a',a)
print('b',b)
c=np.linalg.solve(a,b)
print(c)
