
class Solution:
    def generate(self, numRows):
        triangle = []

        for row in range(numRows):
            # البداية: صف جديد كله 1
            new_row = [1] * (row + 1)

            # نملأ الوسط فقط إذا الصف أكبر من 2 عناصر
            for i in range(1, row):
                new_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]

            triangle.append(new_row)

        return triangle
