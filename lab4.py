#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_my_line(normal_vector,point_on_line):
    a=normal_vector[0]
    b=normal_vector[1]
    c=normal_vector[2]
    x_0=point_on_line[0]
    y_0=point_on_line[1]
    z_0=point_on_line[2]
    x=[]
    y=[]
    z=[]
    
    for t in range(-100,100):
        x.append(x_0+t*a)
        y.append(y_0+t*b)
        z.append(z_0+t*c)
    return (x,y,z)

def plane_point(plane,point):
    plane_normal=(plane[0],plane[1],plane[2])
    d= my_product(plane_normal,point) / my_length_function(plane_normal)
    
    t=-plane[3]-my_product(plane_normal,point)
    t=t/my_product(plane_normal,plane_normal)
    
    p_0=[0,0,0]
    p_0[0]=point[0]+t*plane[0]
    p_0[1]=point[1]+t*plane[1]
    p_0[2]=point[2]+t*plane[2]
    
    return d,t,p_0

def my_product(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def my_length_function(a):
    return my_product(a,a)**0.5

plane_1=[1,2,3,-6]
point_1=[4,2,10]
results = plane_point(plane_1,point_1)
a = [1,2,3]
b = [4,5,6]
my_product(a,b)
my_length_function(a)

get_ipython().run_line_magic('matplotlib', 'notebook')
xx, yy = np.meshgrid(range(10), range(10)) #5,5 büyüklüğünde bir meshgrid oluştur.
z1 = (-a[0]*xx - a[1]*yy -results[0])*1./a[2]
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='blue')
plt3d.scatter(point_1[0],point_1[1],point_1[2])
plt.show()


# In[ ]:




