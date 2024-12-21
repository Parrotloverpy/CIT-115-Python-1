# Temperature Converter Program
print("Prof. C's Temp Converter:")

# Prompt the user for a temperature
fTemperature = input("Enter a temperature: ")

# Validate if the input is a number
try:
    fTemperature = float(fTemperature)
except ValueError:
    print("You must enter a valid number.")
    exit()

# Prompt for the temperature scale
cScale = input("Is the temp F for Fahrenheit or C for Celsius? ").strip().upper()

# Check for valid scale input
if cScale not in ['F', 'C']:
    print("You must enter a F or C")
    exit()

# Fahrenheit to Celsius conversion
if cScale == 'F':
    if fTemperature > 212:
        print("Temp can not be > 212")
    else:
        cCelsius = (5.0 / 9) * (fTemperature - 32)
        print(f"The Celsius equivalent is: {cCelsius:.1f}")

# Celsius to Fahrenheit conversion
elif cScale == 'C':
    if fTemperature > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheit = ((9.0 / 5.0) * fTemperature) + 32
        print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}")