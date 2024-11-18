-- Average Loan Amount
SELECT ROUND(AVG([Loan Amount]), 2) AS AverageLoanAmount
FROM borrowers
WHERE [Days Left to Pay Current EMI] > 5;

-- Top 10 Outstanding Balance
SELECT Name, [Outstanding Balance]
FROM borrowers
ORDER BY [Outstanding Balance] DESC
LIMIT 10;

-- Assuming good repayment history means person has no delayed payment, we display the person with maximum payments made
SELECT 
    Name, 
    [Credit Score], 
    [Loan Type], 
    [Loan Amount], 
    LENGTH([Payment Dates]) - LENGTH(REPLACE([Payment Dates], ',', '')) + 1 AS PaymentsMade
FROM borrowers
WHERE [Delayed Payment] = 'No'
ORDER BY PaymentsMade DESC;

-- Grouping by different loan types to get an overview
SELECT [Loan Type], 
       COUNT(*) AS BorrowerCount, 
       SUM([Loan Amount]) AS TotalLoanAmount,
       ROUND(AVG([Outstanding Balance]), 2) AS AverageOutstandingBalance
FROM borrowers
GROUP BY [Loan Type]
ORDER BY TotalLoanAmount DESC;