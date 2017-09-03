class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        res = [[False for _ in range(m+1)] for _ in range(n + 1)]
        res[0][0] = True
        for i in range(1, n+1):
            for j in range(0, m +1):
                res[i][j] = res[i-1][j]
                if j >= A[i-1]:
                    res[i][j] |= res[i-1][j - A[i-1]]
        for i in range(m, -1, -1):
            if res[n][i]:
                return i
