import code
import os

SEP = os.path.sep

FILE_DIC = {
    1: f"C:{SEP}GITHUB{SEP}AdventOfCode2022{SEP}files{SEP}input_day1.txt",
    2: f"C:{SEP}GITHUB{SEP}AdventOfCode2022{SEP}files{SEP}input_day2.txt",
    3: f"C:{SEP}GITHUB{SEP}AdventOfCode2022{SEP}files{SEP}input_day3.txt"
}


def main():
    print(code.day_one(FILE_DIC[1]))
    print(code.day_2_part_1(FILE_DIC[2]))
    print(code.day_2_part_2(FILE_DIC[2]))
    print(code.day_3_part_1(FILE_DIC[3]))

if __name__ == '__main__':
    main()

