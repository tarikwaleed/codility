"""
O(n^2)
80% correctness
25% performance
55% totoal score
https://app.codility.com/demo/results/trainingP4CNEN-5AG/
"""
# def solution(arr):
#     poped_elements=[]
#     while(arr):
#         try:
#             arr[1:].index(arr[0])
#             poped_elements.append(arr.pop(0))
#         except ValueError as e:
#             if arr[0] not in poped_elements:
#                 return arr[0]
#             else:
#                 arr.pop(0)


"""
O(n^2)
100% correctness
25% performance
66% totoal score
https://app.codility.com/demo/results/training56HFZ9-BSX/
"""
# def solution(arr):
#     arr.sort()
#     while(arr):
#         try:
#             arr[1:].index(arr[0])
#             arr.pop(0)
#             arr.pop(0)
#         except ValueError as e:
#             return arr[0]

"""
O(n^2)
100% correctness
25% performance
66% totoal score
https://app.codility.com/demo/results/training56HFZ9-BSX/

"""
# def solution(arr):
#     arr.sort()
#     while(arr):
#         if len(arr)==1:
#             return arr[0]
#         if arr[0]==arr[1]:
#             arr.pop(0)
#             arr.pop(0)
#         else:
#             return arr[0]
"""
Final solution
Detected time complexity:
O(N) or O(N*log(N))
100%
https://app.codility.com/demo/results/training5XXYTA-ARH/
"""
def solution(a):
    a.sort()
    a.append(-1)
    for i in range(0,len(a),2):
        if a[i]!=a[i+1]:
            return a[i]
# Test Cases
print(solution([10, 17, 16, 10, 17, 30, 30]))  # Expected Output: 16
print(solution([5, 5, 7, 7, 8, 9, 9]))         # Expected Output: 8
print(solution([1, 2, 3, 4, 5, 1, 2, 3, 4]))   # Expected Output: 5
print(solution([100, 200, 300, 200, 100]))     # Expected Output: 300
print(solution([9, 9, 8, 7, 8]))               # Expected Output: 7
print(solution([15, 23, 15, 23, 27, 27, 30]))  # Expected Output: 30
print(solution([42]))                          # Expected Output: 42
print(solution([4, 4, 6, 6, 8, 8, 8, 8, 10]))  # Expected Output: 10
