class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        res = [0 for _ in range(m + 1)]
        ans = 0
        res[0] = 1
        for item in A:
            for i in range(m, -1, -1):
                if i >= item and res[i-item] > 0:
                    ans = max(ans, i)
                    res[i] = 1
        return ans
