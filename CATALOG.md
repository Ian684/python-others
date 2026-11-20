# 練習目錄

目錄列出各題的實作位置與執行入口。

## 執行與驗證

    python -m unittest discover -s tests -v
    python -m tools.more --list
    python -m tools.more 4 '["  hello   world  "]'

## 題目

| 題號 | 任務／學習重點 | 來源 | 入口 |
|---|---|---|---|
| 01 | 詞頻報告 | [word_report.py](tools/word_report.py) | frequent_words |
| 02 | 支出統計 | [expense_report.py](tools/expense_report.py) | summarize |
| 03 | 重複檔案報告 | [duplicate_files.py](tools/duplicate_files.py) | find_duplicates |
| 04 | 文字空白整理：保留內容、合併空白 | [more.py](tools/more.py) | normalize_spaces |
| 05 | 段落換行：字詞邊界與長單字 | [more.py](tools/more.py) | wrap_paragraph |
| 06 | 網址短名稱：Unicode 正規化與分隔符 | [more.py](tools/more.py) | slugify |
| 07 | 擷取標籤：Unicode 與去重 | [more.py](tools/more.py) | hashtags |
| 08 | 郵件遮罩：保留網域、遮住帳號 | [more.py](tools/more.py) | redact_emails |
| 09 | 電話遮罩：格式清理與保留尾碼 | [more.py](tools/more.py) | mask_phone |
| 10 | 設定檔鍵值：註解、等號與重複鍵 | [more.py](tools/more.py) | parse_properties |
| 11 | 文字行去重：保留順序與非空行 | [more.py](tools/more.py) | deduplicate_lines |
| 12 | 自然檔名排序：數字段按數值比較 | [more.py](tools/more.py) | natural_sort |
| 13 | 資料分批：最後一批不足大小 | [more.py](tools/more.py) | chunks |
| 14 | 單層展平：只展平一層列表 | [more.py](tools/more.py) | flatten_once |
| 15 | 穩定去重：非 hashable 值也可比較 | [more.py](tools/more.py) | unique_values |
| 16 | 記錄分組：同鍵彙整 | [more.py](tools/more.py) | group_records |
| 17 | 建立唯一索引：重複鍵不可靜默覆蓋 | [more.py](tools/more.py) | index_records |
| 18 | 計數合併：整數計數累加 | [more.py](tools/more.py) | merge_counts |
| 19 | CSV 讀取：引號與欄位數 | [more.py](tools/more.py) | csv_records |
| 20 | INI 區段：標準設定解析器 | [more.py](tools/more.py) | ini_sections |
| 21 | 網址參數：保留重複鍵及空值 | [more.py](tools/more.py) | query_parameters |
| 22 | 查詢網址組合：編碼參數而非字串拼接 | [more.py](tools/more.py) | build_url |
| 23 | 網址主機名：user info 與連接埠 | [more.py](tools/more.py) | hostname |
| 24 | Markdown 連結清單：簡單行內連結擷取 | [more.py](tools/more.py) | markdown_links |
| 25 | JSON 格式化：排序鍵與保留 Unicode | [more.py](tools/more.py) | pretty_json |
| 26 | JSON 字典差異：分辨缺少鍵與 null | [more.py](tools/more.py) | changed_keys |
| 27 | 巢狀欄位讀取：路徑列表與預設值 | [more.py](tools/more.py) | deep_get |
| 28 | 巢狀字典合併：不修改原輸入 | [more.py](tools/more.py) | deep_merge |
| 29 | 檔名清理：路徑分隔符與 Windows 保留名 | [more.py](tools/more.py) | safe_filename |
| 30 | 相對路徑整理：拒絕回到父目錄 | [more.py](tools/more.py) | path_components |
| 31 | 副檔名統計：最後一段副檔名與大小寫 | [more.py](tools/more.py) | extension_counts |
| 32 | 容量格式化：二進位 KiB 單位 | [more.py](tools/more.py) | human_bytes |
| 33 | 容量字串解析：單位白名單與整數位元組 | [more.py](tools/more.py) | parse_byte_size |
| 34 | 日期區間：含首尾與跨月 | [more.py](tools/more.py) | date_range |
| 35 | 工作日計數：週末與自訂假日 | [more.py](tools/more.py) | business_days |
| 36 | 月份首末日：閏月與日期驗證 | [more.py](tools/more.py) | month_bounds |
| 37 | 行程衝突：半開時間區間 | [more.py](tools/more.py) | event_conflicts |
| 38 | 時間轉秒：嚴格 HH:MM:SS | [more.py](tools/more.py) | clock_seconds |
| 39 | 秒數格式化：保留超過 24 小時 | [more.py](tools/more.py) | format_duration |
| 40 | 四分位離群值：明確使用 inclusive 四分位 | [more.py](tools/more.py) | iqr_outliers |
| 41 | 移動平均：固定視窗與 running sum | [more.py](tools/more.py) | rolling_average |
| 42 | 長度換算：公尺為共同基準 | [more.py](tools/more.py) | length_conversion |
| 43 | 溫度換算：絕對零度檢查 | [more.py](tools/more.py) | temperature_conversion |
| 44 | 球面距離：角度轉弧度與浮點界限 | [more.py](tools/more.py) | haversine_km |
| 45 | Luhn 檢查碼：交錯倍增與非數字拒絕 | [more.py](tools/more.py) | luhn_valid |
| 46 | ISBN-10 檢查碼：末位 X 的特殊規則 | [more.py](tools/more.py) | isbn10_valid |
| 47 | IPv4 轉整數：標準位址解析 | [more.py](tools/more.py) | ipv4_integer |
| 48 | 網段摘要：network/broadcast/總位址數 | [more.py](tools/more.py) | network_summary |
| 49 | Base64 還原：嚴格驗證與 UTF-8 | [more.py](tools/more.py) | base64_text |
| 50 | ROT13 編碼：可逆轉換不是加密 | [more.py](tools/more.py) | rot13_text |

每個新增單元的正常值與邊界案例可在 tests/、check.py 或 testbench 找到。先預測輸出，再執行，再修改輸入觀察；不是把通過單一範例視為正式部署或線上 AC。
