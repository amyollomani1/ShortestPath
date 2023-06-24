import pygame
from queue import PriorityQueue
import math
from Cell import *
from algorithm import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A Path Finding Application")

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Cell(i,j,gap,rows)
            grid[i].append(cell)
    return grid

def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j *gap, 0), (j * gap, width))
            
def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for cell in row:
            cell.draw(win)
            
    draw_grid(win,rows,width)
    pygame.display.update()
    
#helper function
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x,y = pos
    row = x // gap
    col = y // gap
    return row,col
             
def main(win,width, ROWS):
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    
    while run:
        draw(win, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]: #left mouse button
                pos = pygame.mouse.get_pos() #gets pos of mouse
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                if not start and cell != end:
                    start = cell
                    start.make_start()
                elif not end and cell != start:
                    end = cell
                    end.make_end()
                elif cell != end and cell != start:
                    cell.make_barrier()
                    
            elif pygame.mouse.get_pressed()[2]: #right mouse button
                pos = pygame.mouse.get_pos() #gets pos of mouse
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                cell.reset()
                if cell == start:
                    start = None
                if cell == end:
                    end = None
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                            
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    #lambda is a way to call draw function and pass result as argument to algortihm
                    
                
    pygame.quit()
     
main(WIN, WIDTH, 50)         
