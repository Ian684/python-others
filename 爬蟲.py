import requests
from bs4 import BeautifulSoup
import csv
# 1.提取目標網址內容2.解析html檔案3.輸出檔案為csv
# ======================================================================提取
destination = input('輸入網址與目標行數:').split()
place,quantity = destination[0],int(destination[1])
headers = {
    "User-Agent": "Mozilla/5.0"
}
# 偽裝真人

response = requests.get(place, headers=headers)
# 要求提取
# ======================================================================解析
if response.status_code == 200:
# 判斷 200 404 500 或其他狀況

    archive = BeautifulSoup(response.text, "html.parser")
# 用內建解析器

    title = archive.find("h1").text
    print("頁面標題:", title) 
# <h1>標題  <P>段落  <a>超鏈結  <img>圖像  <table>表格

    paragraphs = archive.find_all("p")
    content = []
    for p in paragraphs[:quantity]:
        content.append(p.text.strip())
# 前後空白問題 
# ======================================================================輸出
    with open("statistics.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["標題", "內容"])
        for para in content:
            writer.writerow([title, para])
# 創建寫入器並寫入statistics.csv

    print("數據已儲存到 statistics.csv")
else:
    print("請求失敗，狀態碼:", response.status_code)
