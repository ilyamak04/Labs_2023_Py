import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as inp:
        with open(OUTPUT_FILENAME, "w") as out:
            reader = csv.DictReader(inp, delimiter=',', quotechar='\n')
            for item in reader:
                json.dump(item, out, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
