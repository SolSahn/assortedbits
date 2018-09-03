# A script simulating Langton's ant using a 2D grid and ASCII

import os
import time

GRIDSIZE = (225, 48) # Tuple determining size of grid
FRAMERATE = 0.02 # Framerate of simulation
ITERATIONS = 20000 # Number of iterations ant

swap = {
    0: 1,
    1: 0
}

textgraphics = {
    0: " ",
    1: "#"
}

class Ant:
    def __init__(self, position, rotation):
        self.position = position # Two-value list representing position of ant
        self.rotation = rotation # Rotation of ant
        
        self.positionSwitcher = { # Sets 0 1 2 3 to N E S W
            0: lambda: (self.position[0], self.position[1] + 1),
            1: lambda: (self.position[0] + 1, self.position[1]),
            2: lambda: (self.position[0], self.position[1] - 1),
            3: lambda: (self.position[0] - 1, self.position[1])
        }
        self.rotationSwitcher = { # Rotates left on black, right on white
            0: lambda: self.rotation + 1,
            1: lambda: self.rotation - 1
        }

    def move(self, direction): # Move ant based on switcher
        self.movement = self.positionSwitcher[direction]
        self.position = self.movement()

    def wrap(self): # Wraps around to prevent rotational over- and underflow
        if self.rotation > 3:
            self.rotation = 0
        elif self.rotation < 0:
            self.rotation = 3

    def iterate(self, color): # Rotates, wraps, and moves ant
        self.rotate = self.rotationSwitcher[color]
        self.rotation = self.rotate()
        self.wrap()

        self.move(self.rotation)

def graphics():
    os.system("clear")
    screen = ""
    for x in range(GRIDSIZE[1]):
        for y in range(GRIDSIZE[0]):
            text = textgraphics[grid[x][y]]
            screen += text
            if y == GRIDSIZE[0] - 1:
                screen += "\n"
    print(screen)

grid = [[0 for x in range(GRIDSIZE[0])] for y in range(GRIDSIZE[1])]
a = Ant((16, 115), 0)

for i in range(ITERATIONS):
    graphics()
    try:
        a.iterate(grid[a.position[0]][a.position[1]])
    except IndexError:
        print("ant has exited board!")
        exit()
    grid[a.position[0]][a.position[1]] = swap[grid[a.position[0]][a.position[1]]]
    time.sleep(FRAMERATE)
