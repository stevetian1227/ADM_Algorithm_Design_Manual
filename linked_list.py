class Node():
    def __init__(self,data=None):
        self.data = None
        self.next = None

class SLinkedList():
    def __init__(self):
        self.root = None
    
    def insert(self,node,data):
        if node is None:
            return
        newNode = Node(data)
        newNode.next = node.next
        node.next = newNode
    
    def search(self,data):
        if self.root is None:
            return(0)
        node = self.root
        if node.data == data:
            return(1)
        while node.next is not None:
            node = node.next
            if node.data == data:
                return(1)
        return(0)

    def remove(self,data):
        node = self.root
         
        if (node is not None):
            if (node.data == data):
                self.root = node.next
                root = None
                return
        while (node is not None):
            if node.data == data:
                break
            prev = node
            node = node.next

        if (node == None):
            return

        prev.next = node.next
        node = None


list = SLinkedList()
list.root = Node("first")
