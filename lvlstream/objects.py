class staticobject:
    def __init__(self, objectstr: str) -> None:
        self.__object = objectstr.split(',')
    
    def __getobjectvalue(self, key: str) -> str:
        for index, value in enumerate(self.__object):
            if value == key:
                return self.__object[index + 1]
    def __setobjectvalue(self, key: str, ovalue: str) -> str:
        for index, value in enumerate(self.__object):
            if value == key:
                self.__object[index + 1] = ovalue
    
    @property
    def placement(self) -> dict:
        return {
            'x': int(self.__getobjectvalue('2')),
            'y': int(self.__getobjectvalue('3'))
        }
    
    @property
    def oid(self) -> int:
        return int(self.__getobjectvalue('1'))
    
    @property
    def groups(self) -> list[int]:
        return [int(i) for i in self.__getobjectvalue('57').split('.')]
    
    
    def group_mod(self, gid: int, rm: bool) -> None:
        if rm == True:
            groups = self.groups
            groups.remove(gid)
            self.__setobjectvalue('57', groups)
        else:
            groups = self.groups
            groups.append(gid)
            self.__setobjectvalue('57', groups)
    
    def set_id(self, id: str) -> None:
        self.__setobjectvalue('1', id)
    
    
    @property
    def getobjectstr(self) -> str:
        return ','.join(self.__object)



class dynamicobject:
    ...