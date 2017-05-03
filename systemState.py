import constants
import collections

class SystemState():
    def __init__(self):
        self.trailPoints = collections.deque()
        self.currentPage = constants.Page.HOME
        self.direction = constants.Direction.NONE 
        self.removedPoint = (0,0)
        self.lastSwipe = 0
        self.userList = collections.deque()
        
    def setPage(self, newPage):
        self.currentPage = newPage
    
    def resetDirection(self):
        self.direction = constants.Direction.NONE

    # adds points to the trail, pops off oldest point if past length limit and returns it
    def addPoint(self, x):
        self.trailPoints.append(x)
        if len(self.trailPoints) > constants.POINT_LIMIT:
            return self.trailPoints.popleft()
        else:
            return self.trailPoints[0]