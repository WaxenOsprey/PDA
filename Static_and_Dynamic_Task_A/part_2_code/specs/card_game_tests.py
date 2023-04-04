import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Diamonds", 5)

        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        self.card1 = Card("Spades", 1)

        result = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, result)

    def test_highest_card(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Diamonds", 5)

        result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(5, result.value)

    def test_cards_total(self):
        self.cards = [self.card1, self.card2]

        result = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 6", result)