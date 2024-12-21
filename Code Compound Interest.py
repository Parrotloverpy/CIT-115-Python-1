sPrincipal = input("Enter the starting principal amount (e.g., 1000.00): ")
sInterestRate = input("Enter the annual interest rate (e.g., 2.5): ")
sCompounding = input("Enter the number of times interest is compounded per year (e.g., 12): ")
sYears = input("Enter the number of years (e.g., 2): ")

# Convert inputs to appropriate data types
nPrincipal = float(sPrincipal)
nInterestRate = float(sInterestRate)
nCompounding = int(sCompounding)
nYears = float(sYears)

# Calculate future value using the compound interest formula
decimal_rate = nInterestRate / 100
future_value = nPrincipal * (1 + decimal_rate / nCompounding) ** (nCompounding * nYears)

# Output the result with the correct formatting
print(f"At the end of {nYears} years, you will have ${future_value:,.2f}")