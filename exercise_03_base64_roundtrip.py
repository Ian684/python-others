import base64
def solve(text):
    encoded = base64.b64encode(text.encode()).decode()
    return encoded, base64.b64decode(encoded).decode()
