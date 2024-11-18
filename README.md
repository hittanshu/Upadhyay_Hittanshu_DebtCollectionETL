Debt Collection ETL and Basic Analysis
======================================

Objective
---------

This project performs a basic ETL (Extract, Transform, Load) process on borrower data, cleans and transforms the data using Python, and saves it as a CSV. The transformed data can then be loaded manually into a SQLite database for further SQL-based analysis.

Table of Contents
-----------------

1.  Project Structure
    
2.  How to Run
    
3.  Assumptions
    
4.  SQL Queries and Analysis
    
5.  Notes
    
6.  Deliverables
    

Project Structure
-----------------

The project contains the following files:

*   etl\_script.py: Python script for performing ETL (Extract, Transform, Load) on the borrower data.
    
*   analysis\_queries.sql: SQL script containing the queries for analysis.
    
*   borrowed\_data.csv: Transformed CSV file generated after the ETL process.
    
*   borrowers.db: SQLite database file (to be manually created from borrowed\_data.csv).
    
*   analysis\_results.txt: Contains the output of SQL queries.
    
*   README.md: This document.
    

How to Run
----------

### Step 1: Data ETL

1.  Place the provided 5k\_borrowers\_data.csv file in the same directory as the etl\_script.py file.
    
2.  Copy
    ``` bash
     etl_script.py
    ```
    
5.  The script will:
    
    *   Clean the data.
        
    *   Transform it to include derived columns (Outstanding Balance, Payments Made).
        
    *   Save the transformed data as borrowed\_data.csv.
        

### Step 2: Load Data to SQLite

1.  Open **SQLite Studio** or your preferred SQLite client.
    
2.  Create a new SQLite database named borrowers.db.
    
3.  Import the transformed CSV file (borrowed\_data.csv) into a new table named borrowers:
    
    *   Use the **SQLite Studio** import functionality to upload borrowed\_data.csv.
        
    *   Ensure proper column types are defined during the import.
        
4.  PRAGMA table\_info(borrowers);
    

### Step 3: SQL Analysis

1.  Open the analysis\_queries.sql file in VS Code or any SQL editor.
    
2.  Connect to the borrowers.db SQLite database in **SQLite Studio**.
    
3.  Run the SQL queries provided in analysis\_queries.sql to generate insights.
    

Assumptions
-----------

### ETL Process Assumptions

1.  **Data Format**:
    
    *   The input CSV file (5k\_borrowers\_data.csv) contains consistent column names and formats.
        
    *   Repayment History is stored as JSON-like strings that require parsing.
        
2.  **Derived Columns**:
    
    *   Outstanding Balance = Loan Amount - (Payments Made × EMI)
        
    *   Payments Made is the count of payment dates extracted from Repayment History.
        
3.  **Data Cleaning**:
    
    *   Entries like datetime.date(Y, M, D) in Repayment History are replaced with ISO date strings (YYYY-MM-DD).
        
    *   Missing or invalid numerical values (e.g., Loan Amount, Interest Rate) are ignored or set to NaN.
        
4.  **Dropped Columns**:
    
    *   Irrelevant columns like Geographical Location, IP Address, and Mailing Address were removed.
        

### SQL Assumptions

1.  **Good Repayment History**:
    
    *   Borrowers with Delayed Payment = 'No' are considered to have a "good repayment history."
        
    *   Borrowers with Delayed Payment = 'Yes' are excluded, even if they made significant payments.
        
2.  **Top Borrowers**:
    
    *   Determined by the Outstanding Balance column, sorted in descending order.
        
3.  **Loan Type Analysis**:
    
    *   Analysis is grouped by Loan Type and includes borrower count, total loan amount, and average outstanding balance.
        

SQL Queries and Analysis
------------------------

The SQL file includes queries for the following tasks:

1.  **Average Loan Amount**:
    
    *   Calculates the average loan amount for borrowers more than 5 days past due.
        
2.  **Top 10 Borrowers with Highest Outstanding Balance**:
    
    *   Lists the top 10 borrowers with the highest unpaid balance.
        
3.  **Borrowers with Good Repayment History**:
    
    *   Lists borrowers with no delayed payments, sorted by the number of payments made.
        
4.  **Loan Type Analysis**:
    
    *   Provides an overview of borrower counts, total loan amounts, and average outstanding balances grouped by loan type.
        

Notes
-----

*   **SQLite Studio** was used to load and manage the SQLite database.
    
*   The ETL script only prepares the data; database creation and loading must be done manually.
    
*   Ensure column types are properly defined during the CSV import process.
    

Deliverables
------------

The following files are part of this project:

1.  etl\_script.py: Python script for ETL.
    
2.  analysis\_queries.sql: SQL script for analysis queries.
    
3.  borrowed\_data.csv: Transformed borrower data after ETL.
    
4.  borrowers.db: SQLite database with processed borrower data (manually created).
    
5.  analysis\_results.txt: Output of the SQL queries.
    
6.  README.md: Instructions and project documentation.
