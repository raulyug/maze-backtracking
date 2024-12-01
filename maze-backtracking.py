def solve_maze (maze, start, end):
    path=[]
    visited = []
    
    path.append(start)
    currentPoint = start
    visited.append(currentPoint)
    
    while path[-1] != end and len(path) > 0:
        iter_obj = iter (maze[currentPoint])
        foundOutlet=False
        
        try:
            while not foundOutlet and iter != (len(maze)-1):
                next_point = next(iter_obj)
                if next_point not in visited:
                    foundOutlet = True
        except StopIteration: 
            break
        
        if foundOutlet:
            path.append(next_point)
            visited.append(next_point)
            currentPoint = next_point
        else:
            path.pop()
            currentPoint = path[-1]
    return path

