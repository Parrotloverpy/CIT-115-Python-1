# Prompt for the person's name
str_person_name = input("Enter the person's name: ")

# Initialize variables for test scores
int_test1 = int(input("Enter Test Score 1: "))
int_test2 = int(input("Enter Test Score 2: "))
int_test3 = int(input("Enter Test Score 3: "))
int_test4 = int(input("Enter Test Score 4: "))

# Validate that all test scores are greater than zero
if int_test1 < 0 or int_test2 < 0 or int_test3 < 0 or int_test4 < 0:
    print("Test scores must be greater than 0.")
    exit()

# Prompt user to drop the lowest grade
str_drop_lowest = input("Do you want to drop the lowest grade? (Y/N): ").upper()

# Validate the drop lowest input
if str_drop_lowest not in ['Y', 'N']:
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# Calculate average based on whether to drop the lowest score
if str_drop_lowest == 'Y':
    # Determine the lowest score without using min() or lists
    if int_test1 <= int_test2 and int_test1 <= int_test3 and int_test1 <= int_test4:
        float_average = (int_test2 + int_test3 + int_test4) / 3.0
    elif int_test2 <= int_test1 and int_test2 <= int_test3 and int_test2 <= int_test4:
        float_average = (int_test1 + int_test3 + int_test4) / 3.0
    elif int_test3 <= int_test1 and int_test3 <= int_test2 and int_test3 <= int_test4:
        float_average = (int_test1 + int_test2 + int_test4) / 3.0
    else:
        float_average = (int_test1 + int_test2 + int_test3) / 3.0
else:
    # Average all 4 test scores
    float_average = (int_test1 + int_test2 + int_test3 + int_test4) / 4.0

# Determine letter grade based on the average
if float_average >= 97.0:
    str_letter_grade = "A+"
elif float_average >= 94.0:
    str_letter_grade = "A"
elif float_average >= 90.0:
    str_letter_grade = "A-"
elif float_average >= 87.0:
    str_letter_grade = "B+"
elif float_average >= 84.0:
    str_letter_grade = "B"
elif float_average >= 80.0:
    str_letter_grade = "B-"
elif float_average >= 77.0:
    str_letter_grade = "C+"
elif float_average >= 74.0:
    str_letter_grade = "C"
elif float_average >= 70.0:
    str_letter_grade = "C-"
elif float_average >= 67.0:
    str_letter_grade = "D+"
elif float_average >= 64.0:
    str_letter_grade = "D"
elif float_average >= 60.0:
    str_letter_grade = "D-"
else:
    str_letter_grade = "F"

# Output the results
print(f"\n{str_person_name}'s Average: {float_average:.1f}")
print(f"Letter Grade: {str_letter_grade}")
