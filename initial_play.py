import itertools


def initial_play(hand):
    # find jokers in hand
    jokers_count = hand.count((0, 0))
    # get all possible substitutions for jokers
    jokers_combinations = combinations([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1),
                                        (11, 1), (12, 1), (13, 1), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
                                        (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (1, 3), (2, 3),
                                        (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3),
                                        (12, 3), (13, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                                        (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4)], jokers_count)

    print(jokers_count)

    result = 0, [], []
    for c in jokers_combinations:
        new_hand = [x for x in hand]

        # replace jokers for combination tiles
        for tile in list(c):
            new_hand.pop(new_hand.index((0, 0)))
            new_hand.append(tile)

        # play
        current_result = initial_play_rec(new_hand, [])
        # update the best play
        if current_result[0] > result[0]:
            result = current_result

            # re-insert jokers in result
            for tile in list(c):

                result_hand = result[1]
                for x in result_hand:
                    if x == tile:
                        result_hand.remove(tile)
                        result_hand.append((0, 0))
                        break

                found = False
                result_comb = result[2]
                for x in result_comb:
                    for y in x:
                        if y == tile:
                            x.remove(tile)
                            x.append((0, 0))
                            found = True
                            break
                    if found:
                        break

                result = result[0], result_hand, result_comb

    return result


def initial_play_rec(hand, current_result):
    result_points = 0
    result_hand = hand
    result = []

    # determine series
    _series = series(hand)

    # determine stairs
    _stairs = stairs(hand)

    # base_case
    if len(_series) == 0 and len(_stairs) == 0:
        return 0, hand, [x for x in current_result]

    for serie in _series:
        t_points = serie[0][1][0] * len(serie)
        # remove serie from hand
        new_hand = [x for x in hand]
        for tile in list(map(lambda x: x[1], serie)):
            new_hand.remove(tile)
        # initial_play form result hand
        current_result.append(list(map(lambda x: x[1], serie)))
        pts, final_hand, final_result = initial_play_rec(new_hand, current_result)
        current_result.pop(-1)
        if pts + t_points > 30 and (len(final_hand) < len(result_hand) or points(final_hand) > points(result_hand)):
            result_points = pts + t_points
            result_hand = final_hand
            result = final_result

    for stair in _stairs:
        e_points = sum(map(lambda x: x[1][0], stair))
        # remove stair from hand
        new_hand = [x for x in hand]
        for tile in list(map(lambda x: x[1], stair)):
            new_hand.remove(tile)
        # initial_play from result hand
        current_result.append(list(map(lambda x: x[1], stair)))
        pts, final_hand, final_result = initial_play_rec(new_hand, current_result)
        current_result.pop(-1)
        if pts + e_points > 30 and (len(final_hand) < len(result_hand) or points(final_hand) > points(result_hand)):
            result_points = pts + e_points
            result_hand = final_hand
            result = final_result

    return result_points, result_hand, result


def series(hand):
    # create index
    index = list(enumerate(hand))
    # sort by value, color
    index.sort(key=lambda x: (x[1][0], x[1][1]))
    # create list of list of series
    result = []
    current_serie = [index[0]]
    current_color = index[0][1][1]
    current_value = index[0][1][0]
    for tile in index[1:]:
        if tile[1][0] == current_value and tile[1][1] == current_color:
            continue
        elif tile[1][0] == current_value:
            current_serie.append(tile)
            current_color = tile[1][1]
        else:
            current_value = tile[1][0]
            current_color = tile[1][1]
            if len(current_serie) >= 3:
                result.append(current_serie)
            current_serie = [tile]
    if len(current_serie) >= 3:
        result.append(current_serie)
    return result


def stairs(hand):
    # create index
    index = list(enumerate(hand))
    # sort by color, value
    index.sort(key=lambda x: (x[1][1], x[1][0]))
    # create list of list of stair
    result = []
    current_stair = [index[0]]
    current_color = index[0][1][1]
    current_value = index[0][1][0]
    for tile in index[1:]:
        if tile[1][0] == current_value and tile[1][1] == current_color:
            continue
        elif tile[1][1] == current_color:
            if tile[1][0] == current_value + 1:
                current_stair.append(tile)
            else:
                if len(current_stair) >= 3:
                    result.append(current_stair)
                current_stair = [tile]
            current_value = tile[1][0]
        else:
            current_value = tile[1][0]
            current_color = tile[1][1]
            if len(current_stair) >= 3:
                result.append(current_stair)
            current_stair = [tile]
    if len(current_stair) >= 3:
        result.append(current_stair)
    return result


def points(hand):
    return sum([tile[0] for tile in hand])


def combinations(data, count):
    return itertools.combinations(data, count)


test_hand = [(0, 0), (3, 2), (4, 1), (13, 1), (13, 3), (1, 1), (2, 2), (10, 4), (13, 2), (5, 1), (13, 4), (6, 1),
             (7, 1), (8, 2), (1, 2)]
print(series(test_hand))
print(stairs(test_hand))
print(initial_play(test_hand))
