__author__ = 'justintaing'

import sys
import maze as m

if __name__ == "__main__":
    maze = m.Maze()
    output = ""

    maze.load_maze(sys.argv[1])
    print("Maze generated\n")
    maze.display_maze()

    print("\nEnter 1 for DFS")
    print("Enter 2 for BFS")
    mode = int(input("> "))

    verbose = input("Display verbose output? (y/n): ")
    verbose = True if verbose.lower() == 'y' else False

    try:
        if sys.argv[2]:
            output = sys.argv[2]
    except IndexError:
        pass

    if mode == 1:
        if maze.find_exit_path(verbose):
            print("Path found:")
            maze.print_exit_path(output)
        else:
            print("No path found")
    elif mode == 2:
        if maze.find_shortest_path(verbose):
            print("Path found:")
            maze.print_shortest_path(output)
        else:
            print("No path found")