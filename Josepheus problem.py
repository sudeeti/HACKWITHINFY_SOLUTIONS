def josephus(n, k):
    position = 0  # Josephus position starts from 0 in zero-based index
    for i in range(2, n + 1):
        position = (position + k) % i
    return position + 1  # Converting zero-based index to one-based index

# Input
n = int(input())
k = int(input())

# Output
print(josephus(n, k))
