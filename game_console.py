class GameConsole(): 
   
    def __init__(self, name: str = '', storage: str = '', portable: bool = False) -> None:
        self._name: str = name
        self._storage: str = storage
        self._portable: bool = portable

    @property 
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        if value != self._name:
            self._name = value

    @property 
    def storage(self) -> str:
        return self._storage
    @storage.setter
    def storage(self, value:str):
        if value != self._storage:
            self._storage = value

    @property 
    def portable(self) -> bool:
        return self._portable
    @portable.setter
    def portable(self, value:bool):
        if value != self._portable:
            self._portable = value

myGameConsole = GameConsole('Xbox')
myGameConsole.storage = '500G'
myGameConsole.portable = False 
port_str:str = 'and is portable' if myGameConsole.portable else ''
print(f'the {myGameConsole.name} im playing on has {myGameConsole.storage}s of storage {port_str}')

    
        