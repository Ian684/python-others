import binascii
import calendar
import codecs
import collections
import configparser
import copy
import csv
import datetime
import decimal
import io
import ipaddress
import json
import math
import pathlib
import re
import statistics
import textwrap
import unicodedata
import urllib.parse

def normalize_spaces(text):
    """所有 Unicode 空白合併成單一空格，去除兩端。"""
    return ' '.join(text.split())

def wrap_paragraph(text, width):
    """按單字折行，不拆開超長單字；width>0。"""
    if width < 1:
        raise ValueError('positive width required')
    return textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)

def slugify(text):
    """轉為 ASCII 小寫 slug；非英數以 - 分隔。"""
    normalized = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower()
    return re.sub('[^a-z0-9]+', '-', normalized).strip('-')

def hashtags(text):
    """擷取 # 後的 Unicode 字母數字底線，依首次出現排序。"""
    return list(dict.fromkeys(re.findall('(?<!\\w)#(\\w+)', text)))

def redact_emails(text):
    """替換常見 email 的帳號；非完整 RFC email 解析器。"""
    return re.sub('[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\\.[A-Za-z]{2,})', '***@\\1', text)

def mask_phone(text):
    """只保留數字，至少 4 位，其餘以 * 隱藏。"""
    digits = ''.join((c for c in text if c.isascii() and c.isdigit()))
    if len(digits) < 4:
        raise ValueError('at least four digits required')
    return '*' * (len(digits) - 4) + digits[-4:]

def parse_properties(text):
    """每行 key=value，略過空行與 # 註解；重複鍵拒絕。"""
    result = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, separator, value = line.partition('=')
        if not separator or not key.strip() or key.strip() in result:
            raise ValueError('invalid or duplicate key')
        result[key.strip()] = value.strip()
    return result

def deduplicate_lines(text):
    """每行去除兩端空白，去掉空行，保留第一次出現。"""
    return list(dict.fromkeys((line.strip() for line in text.splitlines() if line.strip())))

def natural_sort(names):
    """對相同大小寫視為相等的 ASCII 數字段做自然排序。"""
    key = lambda name: [(1, int(part)) if part.isdigit() else (0, part.casefold()) for part in re.split('([0-9]+)', name)]
    return sorted(names, key=key)

def chunks(values, size):
    """正整數批次大小，最後一批可較短。"""
    if size < 1:
        raise ValueError('positive chunk size required')
    return [values[i:i + size] for i in range(0, len(values), size)]

def flatten_once(rows):
    """每一列必須是 list，保留更深一層結構。"""
    if any((not isinstance(row, list) for row in rows)):
        raise ValueError('list rows required')
    return [value for row in rows for value in row]

def unique_values(values):
    """保留首次出現，支援列表等不可雜湊的 JSON 值；O(n²)。"""
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result

def group_records(records, key):
    """依字串欄位分組，缺少欄位拋錯。"""
    result = {}
    for record in records:
        result.setdefault(str(record[key]), []).append(record)
    return result

def index_records(records, key):
    """用字串欄位建立索引，重複值拋錯。"""
    result = {}
    for record in records:
        value = str(record[key])
        if value in result:
            raise ValueError('duplicate key')
        result[value] = record
    return result

def merge_counts(reports):
    """合併字串到非負整數的字典，按鍵排序。"""
    result = collections.Counter()
    for report in reports:
        if any((not isinstance(v, int) or v < 0 for v in report.values())):
            raise ValueError('non-negative integer counts required')
        result.update(report)
    return dict(sorted(result.items()))

def csv_records(text):
    """有標頭的 CSV 轉成記錄；拒絕重複欄名與長短不符。"""
    rows = list(csv.reader(io.StringIO(text)))
    if not rows:
        return []
    header = rows[0]
    if len(set(header)) != len(header) or any((len(r) != len(header) for r in rows[1:])):
        raise ValueError('invalid CSV shape')
    return [dict(zip(header, row)) for row in rows[1:]]

def ini_sections(text):
    """INI 解析為區段字典，不啟用 interpolation。"""
    parser = configparser.ConfigParser(interpolation=None)
    parser.read_string(text)
    return {section: dict(parser[section]) for section in parser.sections()}

def query_parameters(url):
    """URL query 解析為 key -> 值列表，保留空值。"""
    return urllib.parse.parse_qs(urllib.parse.urlsplit(url).query, keep_blank_values=True)

def build_url(base, parameters):
    """保留原 query，加入字典參數；列表值展開，保留 fragment。"""
    parts = urllib.parse.urlsplit(base)
    pairs = urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
    pairs.extend(((k, item) for k, value in parameters.items() for item in (value if isinstance(value, list) else [value])))
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(pairs)))

def hostname(url):
    """回傳 HTTP(S) 網址的 hostname；不連線網路。"""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ('http', 'https') or not parts.hostname:
        raise ValueError('HTTP(S) URL required')
    return parts.hostname

def markdown_links(text):
    """擷取不含巢狀括號的 [標籤](目標)，忽略圖片。"""
    return [list(match) for match in re.findall('(?<!!)\\[([^\\]]+)\\]\\(([^\\s)]+)\\)', text)]

def pretty_json(text):
    """有效 JSON 格式化為兩空格縮排。"""
    return json.dumps(json.loads(text), ensure_ascii=False, sort_keys=True, indent=2)

def changed_keys(before, after):
    """回傳新增、刪除或值改變的頂層鍵，按字典序。"""
    missing = object()
    return sorted((k for k in set(before) | set(after) if before.get(k, missing) != after.get(k, missing)))

def deep_get(data, path, default=None):
    """path 是字典鍵列表；不把包含 . 的鍵拆開。"""
    for key in path:
        if not isinstance(data, dict) or key not in data:
            return default
        data = data[key]
    return data

def deep_merge(before, after):
    """字典遞迴合併，其餘值由 after 取代。"""
    result = copy.deepcopy(before)
    for key, value in after.items():
        result[key] = deep_merge(result[key], value) if isinstance(result.get(key), dict) and isinstance(value, dict) else copy.deepcopy(value)
    return result

def safe_filename(name):
    """產生單一檔名，不產生或移動檔案。"""
    cleaned = re.sub('[<>:"/\\\\|?*\\x00-\\x1f]', '_', name).strip(' .')
    if not cleaned:
        cleaned = 'untitled'
    if cleaned.split('.')[0].upper() in {'CON', 'PRN', 'AUX', 'NUL', *(f'COM{i}' for i in range(1, 10)), *(f'LPT{i}' for i in range(1, 10))}:
        cleaned = '_' + cleaned
    return cleaned

def path_components(text):
    """以 / 分隔，相對路徑移除 . 與空段；禁止 .. 或絕對路徑。"""
    if text.startswith('/') or '\\' in text:
        raise ValueError('relative POSIX path required')
    parts = [part for part in text.split('/') if part not in ('', '.')]
    if '..' in parts:
        raise ValueError('parent traversal forbidden')
    return parts

def extension_counts(names):
    """檔名列表副檔名計數，無副檔名使用空字串。"""
    counts = collections.Counter((pathlib.PurePath(name).suffix.lower() for name in names))
    return dict(sorted(counts.items()))

def human_bytes(size):
    """非負位元組數，最大使用 TiB，固定兩位小數。"""
    if size < 0:
        raise ValueError('negative size')
    value = float(size)
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    index = 0
    while value >= 1024 and index < len(units) - 1:
        value /= 1024
        index += 1
    return f'{value:.2f} {units[index]}'

def parse_byte_size(text):
    """例如 1.5 KiB；禁止無法整除成位元組的大小。"""
    match = re.fullmatch('(\\d+(?:\\.\\d+)?)\\s*(B|KiB|MiB|GiB)', text.strip())
    if not match:
        raise ValueError('invalid size')
    units = {'B': 1, 'KiB': 1024, 'MiB': 1024 ** 2, 'GiB': 1024 ** 3}
    size = decimal.Decimal(match[1]) * units[match[2]]
    if size != size.to_integral_value():
        raise ValueError('fractional byte')
    return int(size)

def date_range(start, end):
    """ISO 日期，包含兩端；最多 3660 天避免過大輸出。"""
    a, b = (datetime.date.fromisoformat(start), datetime.date.fromisoformat(end))
    days = (b - a).days
    if not 0 <= days <= 3660:
        raise ValueError('invalid date range')
    return [(a + datetime.timedelta(days=i)).isoformat() for i in range(days + 1)]

def business_days(start, end, holidays):
    """含首尾，排除週六日與給定 ISO 假日。"""
    excluded = set(holidays)
    return sum((datetime.date.fromisoformat(day).weekday() < 5 and day not in excluded for day in date_range(start, end)))

def month_bounds(year, month):
    """回傳月份第一天與最後一天的 ISO 日期。"""
    last = calendar.monthrange(year, month)[1]
    return [datetime.date(year, month, 1).isoformat(), datetime.date(year, month, last).isoformat()]

def event_conflicts(events):
    """[開始分鐘,結束分鐘]，輸出相交事件的索引對。"""
    if any((a >= b for a, b in events)):
        raise ValueError('positive event duration required')
    return [[i, j] for i in range(len(events)) for j in range(i + 1, len(events)) if max(events[i][0], events[j][0]) < min(events[i][1], events[j][1])]

def clock_seconds(text):
    """24 小時時間字串轉午夜後秒數。"""
    if not re.fullmatch('\\d{2}:\\d{2}:\\d{2}', text):
        raise ValueError('HH:MM:SS required')
    h, m, s = map(int, text.split(':'))
    if h >= 24 or m >= 60 or s >= 60:
        raise ValueError('invalid time')
    return h * 3600 + m * 60 + s

def format_duration(seconds):
    """非負整數秒數轉 H:MM:SS，不把時數取 24 餘數。"""
    if seconds < 0:
        raise ValueError('negative duration')
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f'{hours}:{minutes:02}:{seconds:02}'

def iqr_outliers(values):
    """至少兩值，inclusive quartiles 的 1.5 IQR 範圍外資料。"""
    if len(values) < 2:
        raise ValueError('two measurements required')
    q1, _, q3 = statistics.quantiles(values, n=4, method='inclusive')
    spread = q3 - q1
    return [x for x in values if x < q1 - 1.5 * spread or x > q3 + 1.5 * spread]

def rolling_average(values, width):
    """完整視窗平均，回傳到六位小數；1<=width<=len。"""
    if not 1 <= width <= len(values):
        raise ValueError('invalid window')
    total = sum(values[:width])
    result = [round(total / width, 6)]
    for i in range(width, len(values)):
        total += values[i] - values[i - width]
        result.append(round(total / width, 6))
    return result

def length_conversion(value, source, target):
    """m,cm,mm,km,inch,foot；結果取六位小數。"""
    units = {'m': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000, 'inch': 0.0254, 'foot': 0.3048}
    return round(value * units[source] / units[target], 6)

def temperature_conversion(value, source, target):
    """C/F/K，禁止低於絕對零度。"""
    if source not in ('C', 'F', 'K') or target not in ('C', 'F', 'K'):
        raise ValueError('unknown unit')
    c = value if source == 'C' else (value - 32) * 5 / 9 if source == 'F' else value - 273.15
    if c < -273.15 - 1e-09:
        raise ValueError('below absolute zero')
    return round(c if target == 'C' else c * 9 / 5 + 32 if target == 'F' else c + 273.15, 6)

def haversine_km(a, b):
    """[緯度,經度]，球體半徑 6371km 的大圓距離。"""
    if any((not -90 <= p[0] <= 90 or not -180 <= p[1] <= 180 for p in (a, b))):
        raise ValueError('invalid coordinates')
    lat1, lat2 = map(math.radians, (a[0], b[0]))
    dlat = lat2 - lat1
    dlon = math.radians(b[1] - a[1])
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return round(6371 * 2 * math.asin(math.sqrt(min(1, max(0, h)))), 3)

def luhn_valid(text):
    """檢查數字字串，不儲存或傳送資料。"""
    if not text or not text.isascii() or (not text.isdigit()):
        return False
    total = 0
    for i, char in enumerate(reversed(text)):
        value = int(char) * (2 if i % 2 else 1)
        total += value - 9 if value > 9 else value
    return total % 10 == 0

def isbn10_valid(text):
    """略過連字號，只允許最後一碼為 X。"""
    digits = text.replace('-', '').upper()
    if not re.fullmatch('[0-9]{9}[0-9X]', digits):
        return False
    return sum(((10 - i) * (10 if c == 'X' else int(c)) for i, c in enumerate(digits))) % 11 == 0

def ipv4_integer(text):
    """IPv4 -> 32 位元整數；不解析主機名。"""
    return int(ipaddress.IPv4Address(text))

def network_summary(cidr):
    """IPv4 CIDR，strict=False 允許輸入主機位址。"""
    network = ipaddress.IPv4Network(cidr, strict=False)
    return {'network': str(network.network_address), 'broadcast': str(network.broadcast_address), 'addresses': network.num_addresses}

def base64_text(text):
    """Strict Base64 syntax, then UTF-8 decoding; avoids the legacy base64.py name."""
    if not re.fullmatch('(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?', text):
        raise ValueError('invalid Base64')
    return binascii.a2b_base64(text).decode('utf-8')

def rot13_text(text):
    """只改英文字母，保留中文與其他字元。"""
    return codecs.encode(text, 'rot_13')

def main():
    import argparse
    import json
    from pathlib import Path
    parser = argparse.ArgumentParser(description='Numbered practice exercises; arguments are a JSON array')
    parser.add_argument('exercise', nargs='?')
    parser.add_argument('arguments', nargs='?', default='[]')
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()
    catalog = json.loads((Path(__file__).resolve().parents[1] / 'curriculum.json').read_text(encoding='utf-8'))
    if args.list:
        for item in catalog:
            print(str(item['id']) + ': ' + item['title'] + ' (' + item['function'] + ')')
        return
    item = next((item for item in catalog if str(item['id']) == args.exercise), None)
    if item is None:
        parser.error('Unknown exercise; use --list')
    arguments = json.loads(args.arguments)
    if not isinstance(arguments, list):
        parser.error('Arguments must be a JSON array')
    print(json.dumps(globals()[item['function']](*arguments), ensure_ascii=False))
if __name__ == '__main__':
    main()
