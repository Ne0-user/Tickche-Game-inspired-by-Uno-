from LinkedList import LinkedList
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = LinkedList()
    
    def add_card(self,card):
        self.hand.add_first(card)
    
    def remove_card(self, card):
        return self.hand.remove_card(card)