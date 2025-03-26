def longestPrefix(s: str) -> str:
    n = len(s)
    lps = [0] * n  # LPS array
    
    j = 0  # Length of the previous longest prefix suffix

    # Build the LPS array
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]  # Fall back to previous prefix suffix

        if s[i] == s[j]:
            j += 1
            lps[i] = j

    # The last value in LPS gives the length of the longest happy prefix
    return s[:lps[-1]]
n = input().strip()
print(longestPrefix(n))
