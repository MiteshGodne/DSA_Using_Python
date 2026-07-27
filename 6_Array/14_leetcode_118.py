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
        
if __name__ == "__main__":
    obj = Solution()    
    print(obj.generate(7))
