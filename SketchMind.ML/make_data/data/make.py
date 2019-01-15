import numpy as np
import matplotlib.pyplot as plt
import math



def drawArrow1(A, B,name):
    ax = plt.axes()
    ax.arrow(A[0],A[1],B[0],B[1], width=0.05,head_width=0.2, head_length=0.2, fc='k', ec='k')
    plt.axis('off')
    # plt.show()
    plt.savefig(name, dpi=10)
    plt.close()
    # plt.savefig('data/test1.png', dpi=20) 

def get_8_direction():
    # B=np.array()
    temp = []
    a = []
    b = []
    for i in range(8):
        temp = [[0.5-0.3*math.cos(i*3.1415926/4),0.5-0.3*math.sin(i*3.1415926/4)],[0.6*math.cos(i*3.1415926/4),0.6*math.sin(i*3.1415926/4)]]
        a = temp[0]
        b = temp[1]
        name='data/test'+str(i)+'.png'
        drawArrow1(a,b,name)
        
            
        
#%%

get_8_direction()


