from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
  
fig = plt.figure() 
  
ax = fig.gca(projection ='3d') 
R=1 
# defining all 3 axes 
v = np.linspace(0, 1, 100) 
theta = np.linspace(0,2*np.pi,100)
z = 1-np.exp(-R**2/2)
  
# plotting 
ax.plot3D(v, theta, z, 'green') 
ax.set_title('CDF of V and \u03F4') 
ax.set_xlabel('v')
ax.set_ylabel('\u03F4')
plt.show() 