def populate_nested_list(string_input):
    nested_list = [[]]
    nested_list_location = 0
    for i in range(len(string_input)):
        if string_input[i] == "":
            nested_list_location += 1
            nested_list.append([])
            continue
        else:
            nested_list[nested_list_location].append(string_input[i])
    return nested_list


def find_top_values(list_input):
    temp = 0
    total = 0
    totals_list = []

    for i in list_input:
        for j in i:
            temp += int(j)
        if temp > total:
            total = temp
        totals_list.append(temp)
        temp = 0

    totals_list.reverse()

    return total, sum(totals_list[0:3])


def day_one(input_file):
    input_data = open(input_file, "r").read().splitlines()
    populated_list = populate_nested_list(input_data)
    total = find_top_values(populated_list)

    return total



