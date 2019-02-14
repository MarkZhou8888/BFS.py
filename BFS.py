import random
import pprint
def make_make(size, lvl, st):

    matrix = [[random.randint(0,10) for row in range(size)] for col in range(size)]

    for row in range(len(matrix)):
        for col in range(len(matrix)):

            if matrix[row][col] > lvl:
                matrix[row][col] = '.'
            else:
                matrix[row][col] = '|'
    x,y = st
    matrix[x][y] = "S"
    return matrix

def possible_paths(matrix, node):
    possible_paths = []
    #get x,y coordinates from node
    x = node[0]
    y = node[1]
    length = len(matrix)
    #check N,S,W,E,NE,NW,SE,SW
    for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1, y), (x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1):
        if x >= 0 and x < length and y >= 0 and y < length:
            #add to possible paths if the current direction is clear
            if matrix[x][y] == '.':
                possible_paths.append([x,y])
    return possible_paths

maze = make_make(5,2, [0,0])

def bfs(maze, node, goal):

    queue = [[node]]
    visited = []
    #while there are still unvisited paths
    while queue:
        path = queue.pop(0)
        node = path[-1]
        #if there is a new node
        if node not in visited:
            #add to list of visited
            visited.append(node)
            #get all possible paths from given node
            possible_paths_ = possible_paths(maze, node)
            #for every position in each possible path
            for position in possible_paths_:
                #keep track of position and path
                path_found = list(path)
                path_found.append(position)
                queue.append(path_found)
                #if the position is the goal
                if position == goal:
                    for x,y in path_found:
                        maze[x][y] = 'X'
                    return maze

    return ('no path found')
pprint.pprint(bfs(maze, (0,0), [4,4]))
