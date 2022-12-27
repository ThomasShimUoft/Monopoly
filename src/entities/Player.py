from src.entities.Cards import Card


class Player:
    def __init__(self):
        self.money = 0
        self.cards = []

    def get_money(self) -> int:
        return self.money

    def set_money(self, money: int) -> None:
        self.money = money

    def get_cards(self) -> [Card]:
        return self.cards

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def delete_card(self, card: Card) -> None:
        self.cards.remove(card)