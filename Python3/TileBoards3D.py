### Many games include tle boards, where your character can act or move only on close tiles
### The Direction class allows to easily scan all directions

class Direction3D:
    def __init__(self, name, dir):
        self.name = name
        self.dirX = dir[0]
        self.dirY = dir[1]
        self.dirZ = dir[2]
        self.opposite = None

    def SetOpposites(dir1, dir2):
        dir1.opposite = dir2
        dir2.opposite = dir1

#Direct direction are directly forward, backward (X), left, right (Y), up and down (Z)
FDir = Direction("FORWARD",[1, 0, 0] )
BDir = Direction("BACKWARD",[-1, 0, 0] )
LDir = Direction("LEFT",[0, 1, 0] )
RDir = Direction("RIGHT",[0, -1, 0] )
UDir = Direction("UP",[0, 0, 1] )
DDir = Direction("DOWN",[0, 0, -1] )
Direction.SetOpposites(FDir, BDir)
Direction.SetOpposites(LDir, RDir)
Direction.SetOpposites(UDir, DDir)

DirectDirections = [FDir, BDir, LDir, RDir, UDir, DDir]
