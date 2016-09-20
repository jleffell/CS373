# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

#grid = [[0,1],
#        [0,0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
 
    nx = len(grid)
    ny = len(grid[0])

    found  = False
    failed = False

    # close = [[0 for x in range(nj)] for y in range(ni)]

    # Initialize the closed list with the blocked cells
    close = grid[:]

    # Initialize The Open List
    open_list = [[0,init[0],init[1]]]

    while (not found and not failed):

        if open_list == []:
            print "fail"
            failed = True
            return "fail"
        else:

            # Expand coordinate with lowest g-value
            open_list.sort(key=lambda x: x[0])
        
            current = open_list.pop(0)
            g = current[0]
            x = current[1]
            y = current[2]
            close[x][y] = 1

            if x == goal[0] and y == goal[1]:
                print "##### Search Successful: ",current
                found = True
                return current
            else:
                new_list = []

                for n in range(len(delta)):
                    coord = delta[n]
                    xtry = x + coord[0]
                    ytry = y + coord[1]
                    if xtry >=0 and xtry < nx and ytry >=0 and ytry < ny:
                        if close[xtry][ytry] == 0:
                            new_list.append([g+cost,xtry,ytry])
                            close[xtry][ytry] = 1

                for l in range(len(new_list)):
                    open_list.append(new_list[l])

search(grid,init,goal,cost)
