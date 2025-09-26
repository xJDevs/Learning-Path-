# ☕ Coffee Machine

A simple and interactive coffee vending machine program written in Python. This project simulates a real-world coffee machine that allows users to order espresso, latte, or cappuccino by inserting coins and tracks resources and profits.

---

## 🚀 Features
- Choose between **Espresso**, **Latte**, or **Cappuccino**.
- Insert coins (quarters, dimes, nickels, pennies) to pay for your drink.
- Tracks machine resources: water, milk, coffee, and profit.
- Special commands:
  - `report`: Displays current resource levels and total money earned.
  - `off`: Turns off the coffee machine program.

---

## 🛠️ Installation and Usage

1. Clone the repository:
```bash
git clone https://github.com/xJDevs/coffee-machine.git
cd coffee-machine
```

2. Run the coffee machine program:
```bash
python3 coffee_machine.py
```

## 💻 Usage / Demo

When you run the program, you'll be prompted to enter your choice of coffee or a command:

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is your latte ☕. Enjoy!
```

You can also type `report` to see the machine’s current resources or `off` to exit the program.

---

## 📂 Project Structure

```
coffee-machine/
├── coffee_machine.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- Command-line interface (CLI)

---

## 📚 What I Learned

- Organizing code using functions for clarity and reusability.
- Handling user input and validating it through loops and conditionals.
- Managing data with dictionaries for menu items and resources.
- Simulating a real-world machine with resource tracking and transaction handling.
- Building an interactive console application.

---

## 🌟 Future Improvements

- Add support for more drink options and customizable recipes.
- Implement a graphical user interface (GUI).
- Add persistent data storage to save resource states between sessions.
- Enhance input validation and error handling.
- Include unit tests for better code reliability.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Created by [Johel Gómez (xJDevs)](https://github.com/xJDevs)