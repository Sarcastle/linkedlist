from typing_extensions import Self

class Node():

    def __init__(self, id: int, name: str) -> None:
        self._id: int = id
        self._name: str = name
        self._next: Self = None

    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def next(self) -> Self:
        return self._next
    @next.setter
    def next(self, value: Self):
        self._next = value

class LinkedList():
    def __init__(self) -> None:
        self._nodeList: dict[int, Node] = {}
        self._nodePos: dict[int, int] = {}

    def addNode(self, node:Node) -> None:

        if node is not None:  
            found: bool = node.id in self._nodeList
            if not found: 
                pos = len(self._nodeList) + 1 
                self._nodePos[pos] = node.id  
                self._nodeList[node.id] = node 
                
                if pos > 1:  
                    prevNodePos = pos - 1 
                    prevNodeId = self._nodePos[prevNodePos]  
                    prevNode = self._nodeList[prevNodeId] 
                    prevNode.next = node 
        

node1 = Node(1, 'Twin')
node2 = Node(2, 'Full')
node3 = Node(3, 'Queen')
node4 = Node(4, 'King')

myLL = LinkedList()
myLL.addNode(node1)
myLL.addNode(node2)
myLL.addNode(node3)
myLL.addNode(node4)