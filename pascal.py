# Function to find the maximum among three numbers
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

# Function to multiply all elements in a list
def mult_list(elements_list):
    product_result = 1
    for element in elements_list:
        product_result *= element
    return product_result

# Function to reverse a given string
def rev_string(input_string):
    return input_string[::-1]

# Function to check if a number falls within a specified range
def num_within(target_num, range_start, range_end):
    return range_start <= target_num <= range_end

# Function to print Pascal's triangle up to 'rows' rows
def pascal(rows):
    triangle_matrix = []
    for row_index in range(rows):
        current_row = []
        for col_index in range(row_index + 1):
            if col_index == 0 or col_index == row_index:
                current_row.append(1)
            else:
                current_row.append(triangle_matrix[row_index - 1][col_index - 1] + triangle_matrix[row_index - 1][col_index])
        triangle_matrix.append(current_row)
        print(" ".join(str(value) for value in current_row))

# Calling each function to test
print(max_num(5, 7, 2))
print(mult_list([1, 2, 3, 4]))
print(rev_string("Hello"))
print(num_within(3, 2, 4))
print(num_within(10, 2, 5))

pascal(1)
pascal(5)
