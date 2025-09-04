class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        text = list(str(abs_x))
        
        total = 0
        for i, s in enumerate(text):
            digit = 10 ** i if i >0 else 1
            total += self.getSum(digit, int(s))

        result = total*-1 if x < 0 else total
        if result >= -2**31 and result <= 2**31-1:
            return result
        else:
            return 0
        
    def getSum(self, digit:int, n:int) -> int:
        return n * digit