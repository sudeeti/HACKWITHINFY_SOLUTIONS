def rob_max_money(n, nums):
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    prev2 = 0  # Represents dp[i-2]
    prev1 = 0  # Represents dp[i-1]

    for num in nums:
        current = max(prev1, prev2 + num)  # Either rob current house or skip
        prev2 = prev1  # Move the window forward
        prev1 = current

    return prev1  # The last value holds the max money robbed

# Read input
n = int(input().strip())
nums = list(map(int, input().strip().split()))

# Output result
print(rob_max_money(n, nums))
