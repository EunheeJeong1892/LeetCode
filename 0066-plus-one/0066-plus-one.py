class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        to_string = lambda lst: ''.join(map(str, lst))
        to_digits = lambda s: list(map(int, s))
        return to_digits(str(int(to_string(digits)) + 1))

        

        