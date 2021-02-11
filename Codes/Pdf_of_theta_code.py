import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,2*np.pi,100)
R=1
P=theta-theta+(1/(2*np.pi))*(1-np.exp(-R**2/2))
plt.plot(theta,P)
plt.xlabel('\u03F4')
plt.ylabel('Pdf(\u03F4)')
plt.title('Pdf of \u03F4')
plt.show()
