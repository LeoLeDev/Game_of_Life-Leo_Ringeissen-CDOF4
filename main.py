import random
import time
import os

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        print(" ".join(["#" if cell else "." for cell in row]))

def count_neighbors(grid, x, y):
    neighbors = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            neighbor_x, neighbor_y = x + i, y + j

            if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols:
                neighbors += grid[neighbor_x][neighbor_y]

    return neighbors

def update_grid(grid):
    new_grid = [row.copy() for row in grid]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbors = count_neighbors(grid, x, y)

            if grid[x][y] == 1:
                # Any live cell with fewer than two live neighbors dies
                # Any live cell with more than three live neighbors dies
                new_grid[x][y] = 0 if neighbors < 2 or neighbors > 3 else 1
            else:
                # Any dead cell with exactly three live neighbors becomes a live cell
                new_grid[x][y] = 1 if neighbors == 3 else 0

    return new_grid

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(rows, cols, generations, delay):
    grid = create_grid(rows, cols)

    for generation in range(generations):
        clear_screen()
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

if __name__ == "__main__":
    rows = 20
    cols = 40
    generations = 100
    delay = 0.1

    main(rows, cols, generations, delay)

    
