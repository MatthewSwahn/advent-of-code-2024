import numpy as np

arr = np.random.rand(5)
print(arr)
for i in np.arange(len(arr)):
    print(np.delete(arr,i))