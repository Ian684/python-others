import re
def solve(text, pattern):
    return re.findall(pattern, text)
