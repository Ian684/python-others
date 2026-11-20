import json
def solve(left, right):
    result = json.loads(json.dumps(left))
    for key, value in right.items():
        result[key] = value
    return result
