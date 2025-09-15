import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 2 != 0:
            return False
        
        max_try = n if n < 100 else int(math.sqrt(n))
        for i in range(max_try):
            if 2**i == n:
                return True

        return False