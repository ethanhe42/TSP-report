def optimize2opt(nodes, solution, number_of_nodes):
    best = 0
    best_move = None
    for ci in range(0, number_of_nodes):
        for xi in range(0, number_of_nodes):
            yi = (ci + 1) % number_of_nodes  
            zi = (xi + 1) % number_of_nodes 
            c = solution[ ci ]
            y = solution[ yi ]
            x = solution[ xi ]
            z = solution[ zi ]
            cy = length( c, y )
            xz = length( x, z )
            cx = length( c, x )
            yz = length( y, z )
            if xi != ci and xi != yi:
                gain = (cy + xz) - (cx + yz)
                if gain > best:
                    best_move = (ci,yi,xi,zi)
                    best = gain
    if best_move is not None:
        (ci,yi,xi,zi) = best_move
