import matplotlib.pyplot as plt
import numpy as np
v=np.linspace(0,1,100)
P=(1/2)*np.exp(-v/2)
plt.plot(v,P)
plt.xlabel('v')
plt.ylabel('P(v)')
plt.title('Pdf of V')
plt.show()
