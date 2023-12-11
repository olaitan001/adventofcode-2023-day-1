# Read input.text
puzzle_input = open('input.txt', 'r')

# Read line-by-line
read_lines = puzzle_input.readlines()


# Create an empty string for all numbers in each lines
num_line = ""

# Create an empty list to add all string from each line
num_list = []

# For loop to iterate through 'read_lines' 
for line in read_lines:
    # For loop to iterate through 'line'
    for nums in line:
        # If statement to detect numbers in 'nums'
        if nums.isdigit():
            # Combine the numbers that are detected in 'nums' to 'num_line'
            num_line = num_line + nums
    # Add the string 'num_line' to list 'num_list'
    num_list.append(num_line)
    # Empty 'num_line' to be used for the second line
    num_line = ""

    
# Create an empty string for the two digits
two_digit_num = ""

# Create an empty list to store all the two digits numbers
two_digit_list = []

# For loop to iterate through num_list
for digit in num_list:
    # Create a variable for the first digit in 'digit'
    first_digit = digit[0]
    # Create a variable for last digit in 'digit'
    last_digit = digit[-1]
    # Combine the two digits into a single string 'two_digit_num'
    two_digit_num = first_digit + last_digit
    # Convert the combined digits 'two_digit_num' in string to integer
    two_digit_num = int(two_digit_num)
    # Add the combined string to the list 'two_digit_list'
    two_digit_list.append(two_digit_num)
    # Empty 'two_digit_num' to work on the next digits in the list 'num_list'
    two_digit_num = ""

    
# Sum all the two digits in the list 'two_digit_list'
add_num = sum(two_digit_list)

print(add_num)

# Output: 52974
