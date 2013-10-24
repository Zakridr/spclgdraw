import numpy as np
import scipy as sp
import math
import scipy.sparse as mlib
import scipy.sparse.linalg as lalib
import scipy.sparse.csgraph as csglib
# clustering algorithms
# make another file for sparsification algorithms?

# k is volbd
# graph is the matrix, in sparse form say?
# we could also parametrize over the bound... 
# O(n^2 log n) is pretty vague!

# this is the global alg, but only examines a single vertex
# graph is a matrix in scipy land
# v is coordinate of input vertex (a number)
# epsilon, bigC, volbd_mult are floating controls for alg tuning
def kwok_lau(graph, v, k, epsilon, path_length_scaler, volbd_scaler):
    num_vertices = graph.shape[0]
    volbd = k * volbd_scaler
    vertices = list(range(num_vertices))
    print("N: {0}\nVolume bound: {1}\n".format(num_vertices, volbd))

    p = [np.zeros(num_vertices, int)]
    p[0][v] = 1
    last = p[-1]
    
# length of walk to compute
# need to get W!
    I = mlib.identity(num_vertices, int)
# assuming symmetric here
    L, D_vector = csglib.laplacian(graph, return_diag=True)
    D = mlib.diags(D_vector, (0), format='csc')

    lazy_walk = 0.5 * (I + lalib.inv(D) * graph)

    num_iterations = math.ceil(num_vertices ** 2 * math.log(num_vertices, 2))
    for t in range(1, num_iterations):
        p.append(last * lazy_walk)
        last = p[-1]

# value function for sorting:
    sortkey = lambda t: (lambda vertex: p[t][vertex] / D_vector[vertex])

# initialize set now
    S = dict()

    S[0,1] = p[0][v]
    outset = S[0,1]
# when S has one element, the conductance is 1
# conductance is <= 1
    outcond = 2
    for t in range(1, num_iterations):
# so#rt all at once here?
        p[t] = p[t-1] * lazy_walk
    
        for j in range(1, num_vertices):
# compute new S[t,j]
# don't want to include the entire graph, that's dumb...
# should also put another bound in here for later
            S[t,j] = computeS(sortkey(t), vertices, j, num_vertices)
            # find smallest S_{t,j}
            currcond = conductance(S[t,j], L, D)
            if (currcond < outcond and volume(S[t,j], D) <= volbd):
                outset = S[t,j]
                outcond = currcond
    return outset

#helper fcns
# conductance
# volume
# compute S_{t,j} somehow
# involves sorting

# computes conductance of S
# assume S is in np.array form
def conductance(chi_s, L, D):
    return (chi_s * L * chi_s).sum() / volume(chi_s, D)

def volume(chi_s, D):
    return (chi_s * D * chi_s).sum()

def computeS(keyfcn, vertex_list, size, nvertices):
    # sort vlist using keyfcn, in descending order
# get the first size many vertices in list
    #return the np array version corresponding to that set (chi it)
    vertex_list.sort(key=keyfcn, reverse=True)
    return set2vec(vertex_list[:size], nvertices)

def set2vec(S, length):
# length is the length of desired np array guy
    chiS = np.zeros(length)
    for s in S:
        chiS[s] = 1
    return chiS
