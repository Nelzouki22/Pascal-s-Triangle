# 🔢 LeetCode 118 – Pascal's Triangle  
### 🐍 Python Solution + Arabic & English Explanation

---

## 📘 وصف المشكلة (الترجمة العربية)

معطى رقم `numRows`، المطلوب هو إنشاء **أول numRows من مثلث باسكال**.

في مثلث باسكال:

- الصف الأول يبدأ بـ `[1]`
- كل رقم يساوي **مجموع الرقمين فوقه مباشرة**
- أول وآخر عنصر في كل صف هما دائمًا `1`

مثال:

 1
1 1

---

## 📘 Problem Description (English)

Given an integer `numRows`, return the first `numRows` of **Pascal's Triangle**.

Each number is the sum of the two numbers directly above it.

---

## 📌 Examples

### Example 1  
Input:
numRows = 5
Output:
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

### Example 2  
Input:
numRows = 1
Output:
[[1]]

---

## 🧠 الفكرة الأساسية للحل (شرح مبسّط للمبتدئين)

لفهم مثلث باسكال:

1. الصف الأول دائمًا: `[1]`
2. كل صف جديد يعتمد على الصف السابق:
   - أول عنصر = `1`
   - آخر عنصر = `1`
   - باقي العناصر:
     ```
     new_row[i] = last_row[i - 1] + last_row[i]
     ```

نستخدم **قائمة ثنائية الأبعاد** (List of Lists).

---

# 🧩 كود الحل بلغة Python

ضع هذا الكود في ملف باسم:

solution.py

```python
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
🚀 كيفية تشغيل الكود

حفظ ملف solution.py

تشغيله عبر Python:
python solution.py

يمكنك تجربة:
s = Solution()
print(s.generate(5))
📊 Time & Space Complexity
النوع	القيمة
Time Complexity	O(n²)
Space Complexity	O(n²)

لأن المثلث يحتوي على (1 + 2 + … + n) عناصر.

🙌 المؤلف

Project created by Nadir Elzouki
Feel free to fork, star ⭐, or open issues!
