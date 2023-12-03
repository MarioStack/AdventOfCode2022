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


def day_2_part_1(input_file_path: str) -> int:
    with open(input_file_path, "r") as file:
        input_lines = file.read().splitlines()

    total = 0

    for line in input_lines:
        enemy_hand, our_hand = line.split()
        enemy_hand = INPUT_MAP.get(enemy_hand)
        our_hand = INPUT_MAP.get(our_hand)

        if enemy_hand == our_hand:
            total += SCORE_MAP.get("Draw") + SHAPE_MAP.get(our_hand)
        elif (enemy_hand, our_hand) in [("Rock", "Paper"), ("Paper", "Scissors"), ("Scissors", "Rock")]:
            total += SCORE_MAP.get("Win") + SHAPE_MAP.get(our_hand)
        else:
            total += SCORE_MAP.get("Lose") + SHAPE_MAP.get(our_hand)
    return total






















