def maximum(arr):
    min = float('inf')
    max = 0
    for i in arr:
        if i<min:
            min=i
        elif i-min > max:
            max = i-min
    return max

n = int(input())
arr = list(map(int,input().split()))
print(maximum(arr))
