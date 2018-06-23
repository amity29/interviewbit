class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        x = x - (d * (x / d))
        if n == 1:
            return x
        if n == 0:
            return 1 if x != 0 else 0
        extra = x if n - (2 * (n /2)) == 1 else 1
        sol = extra * self.pow(x * x, n/2, d)
        return sol - (d * (sol / d))
