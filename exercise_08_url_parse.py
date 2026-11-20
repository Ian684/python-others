from urllib.parse import urlparse, parse_qs
def solve(url):
    parsed=urlparse(url)
    return parsed.scheme, parsed.netloc, parsed.path, parse_qs(parsed.query)
