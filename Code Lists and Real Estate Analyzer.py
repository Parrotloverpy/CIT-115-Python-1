def getFloatInput(prompt):
    """
    This function prompts the user for input and ensures the input is a valid non-zero positive float.
    """
    while True:
        try:
            # Prompt user for input
            user_input = input(prompt)

            # Try to convert input to a float
            value = float(user_input)

            # Check if the value is positive and non-zero
            if value <= 0:
                print("Please enter a positive, non-zero number.")
                continue

            return value  # Return the valid float

        except ValueError:
            # If the input is not a valid float, print an error message and prompt again
            print("Invalid input. Please enter a valid numeric value.")

def getMedian(sales_list):
    """
    This function calculates and returns the median of the sales list.
    """
    sales_list.sort()  # Sort the list from smallest to largest

    length = len(sales_list)

    # If the number of elements is odd, return the middle element
    if length % 2 == 1:
        median = sales_list[length // 2]
    else:
        # If the number of elements is even, average the two middle elements
        mid1 = sales_list[length // 2 - 1]
        mid2 = sales_list[length // 2]
        median = (mid1 + mid2) / 2

    return median

def main():
    sales_data = []  # List to store all the sales prices

    while True:
        # Get a valid sales price from the user
        sale_price = getFloatInput("Enter property sales value: ")
        sales_data.append(sale_price)

        # Ask if the user wants to enter another value
        while True:
            another = input("Enter another value Y or N: ").strip().lower()
            if another == 'y':
                break
            elif another == 'n':
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

        if another == 'n':
            break  # Exit the loop if the user enters 'n'

    # Sort the sales data list
    sales_data.sort()

    # Print each entry in the sorted list
    print("\nSorted Sales Data:")
    for sale in sales_data:
        print(f"${sale:,.2f}")

    # Calculate and print the statistics
    total_sales = sum(sales_data)
    min_value = sales_data[0]
    max_value = sales_data[-1]
    average = total_sales / len(sales_data)
    median = getMedian(sales_data)
    commission = total_sales * 0.03

    print("\nSales Summary:")
    print(f"Minimum Value:    ${min_value:,.2f}")
    print(f"Maximum Value:    ${max_value:,.2f}")
    print(f"Total Sales:      ${total_sales:,.2f}")
    print(f"Average Sales:    ${average:,.2f}")
    print(f"Median Sales:     ${median:,.2f}")
    print(f"Commission (3%):  ${commission:,.2f}")

# Run the main function
if __name__ == "__main__":
    main()
