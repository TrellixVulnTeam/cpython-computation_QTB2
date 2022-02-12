from logging import root


class LinkedList:
    
    def __init(self, r = None):
        self.root = r
        self.size = 0
        
    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size += 1
        
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
            
                        