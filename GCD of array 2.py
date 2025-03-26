def gcd(a,b):
    while(b!=0):
        a,b = b,a%b
    return a

def func(arr):
    res=arr[0]
    for i in range(1,len(arr)):
        res = gcd(res,arr[i])
    return res

n = int(input())
arr = list(map(int,input().split()))
print(func(arr))
