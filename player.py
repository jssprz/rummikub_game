import random

class Player:
    _hand = []

    def set_hand(self, hand):
        self._hand = hand


    def select_tile(self, heap_count):
        return random.randint(0, heap_count)


    def add_tile(self, tile):
        self._hand.append(tile)


    def initial_play(self):
        return []


    def play(self, table):
        return []