### Many games include tle boards, where your character can act or move only on close tiles
### The Direction class allows to easily scan all directions

class Direction:
    def __init__(self, name, dir):
        self.name = name
        self.dirX = dir[0]
        self.dirY = dir[1]
        self.opposite = None

    def SetOpposites(dir1, dir2):
        dir1.opposite = dir2
        dir2.opposite = dir1

#Direct direction are directly left, right, up and down
LDir = Direction("LEFT",[-1, 0] )
RDir = Direction("RIGHT",[1, 0] )
UDir = Direction("UP",[0, -1] )
DDir = Direction("DOWN",[0, 1] )
Direction.SetOpposites(LDir, RDir)
Direction.SetOpposites(UDir, DDir)
DirectDirections = [LDir, RDir, UDir, DDir]

# around direction are the direct directions plus up-right, up-left, down-right and down-left
ULDir = Direction("UPLEFT",[-1, -1] )
URDir = Direction("UPRIGHT",[1, -1] )
DLDir = Direction("DOWNLEFT",[-1, 1] )
DRDir = Direction("DOWNRIGHT",[1, 1] )
Direction.SetOpposites(ULDir, DRDir)
Direction.SetOpposites(URDir, DLDir)
AroundDirections = [LDir, RDir, UDir, DDir, ULDir, URDir, DLDir, DRDir]

### Example
### scan all direct direction, if you find an ennemy, move in opposite direction
#for dir in DirectDirections:
#    nextPos = [currentX + dir.dirX, currentY + dir.dirY] 
#    if ennemyAt(nextPos):
#        print("MOVE "+dir.opposite.name)
#        return