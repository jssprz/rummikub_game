
def play(hand, table):
    result_hand = []
    result_table = []

    # determine series
    _series = series(hand)

    # determine stairs
    _stairs = stairs(hand)

    # determine table's stairs
    _table_stairs = [x for x in enumerate(table) if not is_serial(x[1])]

    # determine table's series
    _table_series = [x for x in enumerate(table) if is_serial(x[1])]
    
    # determine stairs can be appended
    _app_stairs = appending_stairs(hand, _table_stairs)
    
    # determine series can be appended
    _app_series = appending_series(hand, _table_series)
    
    # determine stairs can be separated
    _split_stairs = splitting_stairs(_table_stairs)
    
    # determine all series with more than 3 tiles
    _big_series = popping_series(_table_series)

    # determine all stairs with more than 3 tiles
    _big_stairs = popping_stairs(_table_stairs)
    
    # determine all possible jokers substitutions
    _jokers_substitutions = jokers_substitution(hand, table)

    for serial in _series:
        # remove tiles from hand
        new_hand = [x for x in hand]
        new_hand = []

        # add serial to table
        new_table = [x for x in table]
        new_table.append(serial)

        play(new_hand, new_table)

    for stair in _stairs:
        # remove tiles from hand
        new_hand = [x for x in hand]
        new_hand = []

        # add stair to table
        new_table = [x for x in table]
        new_table.append(stair)

        play(new_hand, new_table)

    for app_serial in _app_series:
        # remove tile from hand
        new_hand = [x for x in hand]
        new_hand = []

        # add tile to serial in table
        new_table = [x for x in table]
        new_table = []

        play(new_hand, new_table)

    for app_stair in _app_stairs:
        # remove tile from hand
        new_hand = [x for x in hand]
        new_hand = []

        # add tile to stair in table
        new_table = [x for x in table]
        new_table = []

        play(new_hand, new_table)

    for split_stair in _split_stairs:
        # remove the stair from table
        new_table = [x for x in table]
        new_table = []

        # split stair
        stair1 = []
        stair2 = []

        # add the new two stairs to the table
        new_table.append(stair1)
        new_table.append(stair2)

        play(hand, new_table)

    for big_serial in _big_series:
        # remove tile from table's serial
        new_table = [x for x in table]
        new_table = []

        # add tile to the hand
        new_hand = [x for x in hand]
        new_hand = []

        play(new_hand, new_table)

    for big_stair in _big_stairs:
        # remove tile from table's stair
        new_table = [x for x in table]
        new_table = []

        # add tile to the hand
        new_hand = [x for x in hand]
        new_hand = []

        play(new_hand, new_table)

    for joker_substitution in _jokers_substitutions:
        # replace joker from table's combination
        new_table = [x for x in table]
        new_table = []

        # add joker to the hand
        new_hand = [x for x in hand]
        new_hand.append((0, 0))

        play(new_hand, new_table)

    return result_hand, result_table


def appending_stairs(hand, stairs):
    # returns all table's stairs indexes and the tile's index can be added to it
    result = []

    # determine tiles can be added to any stair in stairs list
    possible_tiles = []
    for stair in stairs:
        color = stair[1][0]
        min_value = stair[1][0][0] if stair[1][0][0] != 0 else stair[1][1][0] - 1
        max_value = stair[1][-1][0] if stair[1][-1][0] != 0 else stair[1][-2][0] + 1
        if min_value != 1 and max_value != 13:
            possible_tiles.append((stair[0], [(min_value - 1, color), (max_value + 1, color)]))
        elif min_value != 1:
            possible_tiles.append((stair[0], [(min_value - 1, color)]))
        elif max_value != 13:
            possible_tiles.append((stair[0], [(max_value + 1, color)]))

    # determine the hand's tiles present in possible_tiles
    for tile in hand:
        for p_tiles in possible_tiles:
            for t in p_tiles[1]:
                if tile == t:
                    result.append((p_tiles[0], t))

    return result


def appending_series(hand, series):
    # returns all table's series indexes and the tile's index can be added to it
    result = []

    # determine tiles can be added to any srial in series list
    possible_tiles = []
    for serial in


    return [(0, 0)]


def splitting_stairs(stairs):
    # returns all table's stairs indexes can be separated and the index to do that
    return [0]


def popping_stairs(stairs):
    # returns all table's stairs indexes with more than 3 elements
    return [(0, 0)]


def popping_series(series):
    # returns all table's series indexes with more than 3 elements
    return [0]


def jokers_substitution(hand, table):
    # returns all table's combinations indexes with a joker can be replaced with a hand's tile
    return [(0, 0)]


def series(hand):
    return []


def stairs(hand):
    return []


def get_series(combinations):
    # returns a sub-set of combinations with the series only

    return 0


def get_stairs(combinations):
    # returns a sub-set of combinations with the stairs only
    return 0


def is_serial(table_combination):
    # determine if table_combination is a serial

    # get the different values
    values = [x[0] for x in table_combination]

    if len(values) > 2:
        return False
    elif len(values) == 2:
        return sorted(values)[0] == 0
    return True