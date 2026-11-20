import nltk
nltk.download('vader_lexicon')
# 下載VADER資料
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from snownlp import SnowNLP
from langdetect import detect, LangDetectException
# 依照需求使用三種套件 並用langdetect判斷中英
try:
    choice = input('輸入要進行[a.文本分析]還是[b.聊天分析]:').lower()
    text = input('輸入需要分析的資料(請大於五個字):')
# choice_1先判斷長篇短篇 choice_2再判斷中英文
    if choice == 'a':
        score = TextBlob(text).sentiment.polarity
# 先把內容轉換成TextBlob檔案再從sentiment取出polarity
    elif choice =='b':
        try:
            lang = detect(text)
            if lang == 'ko':
                score = ((SnowNLP(text).sentiments)*2)-1
# 處理原本不符合-1到1的數據
            elif lang == 'en':
                score =  SentimentIntensityAnalyzer().polarity_scores(text)['compound']
            
# 用分析器分析情緒數值並取出compound的數值
        except LangDetectException as e:
            print('無法辨識語言，請輸入中文或英文')
            exit()
    else:
        print('輸入錯誤!!!')
    if score > 0:
        result = '正向情緒'
    elif score < 0:
        result = '負向情緒'
    else:
        result = '無情緒'
    print(f'情緒值:{score:.2f},分析結果為:{result}')
except NameError:
    print('字數太少!!!')
except Exception as e:
    print(f'發生{e}錯誤!!!')
    exit()
