# 2075. Decode the Slanted Ciphertext
# see  more about this on leetcode this include image from which you will get better idea about this problem


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        matrix = []
        idx = 0
        for r in range(rows):
            matrix.append(list(encodedText[idx:idx + cols]))
            idx += cols
        
        result = []
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                result.append(matrix[r][c])
                r += 1
                c += 1
        
        return "".join(result).rstrip()

