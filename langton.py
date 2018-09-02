# A script simulating Langton's ant using Pillow

from PIL import Image
import os.path
import random

# Customizable variables

gridsize = (250, 250) # Tuple determining size of grid
antnum = 50 # Number of ants to randomly place
frames = False # Boolean indicating whether to save each individual iteration as a frame
steps = 2000 # Number of steps each ant gets

# Ant class

class Ant:
    def __init__(self, position, rotation):
        self.position = position # Two-value list representing position of ant
        self.rotation = rotation # Rotation of ant
        
        self.positionSwitcher = { # Sets 0 1 2 3 to N E S W
            0: lambda: (self.position[0], self.position[1] + 1),
            1: lambda: (self.position[0] + 1, self.position[1]),
            2: lambda: (self.position[0], self.position[1] - 1),
            3: lambda: (self.position[0] - 1, self.position[1]),
        }
        self.rotationSwitcher = { # Rotates left on black, right on white
            0: lambda: self.rotation - 1,
            255: lambda: self.rotation + 1
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

grid = Image.new("L", gridsize, "white") # Create grid with size specified earlier
cells = grid.load()
ants = [] # Create empty ant array

colorSwapper = { # Swap black and white after moving ant
    0: 255,
    255: 0
}

if frames: # Creates a frames folder if one does not already exist
    framenum = 0
    if not os.path.isdir("frames"):
        os.mkdir("frames")

for i in range(antnum): # Append specified number of ants with pseudo-random positions and rotations
    position = [random.randrange(50, grid.size[0]-50), random.randrange(50, grid.size[1]-50)]
    rotation = random.randrange(0, 3)
    ants.append(Ant(position, rotation))

for a in ants: # Cycles through all steps of all ants, swapping colors and saving frames if told to
    for i in range(steps):
        a.iterate(cells[a.position[0], a.position[1]])
        cells[a.position[0], a.position[1]] = colorSwapper[cells[a.position[0], a.position[1]]]
        if frames:
            grid.save("frames/frame" + str(frameNum) + ".png")
            frameNum += 1

grid.save("output.png") # Saves final frame as output.png


