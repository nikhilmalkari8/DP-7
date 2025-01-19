def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,  # Replace
                    dp[i][j - 1] + 1,      # Insert
                    dp[i - 1][j] + 1       # Delete
                )

    return dp[m][n]
