class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        if n == 1 or n == 2:
            return True
        res = [False] * (n + 1)
        res[1] = True
        res[2] = True
        for i in range(3, n + 1):
		res[i] = (res[i-1] == False) or (res[i-2] == False)
        return res[-1]
