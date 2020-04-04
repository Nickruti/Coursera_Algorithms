# PACKAGE
# Here are the imports again, just in case you need them.
# There is no need to edit or submit this cell.
import numpy as np
import numpy.linalg as la
from readonly.PageRankFunctions import *
np.set_printoptions(suppress=True)

def pageRank(linkMatrix, d) :
    n = linkMatrix.shape[0]
    M = d * linkMatrix + (1-d)/n * np.ones([n,n])
    r = 100 * np.ones(n)/n
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR-r)>0.01:
        lastR = r
        r = M @ r
        i+=1
    
    return r

# Use the following function to generate internets of different sizes.
generate_internet(5)
L = generate_internet(10)

pageRank(L, 1)

eVals, eVecs = la.eig(L) # Gets the eigenvalues and vectors
order = np.absolute(eVals).argsort()[::-1] # Orders them by their eigenvalues
eVals = eVals[order]
eVecs = eVecs[:,order]

r = eVecs[:, 0]

%pylab notebook
r = pageRank(generate_internet(100), 0.9)
plt.bar(arange(r.shape[0]), r);
100 * np.real(r / np.sum(r))

