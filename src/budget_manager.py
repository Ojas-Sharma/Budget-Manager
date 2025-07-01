import sqlite3
class BudgetApp:
    def __init__(self, budget):
        self.budget = budget
        self.conn = sqlite3.connect('budget.db')
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_expense(self, description, amount, category):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if category not in ["Shopping", "Food", "Groceries", "ET", "Miscellaneous"]:
            raise ValueError("Invalid category. Please choose from Shopping, Food, Groceries, ET, Miscellaneous.")
        self.cursor.execute(
            'INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)',
            (description, amount, category)
        )
        self.conn.commit()

    def fetch_expenses(self):
        self.cursor.execute('SELECT * FROM expenses')
        return self.cursor.fetchall()

    def calculate_total_spent(self):
        self.cursor.execute('SELECT SUM(amount) FROM expenses')
        total = self.cursor.fetchone()[0]
        return total if total else 0

    def calculate_category_breakdown(self):
        self.cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
        return self.cursor.fetchall()

    def show_summary(self):
        total_spent = self.calculate_total_spent()
        remaining_budget = self.budget - total_spent
        summary = {
            "total_budget": self.budget,
            "total_spent": total_spent,
            "remaining_budget": remaining_budget,
            "category_breakdown": self.calculate_category_breakdown(),
            "expenses": self.fetch_expenses()
        }
        return summary
    
    def delete_expense(self, expense_id):
        self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        self.conn.commit()
        print(f"Deleted expense with ID: {expense_id}")

    def close(self):
        self.conn.close()