# 先載套件[pip install yfinance pandas matplotlib]
# 從ptt資料公社和yt教學影片學習 按照檔案字典
import yfinance as yf
import matplotlib.pyplot as plt
import platform
# =========================================================怕出現□□□顯示錯誤
if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Microsoft YaHei"
elif platform.system() == "Darwin": 
    plt.rcParams["font.family"] = "Arial Unicode MS"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK"
# Window macOS Linux常用三種系統的字體轉換
plt.rcParams["axes.unicode_minus"] = False
# 負號問題
# =========================================================爬取資料
stock_name = input("請輸入股票代碼(例如TSM):").upper()
# 都轉大寫
start_date = input("請輸入開始日期(格式YYYY-MM-DD):")
end_date = input("請輸入結束日期(格式YYYY-MM-DD):")
try:
    data = yf.download(stock_name, start=start_date, end=end_date)
# 從yahoo finance擷取
    if data.empty:
        print("股票代碼錯誤或無數據，請檢查代碼和日期範圍！")
        exit()
except Exception as e:
    print(f"錯誤發生：{e}")
    exit()
# 輸出錯誤訊息
# =========================================================均線計算
days = []
while True:
    day = input("請輸入均線天數(輸入q結束):")
    if day == "q":
        break
    else:
        if day.isdigit():
           days.append(int(day))
        else:
            print(f"輸入錯誤：'{day}' 不是數字，請重新輸入！")
# 確保輸入的是數字
for i in days:
    data[f"{i}日"] = data["Close"].rolling(window=i).mean()
# 計算移動平均值
# =========================================================均線和股價繪製
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Close"], label="收盤價", color="blue")
# 設計股價圖表
for i in days:
    plt.plot(data.index, data[f"{i}日"], label=f"{i}日均線", linestyle="dashed")
# 加入平均線
plt.title(f"{stock_name} 股票價格與移動平均線 ({start_date} - {end_date})", fontsize=14)
plt.xlabel("日期", fontsize=12)
plt.ylabel("價格 (USD)", fontsize=12)
# 設定座標意義和標題
plt.legend()
plt.grid()
plt.show()
# 設定顯示圖例和網格並顯示
# =========================================================回報率計算與繪製
data["Return"] = data["Close"].pct_change()
# 計算漲跌幅(今天-昨天)/昨天
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Return"], label="每日回報率", color="purple")
# 設計回報率圖表
plt.title(f"{stock_name} 每日回報率", fontsize=14)
plt.xlabel("日期", fontsize=12)
plt.ylabel("回報率", fontsize=12)
# 設定座標意義和標題
plt.legend()
plt.grid()
plt.show()
# 設定顯示圖例和網格並顯示
