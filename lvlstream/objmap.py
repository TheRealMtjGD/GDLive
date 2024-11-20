from . import objects

class levelmap:
    def __init__(self, lvlstr: str) -> None:
        self.omap = lvlstr.split(';')
        self.ymap = [objects.dynamicobject for _ in range(300)]
        self.levelmap = [self.ymap for _ in range(100000)]
        
        for obj in self.omap:
            staticobject = objects.staticobject(obj)
            self.levelmap[staticobject.placement['x']][staticobject.placement['y']] = staticobject
    
    
    def getobjectdata(self, x: int, y: int) -> objects.staticobject|objects.dynamicobject:
        return self.levelmap[x][y]
    
    @property
    def getmaplength(self) -> tuple:
        return (len(self.levelmap), len(self.ymap))
    
    def extendlvlmap(self, x: int) -> None:
        self.levelmap.extend([self.ymap for _ in range(x)])