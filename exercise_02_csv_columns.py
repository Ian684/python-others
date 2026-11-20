import csv, io
def solve(text):
    return list(csv.DictReader(io.StringIO(text)))
