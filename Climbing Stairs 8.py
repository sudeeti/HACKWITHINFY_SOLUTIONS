def climb_stairs(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Input
n = int(input())

# Output
print(climb_stairs(n))
