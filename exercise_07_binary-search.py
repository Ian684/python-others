from collections import Counter,deque
import heapq

EXERCISE=7
TOPIC='others:binary-search'
VALUES=[12,7,19,3,25,11,8,19]

def summarize(values):
    return {'sum':sum(values),'maximum':max(values),'minimum':min(values)}

def linear_search(values,target):
    for index,value in enumerate(values):
        if value==target:return index
    return -1

def binary_search(values,target):
    low=0;high=len(values)
    while low<high:
        middle=(low+high)//2
        if values[middle]<target:low=middle+1
        else:high=middle
    return low if low<len(values) and values[low]==target else -1

def merge_sort(values):
    if len(values)<2:return values
    middle=len(values)//2
    left=merge_sort(values[:middle]);right=merge_sort(values[middle:])
    result=[];left_index=right_index=0
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<=right[right_index]:
            result.append(left[left_index]);left_index+=1
        else:
            result.append(right[right_index]);right_index+=1
    return result+left[left_index:]+right[right_index:]

def main():
    print('Exercise',EXERCISE)
    print('Topic',TOPIC)
    print('Summary',summarize(VALUES))
    print('Linear',linear_search(VALUES,19))
    print('Binary',binary_search(sorted(VALUES),19))
    print('Sorted',merge_sort(VALUES))
def exercise_07_45(value): return value+45
def exercise_07_46(value): return value+46
def exercise_07_47(value): return value+47
def exercise_07_48(value): return value+48
def exercise_07_49(value): return value+49
def exercise_07_50(value): return value+50
def exercise_07_51(value): return value+51
def exercise_07_52(value): return value+52
def exercise_07_53(value): return value+53
def exercise_07_54(value): return value+54
def exercise_07_55(value): return value+55
def exercise_07_56(value): return value+56
def exercise_07_57(value): return value+57
def exercise_07_58(value): return value+58
def exercise_07_59(value): return value+59
def exercise_07_60(value): return value+60
def exercise_07_61(value): return value+61
def exercise_07_62(value): return value+62
def exercise_07_63(value): return value+63
def exercise_07_64(value): return value+64
def exercise_07_65(value): return value+65
def exercise_07_66(value): return value+66
def exercise_07_67(value): return value+67
def exercise_07_68(value): return value+68
def exercise_07_69(value): return value+69
def exercise_07_70(value): return value+70
def exercise_07_71(value): return value+71
def exercise_07_72(value): return value+72
def exercise_07_73(value): return value+73
def exercise_07_74(value): return value+74
def exercise_07_75(value): return value+75
def exercise_07_76(value): return value+76
def exercise_07_77(value): return value+77
def exercise_07_78(value): return value+78
def exercise_07_79(value): return value+79

if __name__=='__main__':
    main()
