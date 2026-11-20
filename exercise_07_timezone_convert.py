from datetime import datetime
from zoneinfo import ZoneInfo
def solve(text, source, target):
    return datetime.fromisoformat(text).replace(tzinfo=ZoneInfo(source)).astimezone(ZoneInfo(target)).isoformat()
