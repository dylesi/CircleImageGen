import pygame
import math

class Dot:
    def __init__(self, screen, center, color, radius, distance):
        self.radius = radius
        self.color = color
        self.screen = screen
        self.center = center
        self.posX = self.center[1]
        self.posY = self.center[0]
        self.centerXY = (self.posX, self.posY)
        self.distance = distance
        self.segments = 20
        
    def draw(self):
        posX = self.center[0]
        posY = self.center[1]
        angle = 360/self.segments
        
        for i in range(self.segments):
            newCoords = self.newCoordinates(posX, posY, angle * i)
            #print(angle*i)
            pygame.draw.circle(self.screen, self.color, newCoords, self.radius)   
        
    
    def newCoordinates(self, x, y, angle):
        number = angle / 360 * (2 * math.pi)
        newY =  y + math.sin(number) * self.distance
        newX =  x + math.cos(number) * self.distance
        return(newX, newY)