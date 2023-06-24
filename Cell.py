import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128, 0 , 128)
ORANGE = (255,165,0)
GREY = (128, 128, 128)
AQUA = (64, 224, 208)

class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
    
    def get_pos(self):
        return self.row, self.col
    
    def is_marked(self):
        return self.color == RED
    
    def is_not_marked(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == AQUA
    
    def reset(self):
        self.color = WHITE
        
    def mark(self):
        self.color = RED
        
    def unmark(self):
        self.color = GREEN
        
    def make_barrier(self):
        self.color = BLACK
    
    def make_end(self):
        self.color = AQUA
        
    def make_path(self):
        self.color = PURPLE
        
    def make_start(self):
        self.color = ORANGE
        
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        
    #Checks barriers if movement is possible
    def update_neighbors(self,grid):
        self.neighbors = []
        #DOWN
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])
        #UP
        if self.row > 0 and not grid[self.row -1][self.col].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col])
        #LEFT
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])
        #RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])
    
    def __it__(self, other):
        return False