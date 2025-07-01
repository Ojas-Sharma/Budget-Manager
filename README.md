# Budget Management Streamlit Application

This is a simple budget management application built using Streamlit for personal use. It allows users to manage their expenses, view summaries, and track their personal spending effectively.

## Project Structure

```
Budget-Manager
├── src
│   ├── app.py               # Main entry point for the Streamlit application
│   ├── budget_manager.py     # Contains budget management logic
│   └── utils
│       └── __init__.py      # Utility functions and classes
├── requirements.txt          # Project dependencies
├── .streamlit
│   └── config.toml          # Streamlit configuration settings
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd Budget-Manager
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit application:**
   ```
   streamlit run src/app.py
   ```

2. **Interact with the application:**
   - Add expenses by providing a description, amount, and category.
   - View the budget summary, including total spent and remaining budget.
   - Delete expenses

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.