from Node import Node
import random


class Stack:
    def __init__(self, data=None):
        self.top = None
        if data:
            try:
                for d in data:
                    self.push(d)
            except:
                self.push(data)

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top=new_node
        else:
            new_node.set_next(self.top)
            self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Underflow")
        data_out=self.top.get_data()
        self.top=self.top.get_next()
        return data_out
    
    def peek(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.top.get_data()

    def is_empty(self):
        return self.top == None
    
    def __repr__(self):
        str_out = "["
        current = self.top
        while current:
            str_out += str(current.data) + ", "
            current = current.next
        return str_out + ("]" if self.is_empty() else "\b\b]")
    
    
    def shuffle(self):
        cards = []
        while not self.is_empty():
            cards.append(self.pop())
        random.shuffle(cards)
        for c in cards:
            self.push(c)