def maximum_subarray(list):
    maxSum = list[0]
    currSum = list[0]
    
    for i in range(1,len(list)):
        currSum = max(currSum+list[i],list[i])
        maxSum= max(currSum,maxSum)
    return maxSum  
n = int(input())
arr = list(map(int,input().split()))
print(maximum_subarray(arr))
    
