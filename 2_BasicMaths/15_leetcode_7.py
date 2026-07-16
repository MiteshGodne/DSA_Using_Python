# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 + 1
        rev = 0
        num = abs(x)
        while num > 0:
            digit = num % 10 
            num //= 10
            if rev > (MAX - digit) // 10:
                return 0
            rev = rev*10 + digit
        return rev if x >= 0 else rev*(-1)
    
        # Optimized 
    def reverse_v2(self, x: int) -> int:
        a=""
        k=""
        for i in str(x):
            if i.isdigit():
                k=k+str(i)
                print(k)
            else:
                a+=str(i)
        q=int(a+k[::-1]) 
        if q > -2147483648  and  q<2147483647:
            return q
        return 0
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.reverse(1644684))