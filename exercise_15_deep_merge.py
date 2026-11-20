def solve(left,right):
    result=left.copy()
    for key,value in right.items():
        if key in result and isinstance(result[key],dict) and isinstance(value,dict): result[key]=solve(result[key],value)
        else: result[key]=value
    return result
