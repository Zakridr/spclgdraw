import numpy as np
import scipy as sp
import math
import scipy.sparse as mlib
import scipy.sparse.linalg as lalib
# clustering algorithms
# make another file for sparsification algorithms?

# k is volbd
# graph is the matrix, in sparse form say?
# we could also parametrize over the bound... 
# O(n^2 log n) is pretty vague!

# this is the global alg, but only examines a single vertex
# graph is a matrix in scipy land
# v is coordinate of input vertex (a number)
# epsilon, bigC, littleC are floating controls for alg tuning
def kwok_lau(graph, v, k, epsilon, bigC, littleC):
    num_vertices = graph.shape[0]
    volbd = k * littleC
    p = [np.zeros(num_vertices, int)]
    p[0][v] = 1
    last = p[-1]
    
# length of walk to compute
# need to get W!
    I = mlib.identity(num_vertices, int)
# assuming symmetric here
    D = I.multiply(graph.dot(graph))
    lazy_walk = 0.5 * (I + lalib.inv(D) * graph)

    num_iterations = math.ceil(num_vertices ** 2 * math.log(num_vertices, 2))
    for t in range(1, num_iterations):
        p.append(last * lazy_walk)
        last = p[-1]

# value function for sorting:
    sortkey = lambda t: (lambda vertex: p[t][vertex] / D[v,v])

# initialize set now
    # S[0, 0] = []
    # outset = S[0,0]
    # outcond = conductance(outset)
    # for t in range(num_iterations):
# so#rt all at once here?
    #    for j in range(num_vertices):
    #        # find smallest S_{t,j}
    #        currcond = conductance(S[t,j])
    #        if (currcond < outcond and volume(S[t,j]) <= volbd):
    #            outset = S[t,j]
    #            outcond = currcond

#helper fcns
# conductance
# volume
# compute S_{t,j} somehow
# involves sorting

def conductance(csgraph):
    return None
