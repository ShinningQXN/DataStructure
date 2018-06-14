# 【描述】：两个array最长的match的subarray
#         leetcode 718. Maximum Length of Repeated Subarray

# 【算法】：
# 1.match请用dp， 连续match只需考虑dp[i-1][j-1]
# 【易错】：
# 不一定return dp[n][m]

