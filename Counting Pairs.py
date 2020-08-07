a=[1,2,3,4,5,6,2]
k=2
a.sort()
n=len(a)
x=[]
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]+k==a[j]:
            x.append([a[i],a[j]])

#new_data = [list(y) for y in set([tuple(i)for i in x])]
#print(len((new_data)))
import numpy as np
x=np.asarray(x)
print(x)
new_data=np.unique(x, axis=0)
print(new_data)

