# 🧩 What is `self` in Python (OOP)

# `self` is a reference to the current instance of the class.
# It represents the specific object that is being created or used.
# In simple terms, `self` means "this object" or "me" inside the class.

# When you define methods inside a class, `self` must always be the first parameter,
# because it allows access to the object's own attributes and methods.

# Example:
class Person:
    def __init__(self, name):
        self.name = name  # stores the name in this specific object

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Creating two different objects
p1 = Person("Johel")
p2 = Person("Randy")

# Each object has its own 'self' (own data)
p1.greet()   # Hello, my name is Johel
p2.greet()   # Hello, my name is Randy

# ✅ Key points:
# - `self` refers to the current instance (object) of the class.
# - It is passed automatically by Python (you don’t include it when calling the method).
# - It allows each object to keep and use its own data independently.
# - It’s not a reserved keyword, but it’s a strong convention to always name it `self`.

# Quiz Game (OOP Project)

A simple **Python quiz game** built using **Object-Oriented Programming (OOP)** principles.  
This lesson demonstrates how to use classes, objects, and modular programming to create an interactive console quiz.

---

## 📋 Description

The program presents a series of True/False questions to the user, checks the answers, and keeps track of the score.  
It’s a continuation of the OOP lessons, focusing on how to build a complete application by organizing logic across multiple files.

---

## 🧩 Project Structure

```
quiz-game-start/
│
├── main.py              # Main script – runs the quiz logic
├── question_model.py    # Question class – defines question attributes
├── quiz_brain.py        # QuizBrain class – handles question flow and scoring
└── data.py              # List of question/answer dictionaries
```

---

## ⚙️ How It Works

1. **Load Question Data:**  
   The program imports `question_data` from `data.py`.

2. **Create Question Objects:**  
   Each dictionary entry becomes a `Question` object stored in a list (`question_bank`).

3. **Start the Quiz:**  
   A `QuizBrain` object manages the flow of questions, verifying answers and updating the score.

4. **Display Results:**  
   Once all questions are answered, the game displays the final score.

---

## 💻 Example Output

```
Q1: The sky is blue. (True/False)? True
You got it right!
Your current score: 1/1

Q2: The capital of France is Berlin. (True/False)? False
You got it right!
Your current score: 2/2

You've completed the Quiz!
Your final score is: 2/2
```

---

## 🧠 What I Learned

- How to define and use classes and objects in Python.  
- The importance of the `self` parameter for instance-specific data.  
- Modular programming: splitting logic into multiple files.  
- Encapsulation and clean class design.  
- Applying OOP principles to build real-world programs.

---

## 🚀 Run the Program

To play the quiz:

```bash
python main.py
```

Make sure you’re inside the `quiz-game-start` directory.

---

## 🏁 Key Takeaways

- OOP helps organize logic cleanly and efficiently.  
- `self` refers to the current instance of the class.  
- Modular design improves readability and scalability.  

---


