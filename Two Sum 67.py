def two_sum(list,target):
    diff_dict={}
    for i in range(0,len(list)):
        diff = target - list[i]
        if diff in diff_dict:
            return diff_dict[diff],i
        diff_dict[list[i]]=i
        
n = int(input())
arr = list(map(int,input().split()))
tar = int (input())

response = two_sum(arr,tar)
print(response[0],response[1])
