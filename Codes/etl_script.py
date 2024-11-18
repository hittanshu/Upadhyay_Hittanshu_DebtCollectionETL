import pandas as pd
import re
import ast

# Read the CSV file
df = pd.read_csv("5k_borrowers_data.csv")

# Check for null values and basic info
print(df.info())

# Filter columns required for analysis
df_required = df[['Name', 'Credit Score', 'Loan Type', 'Loan Amount', 'Loan Term', 'Interest Rate', 'EMI', 'Repayment History', 'Days Left to Pay Current EMI', 'Delayed Payment']]

# Function to clean 'Repayment History' column, removing 'datetime.date' parsing issues
def clean_repayment_history(history_str):
    cleaned_str = re.sub(r"datetime\.date\((\d{4}),\s*(\d{1,2}),\s*(\d{1,2})\)", r"'\1-\2-\3'", history_str)
    return cleaned_str

# Apply cleaning function to the 'Repayment History' column
df_required['Repayment History'] = df_required['Repayment History'].apply(clean_repayment_history)

# Function to extract payment details (Payment Dates, Payment Modes) from 'Repayment History'
def extract_payment_details(history_str):
    try:
        history_list = ast.literal_eval(history_str)
        payment_dates = [entry['Payment Date'] for entry in history_list]
        payment_modes = [entry['Payment Mode'] for entry in history_list]
        return pd.Series([payment_dates, payment_modes])
    except (ValueError, SyntaxError) as e:
        # Handling parsing errors
        return pd.Series([[], []])

# Apply the function and create new columns for Payment Dates and Payment Modes
df_required[['Payment Dates', 'Payment Modes']] = df_required['Repayment History'].apply(extract_payment_details)

# Drop the original 'Repayment History' column
df_required.drop('Repayment History', inplace=True, axis=1)

# Function to calculate Outstanding Balance
def calculate_outstanding_balance(row):
    total_paid = len(row['Payment Dates']) * row['EMI']
    outstanding_balance = row['Loan Amount'] - total_paid
    return outstanding_balance

# Apply the function to calculate Outstanding Balance
df_required['Outstanding Balance'] = df_required.apply(calculate_outstanding_balance, axis=1)

# Save the final DataFrame to a new CSV file
df_required.to_csv("borrowed_data.csv")

print("Cleaned data has been saved to 'borrowed_data.csv'.")