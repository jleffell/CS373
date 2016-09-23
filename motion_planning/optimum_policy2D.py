# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]


init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):

    max_val = 999

    # index into value[theta][x][y]]
    value   = [[[max_val for row in range(len(grid[0]))] for col in range (len(grid))],
               [[max_val for row in range(len(grid[0]))] for col in range (len(grid))],
               [[max_val for row in range(len(grid[0]))] for col in range (len(grid))],
               [[max_val for row in range(len(grid[0]))] for col in range (len(grid))]]
    
    actions = [[[-1 for row in range(len(grid[0]))] for col in range (len(grid))],
               [[-1 for row in range(len(grid[0]))] for col in range (len(grid))],
               [[-1 for row in range(len(grid[0]))] for col in range (len(grid))],
               [[-1 for row in range(len(grid[0]))] for col in range (len(grid))]]
    
    policy  = [[' ' for row in range(len(grid[0]))] for col in range (len(grid))]

    change  = True

    while change:
        
        change = False
    
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for theta in range(len(forward)):
                    if goal[0] == x and goal[1] == y:
                            if value[theta][x][y] > 0:
                                value[theta][x][y] = 0
                                change = True

                    elif grid[x][y]==0:
                        
                        for a in range(len(action)):
                            theta2 = (theta + action[a])%len(forward)
                            x2     = x + forward[theta2][0]
                            y2     = y + forward[theta2][1]

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:

                                v2 = value[theta2][x2][y2] + cost[a]
                                
                                if v2 < value[theta][x][y]: 
                                    change = True
                                    value[theta][x][y]  = v2
                                    actions[theta][x][y] = a
    #
    # Follow Optimal Trajectory to Goal
    #

    x     = init[0]
    y     = init[1]
    theta = init[2]

    driving = True
    
    while driving:

        a = actions[theta][x][y]

        if a == -1:
            driving = False
            print "fail"
            return "fail"

        policy[x][y] = action_name[a]

        theta = (theta + action[a])%len(forward)
        x     = x + forward[theta][0]
        y     = y + forward[theta][1]
        
        if x == goal[0] and y == goal[1]:
            policy[x][y] = '*'
            driving = False

    for i in range(len(grid)):
        print policy[i]

optimum_policy2D(grid,init,goal,cost)
