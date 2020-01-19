# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:04:28 2020

@author: Dell
"""

"""Amonng the propositions supplied we only select those propositions which correspond to our conclusion
A=I am a human being.
B=I am good.
C=Good graders study well.
D=Humans love graders.
E=Every human does not study well.
"""

from sympy import*
from sympy.abc import P,Q,R,S,T,U,V,W
P='Every Human'
Q='Good Graders'
R='Study Well'
l=[]
P=[True,True,True,True,False,False,False,False]
Q=[True,True,False,False,True,True,False,False]
R=[True,False,True,False,True,False,True,False]
S=[]
T=[]
U=[]
V=[]
W=[]
for i in range(8):
    S.append(Implies(Q[i],R[i]))#Good graders study well

for i in range(8):
    T.append(P[i] and not(R[(i)]))#Every human does not study well

for i in range(8):
    U.append((S[i] and T[i]))

for i in range(8):
    V.append(P[i] and Q[i])#Conclusion:Every human is a good grader

for i in range(8):
    W.append(Implies(U[i],V[i]))


for i in W:
    if(i==False):
        print('No')
    else:
        continue


