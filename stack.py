from node import Node

#create stack class
class Stack: 
    def __init__(self, name):
        self.size = 0
        self.top_item = None 
        self.limit = 1000
        self.name = name 

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item 
            self.size += 1
        else: 
            print("No Room")

    def pop(self): 
        if self.size > 0: 
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
        print("Stack is empty")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        print("Peeking")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name