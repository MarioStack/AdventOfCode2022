import code
import os

SEP = os.path.sep

FILE_DIC = {
    1: f"C:{SEP}GITHUB{SEP}AdventOfCode2022{SEP}files{SEP}input_day1.txt",
}


def main():
    print(code.day_one(FILE_DIC[1]))


if __name__ == '__main__':
    main()

