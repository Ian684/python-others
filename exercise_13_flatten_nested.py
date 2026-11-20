def solve(values):
    result=[]
    for value in values:
        if isinstance(value,list): result.extend(solve(value))
        else: result.append(value)
    return result
