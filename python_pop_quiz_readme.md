# 🧠 Python Pop Quiz (Experienced Beginner)
**Total Marks: 30**  
**Topics Covered:** Loops, Control Flow, Dictionaries  
**Instructions:**  
- Answer all questions.  
- Show workings where necessary.  
- Code must be syntactically correct.  

---

## ✏️ Section A: Multiple Choice (6 Marks)

**1.** What will the following code output? (2 marks)
```python
for i in range(1, 5):
    if i % 2 == 0:
        print(i)
```
A. 1 2 3 4  
B. 2 4  
C. 1 3  
D. 4  

---

**2.** What does `break` do in a loop? (2 marks)  
A. Skips the current iteration  
B. Ends the loop completely  
C. Restarts the loop  
D. Pauses execution  

---

**3.** What is the output? (2 marks)
```python
x = {"a": 1, "b": 2}
print(x.get("c", 0))
```
A. None  
B. Error  
C. 0  
D. 1  

---

## ✏️ Section B: Short Answer (10 Marks)

**4.** Explain the difference between `break` and `continue`. (3 marks)

---

**5.** Write a `for` loop that prints numbers from 10 to 1 (descending). (3 marks)

---

**6.** Given the dictionary:
```python
student = {"name": "Alex", "marks": 75}
```
Add a new key `"grade"` with value `"B"`. (2 marks)

---

**7.** What will this code output? (2 marks)
```python
for i in range(3):
    print(i)
else:
    print("Done")
```

---

## 💻 Section C: Coding Questions (14 Marks)

**8.** Write a program that:
- Uses a loop to calculate the sum of numbers from 1 to 10  
(4 marks)

---

**9.** Write a program that:
- Takes a dictionary of items and prices  
- Prints only items that cost more than 50  

Example:
```python
items = {"bread": 20, "milk": 60, "eggs": 55}
```
Expected Output:
```
milk
eggs
```
(5 marks)

---

**10.** Write a program that:
- Counts how many vowels are in a string  
- Uses a loop and conditional statements  

Example:
```
Input: "hello world"
Output: 3
```
(5 marks)

---

# ✅ MEMORANDUM (ANSWER KEY)

## Section A

**1.** B (2, 4) ✔ (2 marks)  
**2.** B (Ends the loop completely) ✔ (2 marks)  
**3.** C (0) ✔ (2 marks)  

---

## Section B

**4.**
- `break`: Stops the loop entirely  
- `continue`: Skips current iteration and continues  
✔ (3 marks)

---

**5.**
```python
for i in range(10, 0, -1):
    print(i)
```
✔ (3 marks)

---

**6.**
```python
student["grade"] = "B"
```
✔ (2 marks)

---

**7.**
```
0
1
2
Done
```
✔ (2 marks)

---

## Section C

**8.**
```python
total = 0
for i in range(1, 11):
    total += i
print(total)
```
✔ (4 marks)

---

**9.**
```python
items = {"bread": 20, "milk": 60, "eggs": 55}

for item, price in items.items():
    if price > 50:
        print(item)
```
✔ (5 marks)

---

**10.**
```python
text = "hello world"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)
```
✔ (5 marks)

---

# 🧾 Mark Allocation Summary

| Section | Marks |
|--------|------|
| A      | 6    |
| B      | 10   |
| C      | 14   |
| **Total** | **30** |
