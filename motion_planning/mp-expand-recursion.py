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

grid = [[0,1],
        [0,0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    ni = len(grid)
    nj = len(grid[0])

    close = [[0 for x in range(nj)] for y in range(ni)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            gij = grid[i][j]
            close[i][j]=gij

    olist = [[0,init[0],init[1]]]
    path = expand(olist,close,ni,nj)
    
    return path

def getList(current,close,ni,nj):
    
    nlist = []
    
    g = current[0]
    i = current[1]
    j = current[2]
    close[i][j]=1
    for n in range(len(delta)):
        coord = delta[n]
        it = i + coord[0]
        jt = j + coord[1]
        if it >=0 and it < ni and jt >=0 and jt < nj:
            if close[it][jt] == 0:
                nlist.append([g+cost,it,jt])
                close[it][jt] = 1
    return nlist

def expand(olist,close,ni,nj):
    
    if olist == []:
        print "fail"
        return "fail"
   
    olist.sort(key=lambda x: x[0])
    current = olist[0]
    if current[1] == goal[0] and current[2] == goal[1]:
        print "##### Search Successful: ",olist[0]
        return olist[0]
    else:
        nlist = getList(current,close,ni,nj)
        for l in range(len(nlist)):
            olist.append(nlist[l])
        olist.pop(0)
        expand(olist,close,ni,nj)

search(grid,init,goal,cost)
