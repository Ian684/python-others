import uuid
def solve(count):
    return [str(uuid.uuid4()) for _ in range(count)]
