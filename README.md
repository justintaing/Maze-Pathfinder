# Maze Pathfinder
Finds an exit path of a given maze using either DFS or BFS (for shortest path).

This is a python implementation of a data structures class project, originally written in C++.

# Input file structure
Maze files contain the size of the maze, coordinates for the start and exit points, and a set of columns for each row where the maze should have an open path.

The given `maze.txt` file produces the following maze:
```
############
# #####    #
#     # #  #
#s  # #    #
# # # # ## #
# # # # #  #
# ### # # ##
# #   # # ##
# # ### #  #
##      #  #
#    #### e#
############
```
With `s` for the starting point and `e` for the exit.

