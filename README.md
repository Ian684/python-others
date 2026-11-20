# Python 日常工具練習

**目前共 50 個實作練習單元。** 完整題號、來源與執行方式見 [CATALOG.md](CATALOG.md)，機器可讀清單見 [EXERCISES.json](EXERCISES.json)。

以下保留起步練習的說明；其餘題目按完整目錄閱讀。

原有爬蟲、文字分析與倉儲檔案保留。新增 tools/ 練習可由命令列使用的工具，需要 Python 3.10 以上，只用標準函式庫。

| 工具 | 輸入與輸出 | 重點 |
|---|---|---|
| word_report | UTF-8 文字 → 詞頻 | Unicode、大小寫合併、同頻排序 |
| expense_report | CSV → 分類支出 | Decimal、日期、列號錯誤 |
| duplicate_files | 目錄 → 重複群組 | 依大小篩選，再串流 SHA256 |

    python -m tools.word_report README.md --top 10
    python -m tools.expense_report examples/expenses.csv
    python -m tools.duplicate_files ./examples
    python -m unittest discover -s tests -v

範例支出輸出 food 205.50、transport 30.00、TOTAL 235.50；假設同一幣別。無效日期、非有限值與超過兩位小數會指出列號，不把錯誤當成 0。

詞頻把連續英數字元或中文字組當成詞，不做中文斷詞；「資料分析」是一個詞。它是文字統計，不是語意分析模型。

重複檔工具不刪除檔案，跳過符號連結，逐塊讀取內容，適用掃描期間不持續變動的本機目錄。測試包含相同大小但不同內容的檔案，並檢查掃描前後資料不變。

原有爬蟲的網路與套件需求獨立；新增測試不會向 Dcard、股市等外部服務送出請求。
