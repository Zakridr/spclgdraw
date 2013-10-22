import scipy, numpy, math
# clustering algorithms
# make another file for sparsification algorithms?

# k is volbd
# graph is the matrix, in sparse form say?
# we could also parametrize over the bound... 
# O(n^2 log n) is pretty vague!

# this is the global alg, but only examines a single vertex
def kwok_lau(graph, v, k, epsilon, bigC):
    num_vertices = graph.shape[0]
    volbd = k * c
# initialize p
# first value set to be zero everywhere except coord of v, where it's 1
    p = ['TODO']
    last = p[-1]
    num_iterations = num_vertices ** 2 * math.log(num_vertices, 2)
    for t in range(1, num_iterations):
        p.append(matrix_mult(W, last))
        last = p[-1]
    # ok, we have our p_ts now.
# initialize set now
    S[0, 0] = 'TODO'
    outset = S[0,0]
    outcond = conductance(outset)
    for t in range(num_iterations):
# sort all at once here?
        for j in range(num_vertices):
            # find smallest S_{t,j}
            currcond = conductance(S[t,j])
            if (currcond < outcond and volume(S[t,j]) <= volbd):
                outset = S[t,j]
                outcond = currcond

#helper fcns
# conductance
# volume
# compute S_{t,j} somehow
# involves sorting
