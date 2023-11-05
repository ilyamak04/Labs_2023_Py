import json


INPUTFILE = "input.json"

def task() -> float:
    score_weight = 0
    with open(INPUTFILE) as inp:
        data = json.load(inp)
        for item in data:
            score_weight += item['score'] * item['weight']
    return round(score_weight, 3)

print(task())


