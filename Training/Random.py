import numpy as np 
# np.random.seed(123)
# np.random.rand()
# x = np.random.randint(low=4,high=8,size = (2,4))
# x = np.array(range(2,10,1)) #start,stop,step  
# print(x[-1])
x = [0]
counter = 50
for i in range(100) :
    counter = max(10,counter-i)
    x.append(counter)
import matplotlib.pyplot as plt
plt.plot(x)
plt.show()