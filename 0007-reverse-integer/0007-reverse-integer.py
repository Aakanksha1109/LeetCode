class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x<0
        x = abs(x)

        reversenum = 0
        while x!= 0:
            reversenum = reversenum*10 + (x % 10)
            x//=10

        if is_neg :
            reversenum = -reversenum
        
        if reversenum < -2**31 or reversenum > 2**31 - 1:
            return 0

        return reversenum