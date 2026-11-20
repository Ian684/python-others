import re
import sys
# pattern_1 = 'cat'
# pattern_2 = 'dog'
# string = 'dog big'
# 一般
# print(pattern_1 in string)
# print(pattern_2 in string)
# 普通正則
# print(re.search(pattern_1 ,string))
# print(re.search(pattern_2 ,string))
# 多種可能正則
# ptn = r'r[au]n'
# print(re.search(ptn ,'dog runs to cat'))
# 更多種可能正則
# print(re.search(r'r[a-z]n' ,'dog runs to cat'))
# test_str = "請參考 https://www.example.com 或 http://test.org 以獲取更多資訊。"
# r = r'https?://[\w\.]+'
# result = re.findall(r ,test_str)
# print(result)
# test_str = "Hello, Python3! Welcome to 2025."
# r = r'[^a-zA-Z]+'
# result = re.sub(r ,'' ,test_str)
# # print(result)
test_str = "請選擇一個選項 (A) Apple (B) Banana (C) Cherry"
r = r'\(([A-Z])\)'
print(re.findall(r ,test_str))
# text = "This is is a test. Please please check the the result."
# result = re.findall(r'\b(\w+)\b\s+\b\1\b' ,text ,flags=re.IGNORECASE)
# sys.stdout.write(str(result) +'\n')