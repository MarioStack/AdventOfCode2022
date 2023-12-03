from string import ascii_letters


def ascii_dictionary() -> dict:
    dictionary = {}

    for number, letter in enumerate(ascii_letters):
        dictionary[letter] = number + 1

    return dictionary


def rucksack_values(rucksack_list: list[str], ascii_dict: dict) -> int:
    duplicate_found = False
    total = 0

    for rucksack in rucksack_list:
        first_half, second_half = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

        for first_character in first_half:
            if duplicate_found:
                break

            for second_character in second_half:
                if first_character == second_character:
                    duplicate_found = True
                    total += ascii_dict[first_character]
                    break

        duplicate_found = False

    return total


def day_3_part_1(input_file_path: str) -> int:
    with open(input_file_path, "r") as file:
        input_data = file.read().splitlines()

    ascii_dict = ascii_dictionary()

    print(rucksack_values(input_data, ascii_dict))


