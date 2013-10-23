import numpy as np
import scipy as sp
import scipy.sparse as sparse
import random
import cluster

SEED = 25
random.seed(SEED)

# so this is always the same matrix... 
# even when I didn't have that constant seed above.
# confused!
def rand_matrix(vertices, clusters, cprob, ncprob):
    curr_cluster = 1
    cluster_size = vertices // clusters
    def same_cluster(vi, vj):
        return (vi // cluster_size == vj // cluster_size)
    graph = [[0 for x in range(vertices)] for y in range(vertices)]
    p = 0
    for first in range(vertices):
        for second in range(first + 1, vertices):
            if same_cluster(first, second):
                p = cprob
            else:
                p = ncprob
            if random.random() <=  p:
                graph[first][second] = graph[second][first] = 1
    return graph

def is_graph(g):
    rows = len(g)
    cols = len(g[0])
    for i in range(rows):
        if len(g[i]) != cols:
            print("Fails on col consistency")
            return False
        for j in range(i, cols):
            if (g[i][j] != g[j][i] or (g[i][j] != 1 and g[i][j]
                                                      != 0)):
                print("fails on symmetry: row {0}, col {1}".format(i, j))
                return False
    return True

def raw2np(matrix):
    return sparse.lil_matrix(matrix)

v = 10
c = 2
cp= 1
ncp = 0
m = rand_matrix(v, c, cp, ncp)
#print("We had {0},\nand graph status is: {1}".format(m, is_graph(m)))
#
#spm = raw2np(m)

# ok, now we need to test other guy

graph = sparse.csc_matrix([[0, 0, 1], [0, 0, 1], [1, 1, 0]])
init_v = 0
k = 5
epsilon = 0.001
bigC = 1
littleC = 1
cluster.kwok_lau(graph, init_v, k, epsilon, bigC, littleC)

