def solution(n):
    ones_indeces=[]
    binary=bin(n)[2:]
    for index,digit in enumerate(binary):
        if digit=='1':
            ones_indeces.append(index)
    max_diff=0
    for i in range(len(ones_indeces)-1):
        diff=ones_indeces[i+1]-ones_indeces[i]
        max_diff=max(max_diff,diff)
    return max_diff-1 if max_diff>0 else  0
a=solution(1041)
print(a)
