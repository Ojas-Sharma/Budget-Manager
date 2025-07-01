import streamlit as st
from budget_manager import BudgetApp

def main():
    st.title("Budget Management Application")

    budget = st.number_input("Enter your total budget:", min_value=0.0, format="%.2f")
    app = BudgetApp(budget)

    if st.button("Set Budget"):
        st.session_state.budget_app = app
        st.success(f"Budget set to ${budget:.2f}")

    if 'budget_app' in st.session_state:
        app = st.session_state.budget_app

        # Add Expense Section
        st.subheader("Add Expense")
        description = st.text_input("Expense Description")
        amount = st.number_input("Expense Amount", min_value=0.0, format="%.2f")
        category = st.selectbox("Expense Category", ["Shopping", "Food", "Groceries", "ET", "Miscellaneous"])

        if st.button("Add Expense"):
            app.add_expense(description, amount, category)
            st.success(f"Expense Added: {description} - ${amount:.2f} ({category})")

        # Budget Summary Section
        st.subheader("Budget Summary")
        if st.button("Show Summary"):
            summary = app.show_summary()
            print(summary)
            st.subheader("Budget Summary")
            st.write(f"**Total Budget:** {summary['total_budget']:.2f}")
            st.write(f"**Total Spent:** {summary['total_spent']:.2f}")
            st.write(f"**Remaining Budget:** {summary['remaining_budget']:.2f}")

            st.subheader("Expenses by Category")
            for category, amount in summary["category_breakdown"]:
                st.write(f"- {category}: ${amount:.2f}")

            st.subheader("All Expenses")
            for expense in summary["expenses"]:
                st.write(f"- {expense[1]}: ${expense[2]:.2f} ({expense[3]})")

        # Delete Expense Section
        st.subheader("Delete Expense")
        expenses = app.fetch_expenses()
        expense_options = {f"{expense[1]}: ${expense[2]:.2f} ({expense[3]})": expense[0] for expense in expenses}
        selected_expense = st.selectbox("Select an expense to delete", list(expense_options.keys()))

        if st.button("Delete Expense"):
            expense_id = expense_options[selected_expense]
            app.delete_expense(expense_id)
            st.success(f"Deleted expense: {selected_expense}")

if __name__ == "__main__":
    main()