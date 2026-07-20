# Maximum Days in a Month Checker in Python

## 📌 Overview

This project is a simple Python program that determines the **maximum number of days in a month** based on a user-entered month number.

The program uses Python's **`match-case`** statement to classify months into those with **31 days**, **30 days**, or **February (28 or 29 days)**. It also validates the input and displays an error message for invalid month numbers.

This project is ideal for beginners learning conditional statements, pattern matching, and user input handling in Python.

---

## 🚀 Features

* Accepts a month number (1–12) from the user
* Displays the maximum number of days in the selected month
* Handles February separately (28 or 29 days)
* Uses Python's `match-case` statement
* Validates invalid month numbers
* Beginner-friendly implementation

---

## 🛠️ Technologies Used

* Python 3.10+

---

## 📂 Project Structure

```text
├── max_days_in_month.py
└── README.md
```

---

## 💻 Source Code

```python
month = int(input("Enter a month number : "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Max. days are 31")

    case 4 | 6 | 9 | 11:
        print("Max. days are 30")

    case 2:
        print("Max. days are 28 or 29")

    case _:
        print("Invalid month number")
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-max-days-in-month.git
cd python-max-days-in-month
```

### Run the Program

```bash
python max_days_in_month.py
```

---

## 📋 Sample Output

### Example 1

```text
Enter a month number : 1
Max. days are 31
```

### Example 2

```text
Enter a month number : 4
Max. days are 30
```

### Example 3

```text
Enter a month number : 2
Max. days are 28 or 29
```

### Example 4

```text
Enter a month number : 15
Invalid month number
```

---

## 🧠 Concepts Covered

* User Input
* Pattern Matching (`match-case`)
* Conditional Logic
* Input Validation
* Console Output

---

## 🔍 How It Works

1. Read the month number from the user.
2. Use the `match-case` statement to compare the input.
3. If the month is:

   * **1, 3, 5, 7, 8, 10, or 12** → Display **31 days**
   * **4, 6, 9, or 11** → Display **30 days**
   * **2** → Display **28 or 29 days**
4. If the input is outside the range **1–12**, display **"Invalid month number"**.

---

## 📅 Month Classification

| Month Number          | Maximum Days |
| --------------------- | -----------: |
| 1, 3, 5, 7, 8, 10, 12 |           31 |
| 4, 6, 9, 11           |           30 |
| 2                     |     28 or 29 |
| Others                |      Invalid |

---

## ⏱️ Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(1)**   |
| Space Complexity | **O(1)**   |

The program performs a constant number of comparisons regardless of the input.

---

## 🔮 Future Improvements

* Determine February's days based on a user-entered year
* Display the month name along with the number of days
* Create a calendar viewer
* Build a graphical version using Tkinter
* Develop a web version using Flask

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* How to use Python's `match-case` statement
* How to group multiple conditions efficiently
* Basic calendar-related programming logic
* User input validation and decision-making in Python

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software Engineer | Python | Java | SQL | Data Analytics

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="664" height="730" alt="image" src="https://github.com/user-attachments/assets/51580c4c-2248-40a4-8d5d-ae1276916897" />
