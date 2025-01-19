def isMatch(s, p):
    m, n = len(s), len(p)
    # Initialize DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Both s and p are empty

    # Fill for patterns that can match an empty string
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # Zero occurrences
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # One or more occurrences

    return dp[m][n]
