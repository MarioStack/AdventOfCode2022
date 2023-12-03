INPUT_MAP = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "Y": "Paper",
    "X": "Rock",
    "Z": "Scissors"
}

SHAPE_MAP = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

SCORE_MAP = {
    "Lose": 0,
    "Draw": 3,
    "Win": 6
}

WANTED_OUTCOME = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

WIN_CONDITIONS = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}


def day_2_part_2(input_file_path: str) -> int:
    with open(input_file_path, "r") as file:
        input_lines = file.read().splitlines()

    total = 0

    for line in input_lines:
        enemy_hand, our_hand = line.split()
        enemy_hand = INPUT_MAP.get(enemy_hand)
        wanted_outcome = WANTED_OUTCOME.get(our_hand)

        if wanted_outcome == "Draw":
            total += SCORE_MAP.get(wanted_outcome) + SHAPE_MAP.get(enemy_hand)
        elif wanted_outcome == "Win":
            total += SCORE_MAP.get(wanted_outcome) + SHAPE_MAP.get(WIN_CONDITIONS.get(enemy_hand))
        else:
            total += (SCORE_MAP.get(wanted_outcome) +
                      SHAPE_MAP.get(list(WIN_CONDITIONS.keys())[list(WIN_CONDITIONS.values()).index(enemy_hand)]))
    return total

