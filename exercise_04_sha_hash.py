import hashlib
def solve(text):
    return hashlib.sha256(text.encode()).hexdigest(), hashlib.sha3_256(text.encode()).hexdigest()
