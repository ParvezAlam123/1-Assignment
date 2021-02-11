from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
  
fig = plt.figure() 
  
ax = plt.axes(projection ='3d') 
  
# defining all 3 axes 
v = np.linspace(0, 1, 100) 
theta = np.linspace(0,2*np.pi,100)
z = (1/(4*np.pi))*np.exp(-v/2)
  
# plotting 
ax.plot3D(v, theta, z, 'red') 
ax.set_title('PDF of V and \u03F4') 
ax.set_xlabel('v')
ax.set_ylabel('\u03F4')
plt.show() 