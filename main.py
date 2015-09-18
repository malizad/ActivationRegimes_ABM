import random
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import stats
import powerlaw
import plfit
from collections import deque


# In[2]:

mu = 0.3 # constriction factor used to limit the convergence velocity
delta = 1 # intolerance threshold 
max_iter = 600000 # maximum number of iteration at each run
no_of_agents = 1000
U = 0.2 # level of uncertainty
epsilon = 0.05


"""
Defining the psign function.
"""
def psign (x):
    if x >= 0:
        x = 1
    else:
        x = -1
    return x

# Defining the init method: a special method that gets invoked when an object is instantiated
def init():
    global op1, op2
    #random.seed(1)
    op1 = [(-1 + 2 * random.random()) for agents in range(no_of_agents)]
    #random.seed(2)
    op2 = [(-1 + 2 * random.random()) for agents in range(no_of_agents)]


"""
Compute Number of Extremists
"""
def CompNoExtremists():
    extreme1 = 0
    extreme2 = 0
    for opinion1 in range(len(op1)):
        if abs(op1[opinion1]) >= 0.9:
            extreme1 += 1
    for opinion2 in range(len(op2)):
        if abs(op2[opinion2]) >= 0.9:
            extreme2 += 1
    NoExtremists = extreme1 + extreme2
    return NoExtremists


"""
Main
"""
cmat = np.zeros([9,30])
emat = np.zeros([9,30])
smat = np.zeros([9,30])
mmat = np.zeros([9,30])

delta = [1,1.5,2]
U = [0.2,0.3,0.4]
#d=1
#u=0.2
z=0
for d in delta:
    for u in U:
        clist =list()
        elist = list()
        slist = list()
        mlist = list()
        for i in range(1): 
            init()    
            #Interact(d,u)
            #UniAct(d,u)
            PoisAct(d,u)
            clust, minor = CompNoClusters()
            clist.append(len(clust))
            mlist.append(minor)
            maxsize = max(clust)
            slist.append(maxsize)
            extr = CompNoExtremists()
            elist.append(extr)
        cmat[z]=clist
        emat[z]=elist
        smat[z]=slist
        mmat[z]=mlist
        z +=1

np.savetxt("RndE.txt",emat,delimiter="\t")
np.savetxt("RndC.txt",cmat,delimiter='\t')
np.savetxt("RndS.txt",smat,delimiter='\t')
np.savetxt("RndM.txt",mmat,delimiter='\t')


    
  
plt.plot(op1, op2, 'ro')
plt.xlabel('Opinion 1',fontsize=18)
plt.ylabel('Opinion 2',fontsize=18)
plt.show() 


# In[11]:

init()
UniAct(1,0.2)
plt.plot(op1, op2, 'ro')
plt.xlabel('Opinion 1',fontsize=18)
plt.ylabel('Opinion 2',fontsize=18)
plt.show() 


# In[12]:

nl, ns = stats.norm.fit(op1)
x=np.linspace(-2,2,100)
pdf_fitted = stats.norm.pdf(x, nl, ns)
plot(x,pdf_fitted,'g-',label='Normal')
hist(op1,normed=True,alpha=0.3)
xlabel('Opinion1',fontsize=18)
ylabel('PDF',fontsize=18)
legend(loc='upper right')
