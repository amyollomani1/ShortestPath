from queue import PriorityQueue
import pygame
from Cell import Cell
def reconstruct_path(came_from, current, draw):	
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
   

def algorithm(draw, grid, start, end): #draw is  a function
    count = 0
    unmarked_set = PriorityQueue()
    unmarked_set.put((0,count,start)) #use count as a tie breaker
    cameFrom = {}
    g_score = {cell: float("inf") for row in grid for cell in row} #float("inf") is infinity in python
    g_score[start] = 0
    f_score = {cell: float("inf") for row in grid for cell in row} #float("inf") is infinity in python
    f_score[start] = h(start.get_pos(),end.get_pos()) #f score is heursristic to make estimate of shortest distance between start and end
    unmarked_set_hash = {start} #Allows us to check items in PQ. We're using this and PQ
    
    while not unmarked_set.empty(): #allows us to exit if comething goes wrong
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = unmarked_set.get()[2] #gets min from PQ
        unmarked_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(cameFrom, end, draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            
            #if found better case
            if temp_g_score < g_score[neighbor]:
                cameFrom[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in unmarked_set_hash:
                    count += 1
                    unmarked_set.put((f_score[neighbor], count, neighbor))
                    unmarked_set_hash.add(neighbor)
                    neighbor.unmark()
                    
        draw()
        if current != start:
            current.mark()
    
    return False

def h(p1,p2):  #huersitc)
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1 - x2) + abs(y1-y2) #taxi driver distance
