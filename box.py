class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def move(self):
        self.x, self.y = self.x + self.dx, self.y + self.dy

    def collide(self, listObjects):
        for object in listObjects:
            if self.x + self.dx == object.x and self.y + self.dy == object.y:
                return object
        return None

    def overlap(self, listObjects):
        for object in listObjects:
            if self.x == object.x and self.y == object.y:
                return True
        return False