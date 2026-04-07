from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # Perimeter path: Bottom, Right, Top, Left
        # Directions as robot walks the border: E, N, W, S
        self.dirs = ["East", "North", "West", "South"]
        self.dx =   [1,       0,      -1,      0]
        self.dy =   [0,       1,       0,     -1]
        
        # Total perimeter steps
        self.perimeter = 2 * (width + height) - 4
        self.pos = 0  # Current step along perimeter
        
        # Precompute corner positions along perimeter
        # Bottom row: (0,0) to (w-1, 0) -> steps 0 to w-1
        # Right col:  (w-1, 0) to (w-1, h-1) -> steps w-1 to w+h-2
        # Top row:    (w-1, h-1) to (0, h-1) -> steps w+h-2 to 2w+h-3
        # Left col:   (0, h-1) to (0, 0) -> steps 2w+h-3 to 2w+2h-4
        self.d = 0  # Direction index (starts facing East)

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.perimeter
        
        # Determine direction based on position on perimeter
        w, h = self.w, self.h
        if self.pos < w:                         # Bottom edge, going East
            self.d = 0
        elif self.pos < w + h - 1:               # Right edge, going North
            self.d = 1
        elif self.pos < 2 * w + h - 2:           # Top edge, going West
            self.d = 2
        else:                                     # Left edge, going South
            self.d = 3

    def getPos(self) -> List[int]:
        w, h = self.w, self.h
        p = self.pos
        if p < w:                                # Bottom edge
            return [p, 0]
        elif p < w + h - 1:                      # Right edge
            return [w - 1, p - (w - 1)]
        elif p < 2 * w + h - 2:                  # Top edge
            return [w - 1 - (p - (w + h - 2)), h - 1]
        else:                                     # Left edge
            return [0, h - 1 - (p - (2 * w + h - 3))]

    def getDir(self) -> str:
        return self.dirs[self.d]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()


# Test cases
if __name__ == "__main__":
    robot = Robot(6, 3)
    robot.step(2); print(robot.getPos(), robot.getDir())  # [2,0], East
    robot.step(2); print(robot.getPos(), robot.getDir())  # [4,0], East
    robot.getPos()                                         # [4,0]
    robot.getDir()                                         # East
    robot.step(2); print(robot.getPos(), robot.getDir())  # [5,1], North
    robot.step(1); print(robot.getPos(), robot.getDir())  # [5,2], North
    robot.step(4); print(robot.getPos(), robot.getDir())  # [1,2], West
    print(robot.getPos())                                  # [1,2]
    print(robot.getDir())                                  # West