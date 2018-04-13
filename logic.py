import random


class Rummikub:
    _heap = []
    _players = []
    _table = []
    _initial_played = []
    _hands = []

    def initialize_game(self, players):
        self._players = players

        tiles = [(0, 0), (0, 0),
                 (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1),
                 (13, 1),
                 (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),
                 (13, 2),
                 (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3),
                 (13, 3),
                 (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4),
                 (13, 4)]

        # re-sort tiles, initialize heap
        while len(tiles) > 0:
            r_index = random.randint(0, len(tiles))
            self._heap.append(tiles[r_index])
            tiles.pop(r_index)

        # determine players order, re-sort _players
        self.__determine_players_order()

        # create initial hand for each player
        self._hands = list(map(lambda x: [], self._players))
        for i in range(14):
            for j in range(len(self._players)):
                index = self._players[i].select_tile(len(self._heap))
                self._hands[j].append(self._heap[index])
                self._heap.pop(index)

        # set initial hand for each player
        for i in range(len(self._players)):
            self._players[i].set_hand(self._hands[i])

        return 0

    def __determine_players_order(self):
        aux = list(enumerate(self._players))
        selected_tiles = []

        # each player get a tile from heap
        for i in range(len(self._players)):
            index = self._players[i].select_tile(len(self._heap))
            tile = self._heap[index]
            selected_tiles.append(tile)
            self._heap.pop(index)
            aux[i][0] = tile[0]

        # sort player for selected tile value
        aux.sort(key=lambda x: x[0], reverse=True)

        # re-insert selected tiles to the heap
        self._players = list(map(lambda x: x[1], aux))
        for tile in selected_tiles:
            self._heap.insert(random.randint(0, len(self._heap)), tile)

    def game(self):
        current_player = 0
        while not self.__game_finished():
            # verify if player have not made the initial play
            if not self._initial_played[current_player]:
                combination = self._players[current_player].initial_play()

                if len(combination) == 0:
                    # add new tile to the player's hand
                    index = self._players[current_player].select_tile(len(self._heap))
                    self._players[current_player].add_tile(self._heap[index])
                    self._hands.append(self._heap[index])
                    self._heap.pop(index)
                elif self.is_correct(combination) and self.more_30_points(combination):
                    # continue the players turn
                    new_table = self._players[current_player].play(self._table)

                    # verify the new_table is correct (from player's hand and current table)


                    # update player's hand and table

                    # add combination to the current table
                    self._table.extend(combination)
                else:
                    print('error in initial play')
            else:
                self._players[current_player].play(self._table)

    def __game_finished(self):
        for player in self._players:
            if player.hand_size() == 0:
                return True
        return False

    def is_correct_move(self, player_id, result_table):
        current_table = self._table
        player_hand = self._hands[player_id]

        possible_tiles = player_hand + [item for sublist in current_table for item in sublist]
        for c in result_table:
            # verify the current combination is correct
            if self.is_correct(c):
                for tile in c:
                    # verify all tiles in result table was in current_table or player_hand
                    if tile in possible_tiles:
                        possible_tiles.remove(tile)
                    else:
                        return False

        # check position of jokers

        # check the result player's hand don't contains table's tiles

        return True

    def is_correct(self, combination):
        for c in combination:
            if not self.is_serial(c) and not self.is_stair(c):
                return False
        return True

    def more_30_points(self, combination):
        points = 0
        for c in combination:
            for tile in c:
                points += tile[0]
                if points >= 30:
                    return True
        return False

    def is_serial(self, tiles):
        if len(tiles) < 3:
            return False

        colors = [tiles[0][1]]
        value = tiles[0][0]
        for i in range(1, len(tiles)):
            if tiles[i][1] not in colors or value != tiles[i][0]:
                return False
            colors.append(tiles[i][1])
        return True

    def is_stair(self, tiles):
        if len(tiles) < 3:
            return False

        current_value = tiles[0][0]
        color = tiles[0][1]
        for i in range(1, len(tiles)):
            if color != tiles[i][1] or current_value+1 != tiles[i][0]:
                return False
            current_value = tiles[i][0]
        return True