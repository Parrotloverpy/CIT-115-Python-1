import math

# Function to get a valid float input with data validation
def getFloatInput(prompt):
    while True:
        try:
            # Prompt user for input
            user_input = input(prompt)
            # Convert to float
            user_value = float(user_input)
            # Check if the value is positive and non-zero
            if user_value <= 0:
                print("Error: Value must be greater than zero. Please try again.")
            else:
                return user_value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

# Function to calculate the number of gallons of paint needed
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    # Calculate gallons and round up to the nearest whole number
    return math.ceil(fSquareFeet / fFeetPerGallon)

# Function to calculate labor hours
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    # Calculate total labor hours based on gallons of paint
    return fLaborHoursPerGallon * iTotalGallons

# Function to calculate labor cost
def getLaborCost(fLaborHoursPerGallon, fLaborChargePerHour, iTotalGallons):
    # Calculate total labor cost based on labor hours and hourly rate
    total_hours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    return total_hours * fLaborChargePerHour

# Function to calculate the paint cost
def getPaintCost(fPaintPrice, iTotalGallons):
    # Calculate total paint cost
    return fPaintPrice * iTotalGallons

# Function to get the sales tax rate based on the state
def getSalesTax(state):
    state = state.upper()  # Ensure state input is in uppercase
    tax_rates = {
        'CT': 0.06,
        'MA': 0.0625,
        'ME': 0.085,
        'NH': 0.0,
        'RI': 0.07,
        'VT': 0.06
    }
    # Return tax rate or 0 if state is not in the dictionary
    return tax_rates.get(state, 0.0)

# Function to display the cost estimate and output to a file
def showCostEstimate(fPaintCost, fLaborCost, fSalesTax, fTotalCost, fTotalCostWithTax, file_name):
    # Display the result to the screen
    print("\nPaint Job Estimate")
    print("--------------------")
    print(f"Paint Cost: ${fPaintCost:,.2f}")
    print(f"Labor Cost: ${fLaborCost:,.2f}")
    print(f"Sales Tax: ${fSalesTax:,.2f}")
    print(f"Total Cost (without tax): ${fTotalCost:,.2f}")
    print(f"Total Cost (with tax): ${fTotalCostWithTax:,.2f}")

    # Write the result to a file
    with open(file_name, 'w') as file:
        file.write("Paint Job Estimate\n")
        file.write("--------------------\n")
        file.write(f"Paint Cost: ${fPaintCost:,.2f}\n")
        file.write(f"Labor Cost: ${fLaborCost:,.2f}\n")
        file.write(f"Sales Tax: ${fSalesTax:,.2f}\n")
        file.write(f"Total Cost (without tax): ${fTotalCost:,.2f}\n")
        file.write(f"Total Cost (with tax): ${fTotalCostWithTax:,.2f}\n")

    print(f"\nThe output has been written to {file_name}")

# Main program function
def main():
    # Prompt for and get user inputs
    fSquareFeet = getFloatInput("Enter Square Feet of the Wall: ")
    fPaintPrice = getFloatInput("Enter Paint Price (per gallon): ")
    fFeetPerGallon = getFloatInput("Enter Feet per Gallon of Paint: ")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
    fLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour: ")

    # Get state and customer last name
    state = input("Enter the state of the job (e.g., CT, MA, ME, NH, RI, VT): ")
    last_name = input("Enter the customer's last name: ")

    # Calculate the number of gallons of paint required
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)

    # Calculate labor cost and paint cost
    fLaborCost = getLaborCost(fLaborHoursPerGallon, fLaborChargePerHour, iTotalGallons)
    fPaintCost = getPaintCost(fPaintPrice, iTotalGallons)

    # Get the sales tax based on the state
    fSalesTaxRate = getSalesTax(state)
    fSalesTax = fSalesTaxRate * (fLaborCost + fPaintCost)

    # Calculate total cost (without and with tax)
    fTotalCost = fLaborCost + fPaintCost
    fTotalCostWithTax = fTotalCost + fSalesTax

    # Prepare the output file name
    file_name = f"{last_name}_PaintJobOutput.txt"

    # Show the cost estimate and output to a file
    showCostEstimate(fPaintCost, fLaborCost, fSalesTax, fTotalCost, fTotalCostWithTax, file_name)

# Run the program
if __name__ == "__main__":
    main()
