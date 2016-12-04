def greedy_algorithm(nodes):
    free_nodes = nodes[:]
    solution = []
    n = free_nodes[0]
    free_nodes.remove(n)
    solution.append( n )
    while len(free_nodes) > 0:
        min_l = None
        min_n = None
        for c in free_nodes:
            l = length( c, n )
            if min_l is None:
                min_l = l
                min_n = c
            elif l < min_l:
                min_l = l
                min_n = c
        solution.append(min_n)
        free_nodes.remove(min_n)
        n = min_n
    return solution
