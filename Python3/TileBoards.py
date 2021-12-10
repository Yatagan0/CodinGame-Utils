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


#The wild fire algorithm aims to find the shortest path from one point to another
#You can find the shortest path to a range of objects by using propagate several times from different (x,y)
##PREREQUISITE : have a getValue(x,y) function that returns the state of the map at (x, y)
class WildFireDistance:
    def __init__(self, x, y):
        self.x = x
        self.y = y        
        self.distance = -1
        self.fromDir = None

    def previous(self):
        if self.fromDir is None:
            return None
        x, y = self.fromDir.opposite.Move(self.x, self.y)
        return [x, y]
        
class WildFire:
    def __init__(self, h, w, tx, ty):
        self.Width = w
        self.Height = h
        self.map = []
        for i in range(h):
            row = []
            for j in range(w):
                row.append(WildFireDistance(j, i))
            self.map.append(row)

        self.targetX = tx
        self.targetY = ty
        self.minDist = -1

        self.invalidChars = ["#", "?"]#walls, unknowns,traps...

    def InRange(self, x, y):
        return 0 <= x < self.Width and 0 <= y < self.Height

    def Propagate(self, x, y, dist, fromDirection):
        #(x,y) not on the map
        if not self.InRange(x, y):
            return
        
        #if we have found a path, don't look for longer paths
        if self.minDist != -1 and dist >= self.minDist:
            return

        #we found a path !
        if  x == self.targetX and y == self.targetY:
            self.minDist = dist

        v = getValue(x,y)
        if v in self.invalidChars:
            return

        #did we already encounter this position ?
        val = self.map[y][x]
        if val.distance != -1 and dist >= val.distance:
            return

        val.distance = dist
        val.fromDir = fromDirection

        for dir in DirectDirections.values():
            #don't go back where you come from
            if fromDirection != None and dir == fromDirection.opposite:
                continue
            xx, yy = dir.Move(x, y)
            #compute for neighbor position
            self.Propagate(xx, yy, dist+1, dir)

    def GoFrom(self, x, y):
        val = self.map[y][x]
        if val.fromDir != None:
            return val.fromDir.opposite.name
        return ""

    def DumpMap(self):
        for i in self.map:
            s = ""
            for j in i:
                s+=str(j.distance)+" "

            log([s])

#example
#wf = WildFire(rowsNb,columnsNs, robot.x, robot.x)
#wf.Propagate(treasure[0].x, treasure[0].y, 0, None)
#wf.Propagate(treasure[1].x, treasure[1].y, 0, None)
#while not treasureFound:
 #   robot.addMove("MOVE "+wf.GoFrom(robot.x, robot.x))