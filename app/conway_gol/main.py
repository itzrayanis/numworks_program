# GAME OF LIFE

import kandinsky
import time
import random
import ion

WIDTH = 320
HEIGHT = 222
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

def create_empty_grid():
    return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

grid = create_empty_grid()

cursor_x = GRID_WIDTH // 2
cursor_y = GRID_HEIGHT // 2

auto_mode = False

def clear_screen():
    kandinsky.fill_rect(0, 0, WIDTH, HEIGHT, (255, 255, 255))

def draw_cell(x, y, alive):
    color = (0,0,0) if alive else (255,255,255)
    kandinsky.fill_rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE, color)

def draw_cursor(x, y):
    # Draw cursor as a red outline
    kandinsky.fill_rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, 1, (255,0,0)) # Top edge
    kandinsky.fill_rect(x * CELL_SIZE, y * CELL_SIZE + CELL_SIZE - 1, CELL_SIZE, 1, (255,0,0)) # Bottom edge
    kandinsky.fill_rect(x * CELL_SIZE, y * CELL_SIZE, 1, CELL_SIZE, (255,0,0)) # Left edge
    kandinsky.fill_rect(x * CELL_SIZE + CELL_SIZE - 1, y * CELL_SIZE, 1, CELL_SIZE, (255,0,0)) # Right edge

def display_grid(with_cursor=True):
    # Redraw the whole grid, cells, and optionally cursor
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            draw_cell(x, y, grid[y][x])
    if with_cursor:
        draw_cursor(cursor_x, cursor_y)

def initialize_grid():
    global grid
    grid = create_empty_grid()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid[y][x] = random.randint(0, 1)

def count_neighbors(x, y, ref_grid):
    neighbors = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx + GRID_WIDTH) % GRID_WIDTH
            ny = (y + dy + GRID_HEIGHT) % GRID_HEIGHT
            neighbors += ref_grid[ny][nx]
    return neighbors

def next_generation():
    global grid
    old_grid = [row[:] for row in grid]  # Deep copy
    new_grid = create_empty_grid()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            n = count_neighbors(x, y, old_grid)
            if old_grid[y][x]:
                if n == 2 or n == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
            else:
                if n == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
    grid = new_grid

# Always redraw the whole grid on any update to avoid display conflicts
display_grid()
while True:
    prev_cursor_x, prev_cursor_y = cursor_x, cursor_y
    updated = False

    if ion.keydown(ion.KEY_LEFT) and cursor_x > 0:
        cursor_x -= 1
        updated = True
        time.sleep(0.07)
    if ion.keydown(ion.KEY_RIGHT) and cursor_x < GRID_WIDTH-1:
        cursor_x += 1
        updated = True
        time.sleep(0.07)
    if ion.keydown(ion.KEY_UP) and cursor_y > 0:
        cursor_y -= 1
        updated = True
        time.sleep(0.07)
    if ion.keydown(ion.KEY_DOWN) and cursor_y < GRID_HEIGHT-1:
        cursor_y += 1
        updated = True
        time.sleep(0.07)

    if ion.keydown(ion.KEY_OK):
        grid[cursor_y][cursor_x] = 1 - grid[cursor_y][cursor_x]
        updated = True
        time.sleep(0.17)
    if ion.keydown(ion.KEY_NINE):
        next_generation()
        updated = True
        time.sleep(0.17)
    if ion.keydown(ion.KEY_EIGHT):
        auto_mode = not auto_mode
        updated = True
        time.sleep(0.17)
    if auto_mode:
        next_generation()
        updated = True
        time.sleep(0.12)

    # Pour éviter les conflits d'affichage et les artefacts, on redessine tout à chaque update
    if updated:
        display_grid(with_cursor=True)

    if not auto_mode:
        time.sleep(0.01)