import math

def max_wire_length(w, heights):
    n = len(heights)
    dp = [[0.0, 0.0] for _ in range(n)]
    
    for i in range(1, n):
        for curr_h in [0, 1]:
            max_len = 0.0
            h2 = 1 if curr_h == 0 else heights[i]
            for prev_h in [0, 1]:
                h1 = 1 if prev_h == 0 else heights[i - 1]
                dist = math.sqrt(w ** 2 + (h2 - h1) ** 2)
                
                max_len = max(max_len, dp[i - 1][prev_h] + dist)
            dp[i][curr_h] = max_len

    return round(max(dp[n - 1][0], dp[n - 1][1]), 2)

if __name__ == "__main__":
    print(max_wire_length(100, [1, 1, 1, 1]))