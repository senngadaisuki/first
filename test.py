import numpy as np
import matplotlib.pyplot as plt

data = np.load('RAVEN_0_train.npz')
print(data['image'])
print(data['target'])
plt.figure(1)
for p in range(0,8):
    plt.subplot(3,3,p+1).imshow(data['image'][p])
#plt.subplot(3,3,2).imshow(data['image'][1])

plt.figure(2)
for p in range(0,8):
    plt.subplot(2,4,p+1).imshow(data['image'][p+8])

plt.show()