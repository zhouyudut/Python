# /usr/bin/env python2
# -×- coding: utf8 -×-
import Tkinter
import numpy as np
import matplotlib.pyplot as plt
x1=[1,2,3,4,5,6,7,8,9,10]
y1=[2.498,1.867,1.787,1.914,1.834,1.877,1.716,1.919,1.864,1.858]
x2=[1,2,3,4,5,6,7,8,9,10]
y2=[0.963,0.767,0.733,0.709,0.755,0.717,0.707,0.701,0.713,0.697]
plt.title('prime')
plt.xlabel('process numbers')
plt.ylabel('time(s)')
plt.plot(x1,y1,'r',label='m1')
plt.plot(x2,y2,'b',label='m2')
plt.legend(bbox_to_anchor=[0.3,1])
plt.grid()
plt.show()
# 不同虚拟化场景下的benchmark性能损耗
