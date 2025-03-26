def dnfAlgo(list):
    low = 0
    mid =0
    high = len(list)-1
    
    while(mid<=high):
        if(list[mid]==0):
            list[low], list[mid] = list[mid], list[low]
            low +=1
            mid += 1
        elif(list[mid]==1):
            mid += 1
        else:
            list[mid], list[high] = list[high], list[mid]
            high -= 1
    return list 

n = int(input())
arr = list(map(int,input().split()))
print(*dnfAlgo(arr))
