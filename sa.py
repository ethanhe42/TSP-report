def step(nodes, solution, number_of_nodes, t):
    global nn
    ci = random.randint(0, number_of_nodes-1)
    yi = (ci + 1) % number_of_nodes
    xi = random.randint(0, number_of_nodes-1)
    zi = (xi + 1) % number_of_nodes
    if xi != ci and xi != yi:
        c = solution[ci]
        y = solution[yi]
        x = solution[xi]
        z = solution[zi]
        cy = length(c, y)
        xz = length(x, z)
        cx = length(c, x)
        yz = length(y, z)
        gain = (cy + xz) - (cx + yz)
        if gain < 0:
            u = math.exp( gain / t )
        elif gain > 0.05:
            u = 1
        else:
            u = 0 
        if (random.random() < u):
            nn = nn + 1
            new_solution = range(0,number_of_nodes)
            new_solution[0] = solution[ci]
            n = 1
            while xi != yi:
                new_solution[n] = solution[xi]
                n = n + 1
                xi = (xi-1)%number_of_nodes
            new_solution[n] = solution[yi]
            n = n + 1
            while zi != ci:
                new_solution[n] = solution[zi]
                n = n + 1
                zi = (zi+1)%number_of_nodes
            if anim:
                frame(nodes, new_solution, number_of_nodes, t, c, y, x, z, gain)

def sa_algorithm(nodes):
    number_of_nodes = len(nodes)
    solution = [n for n in nodes]
    t = 100
    l_min = total_length( nodes, solution )
    best_solution = []
    i = 0
    while t > 0.1:
        i = i + 1
        solution = step(nodes, solution, number_of_nodes, t)
        if i >= 200:
            i = 0
            l = total_length( nodes, solution )
            t = t*0.9995
            if l_min is None: 
                l_min = l
            elif l < l_min:
                l_min = l
                best_solution = solution[:]
            else:
                pass
    return best_solution
