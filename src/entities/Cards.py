class Card:
    def __init__(self, name: str):
        self.name = name

class PropertyCard(Card):
    def __init__(self, name: str, rent_values: {int:int}):
        super().__init__(name)
        self.rent_values = rent_values

class ChanceCard(Card):
    def __init__(self, name: str, content: str):
        super().__init__(name)
        self.content = content

class CommunityChestCard(Card):
    def __init__(self, name: str, content: str):
        super().__init__(name)
        self.content = content