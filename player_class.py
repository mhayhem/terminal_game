# @author: Mhayhem
# date: 2025-05-15
class Player:
    """player class to create player objects with name and wins attributes
    
    """
    def __init__(self, name, wins):
        self.name = name.capitalize()
        self.wins = wins
        