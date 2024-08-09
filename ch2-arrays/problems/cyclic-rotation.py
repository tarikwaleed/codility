def solution(arr,k):
    a=len(arr)
    new_arr=arr.copy()
    for i in range(a):
        new_index= (i+k)%a
        new_arr[new_index]=arr[i]
    return new_arr

    

