import json
def json_file() -> float:
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    calculate_sum = sum([item["score"] * item["weight"] for item in json_data])
    return round(calculate_sum, 3)

print(json_file())
