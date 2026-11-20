import re
def solve(text):
    return re.findall(r'\b[A-Za-z]{4,}\b', text)
