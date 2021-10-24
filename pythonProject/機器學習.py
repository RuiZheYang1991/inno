import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# print("導入權重(w)和偏權值(bias)")
# def AND(x1 , x2):
#     x=np.array([x1,x2])
#     w= np.array([0.5,0.5])
#     b = -0.7
#
#     tmp =  np.sum(w * x) +b
#     print(tmp)
#     if tmp <=0 :
#         return 0
#     elif tmp > 0:
#         return 1
#
# print(AND(0,0))
# print(AND(0,1))
# print(AND(1,1))
# print(AND(1,0))



# def step_function(x):#階梯
#     return np.array(x>0,dtype=np.int)
#
# x=np.arange(-5.0,5.0,0.1)
# y = step_function(x)
# print(y)
#
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()

# import math
# import matplotlib.pyplot as plt
#
# x=[]
# dx=-20
# while dx <=20:
#     x.append(dx)
#     dx+=0.1
#
# def sigmoid(x):
#     return 1/(1+math.exp(-x))
#
# px = [xv for xv in x]
# py = [sigmoid(xv) for  xv  in x]
#
# plt.plot(px,py)
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))
# plt.show()

# def relu(x):
#     return np.maximum(0,x)
#
# x=np.arange(-5.0,5.0,0.1)
# y=relu(x)
# print(y)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()




# print(W1.shape)
# print(X.shape)
# print()

#建構三層網絡
# import math
# import numpy as np
#
# def sigmoid(x):
#     return 1/(1+np.exp(-x))
#
# X=np.array([1.0,0.5])
# W = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
# B1 = np.array([0.1,0.2,0.3])
#
# A1 = X.dot(W) + B1
# Z1 = sigmoid(A1)
# print(A1)
# print(Z1)
#
# W2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
# B2=np.array([0.1,0.2])
# print(Z1.shape)
# print(W.shape)
# print(B1.shape)
#
# A2 = np.dot(Z1,W2) +B2
# Z2=sigmoid(A2)
# print("A2")
# print(A2)
# print("Z2")
# print(Z2)
#
#
# def identity_function(x):
#     return x
# W3 = np.array([[0.1,0.3],[0.2,0.4]])
# B3 = np.array([0.1,0.2])
#
# A3= np.dot(Z2,W3)+B3
# Y=identity_function(A3)
# print("Y")
# print(Y)


#整合三層網絡

import math
import numpy as np
def identity_function(x):
    return x
def sigmoid(x):
    return 1/(1+np.exp(-x))
def init_network():
    network={}
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([0.1, 0.2,0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1,0.2])
    return network


def forward(network,x):
    W1,W2,W3=network['W1'],network['W2'],network['W3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']
    a1 = np.dot(x,W1) +b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) +b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3)+b3

    y = identity_function(a3)
    return y

network=init_network()
x= np.array([1.0,0.5])
y = forward(network,x)
print(y)



