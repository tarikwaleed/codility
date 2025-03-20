def solution(a):
    n=len(a)
    s=sum(a)
    min_diff=2000
    sl=0
    for p in range(1,n):
        sl+=a[p]
        diff=abs(s-2*sl)
        min_diff=min(min_diff,diff)
    return min_diff


