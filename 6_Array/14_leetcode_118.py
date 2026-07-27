'''Given an integer numRows, return the first numRows of Pascal's triangle.'''
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(pascal[i-1][j-1] + pascal[i-1][j])
            pascal.append(row)
        return pascal
        
    def getNthRow(self, N: int) -> list[int]:
        row = []
        val = 1
        row.append(val)
        for k in range(1, N):
            val = val * (N-k)//k
            row.append(val)
        return row
    
    def findPascalElement(self, r: int, c: int) -> int:
        n = r-1
        k = c-1
        res = 1
        for i in range(k):
            res *= n-i
            res //= (i+1)
        return res

if __name__ == "__main__":
    obj = Solution()    
    print(obj.generate(7))
    print(obj.getNthRow(6))
    print(obj.findPascalElement(6,4))
