# Function to handle input validation
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be positive. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Goal cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

# Main Program
def main():
    print("Welcome to the Compound Interest Calculator!")

    # Step 1: Get user input with validation
    fDeposit = get_positive_float("Enter the initial deposit amount: $")
    fInterestRate = get_positive_float("Enter the annual interest rate (percentage): ")
    iMonths = int(get_positive_float("Enter the number of months: "))
    fGoal = get_non_negative_float("Enter your saving goal amount: $")

    # Step 2: Convert the annual interest rate to a monthly interest rate
    fMonthlyInterestRate = (fInterestRate / 100) / 12

    # Step 3: Calculate and display monthly compounded balances
    print("\nMonthly Compound Interest Calculation:")
    fBalance = fDeposit
    for iMonth in range(1, iMonths + 1):
        fInterest = fBalance * fMonthlyInterestRate
        fBalance += fInterest
        print(f"Month {iMonth}: ${fBalance:,.2f}")

    # Step 4: Calculate how many months it will take to reach the goal
    print("\nCalculating how many months to reach the goal...")
    fBalance = fDeposit
    iMonthsToGoal = 0
    while fBalance < fGoal:
        fInterest = fBalance * fMonthlyInterestRate
        fBalance += fInterest
        iMonthsToGoal += 1

    # Step 5: Output the result with thousands separator
    print(f"\nIt will take {iMonthsToGoal:,} months to reach your goal of ${fGoal:,.2f}.")

if __name__ == "__main__":
    main()
