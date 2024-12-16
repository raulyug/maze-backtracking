Maze Solver Project

📚 Project Overview

This project implements a basic maze-solving algorithm using depth-first search (DFS). The main function solve_maze(maze, start, end) finds a path from a starting point to an ending point in a maze represented as an adjacency list.

🧠 How It Works

Maze Representation: The maze is represented as a dictionary where keys are points in the maze and values are lists of adjacent points.

Algorithm: The algorithm performs a depth-first search (DFS), keeping track of visited points to avoid loops.

Path Tracking: The function maintains a list path representing the current path being explored.


🔧 How to Use

Define the Maze: Create a dictionary representing the maze.

Call the Function: Use solve_maze(maze, start, end) with the maze dictionary and the desired start and end points.

Get the Result: The function returns a list representing the path from start to end, if one exists.
