import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,2*np.pi,100)
R=1
P=theta-theta+R**2/4
plt.plot(theta,P)
plt.xlabel('\u03F4')
plt.ylabel('Pdf(\u03F4)')
plt.title('Pdf of \u03F4')
plt.show()
