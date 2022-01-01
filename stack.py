from node import Node

#create stack class
class Stack: 
    def __init__(self, name):
        self.size = 0
        self.top_item = None 
        self.limit = 1000
        self.name = name 

    def push(self, value):
        pass 

    def pop(self): 
        pass

    def peek(self):
        pass

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name