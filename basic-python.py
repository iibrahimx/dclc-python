# -----------------------------
# EXERCISE 1
# -----------------------------
def multiplication_or_sum(num1, num2):
    # Calculate product once so we can reuse it
    product = num1 * num2

    # If product is 1000 or less, return the product
    if product <= 1000:
        return product
    # Otherwise return the sum
    else:
        return num1 + num2


print("=========== Exercise 1 ===========")
print("The result is", multiplication_or_sum(20, 30))
print("The result is", multiplication_or_sum(40, 30))


# -----------------------------
# EXERCISE 2
# -----------------------------
def current_and_previous_sums():
    previous_num = 0

    print("Printing current and previous number sum in a range(10)")
    # range(10) gives 0 to 9 (matches expected output)
    for current_num in range(10):
        # Sum is current + previous
        current_sum = current_num + previous_num

        print(
            "Current Number",
            current_num,
            "Previous Number ",
            previous_num,
            " Sum: ",
            current_sum,
        )

        # Update previous AFTER printing (so next loop uses current as previous)
        previous_num = current_num


print("\n=========== Exercise 2 ===========")
current_and_previous_sums()


# -----------------------------
# EXERCISE 3
# -----------------------------
def get_even_index(text):
    result_chars = []

    # enumerate gives us (index, character) as we loop through the string
    for index, char in enumerate(text):
        # even index means index % 2 == 0 (0, 2, 4, 6...)
        if index % 2 == 0:
            result_chars.append(char)

    # join the list of characters into a single string
    return "".join(result_chars)


print("\n=========== Exercise 3 ===========")
my_string = "PYnative"
even_chars = get_even_index(my_string)
print("Orginal String is ", my_string)
print("Printing only even index chars")
# print each character on a new line like the expected output
for c in even_chars:
    print(c)


# -----------------------------
# EXERCISE 4
# -----------------------------
def remove_chars(word, n):
    # Slicing: word[n:] means "start from index n to the end"
    return word[n:]


print("\n=========== Exercise 4 ===========")
print("Removing characters from a string")
print(remove_chars("pynative", 4))  # tive
print(remove_chars("pynative", 2))  # native


# -----------------------------
# EXERCISE 5
# -----------------------------
def first_and_last(item):
    # Compare first element (index 0) and last element (index -1)
    if item[0] == item[-1]:
        return True
    else:
        return False


print("\n=========== Exercise 5 ===========")
numbers_x = [10, 20, 30, 40, 10]
print("Result is", first_and_last(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print("Result is", first_and_last(numbers_y))


# -----------------------------
# EXERCISE 6
# -----------------------------
def divisible_by_five(item):
    print("Given list is", item)
    print("Divisible by 5")

    for i in item:
        # divisible by 5 means remainder is 0
        if i % 5 == 0:
            print(i)


print("\n=========== Exercise 6 ===========")
numbers_x = [10, 20, 33, 46, 55]
divisible_by_five(numbers_x)


# -----------------------------
# EXERCISE 7
# -----------------------------
def num_of_occurences(text):
    # count() counts how many times a substring appears
    return text.count("Emma")


print("\n=========== Exercise 7 ===========")
str_x = "Emma is good developer. Emma is a writer"
print(f"Emma appeared {num_of_occurences(str_x)} times")


# -----------------------------
# EXERCISE 8
# -----------------------------
def print_number_triangle(rows):
    # row goes from 1 to rows
    for row in range(1, rows + 1):
        # repeat the number "row" times, then join with spaces
        line = " ".join([str(row)] * row)
        print(line)


print("\n=========== Exercise 8 ===========")
print_number_triangle(5)


# -----------------------------
# EXERCISE 9
# -----------------------------
def is_palindrome(number):
    # Negative numbers are not palindromes in this simple version
    if number < 0:
        return False

    # Convert number to string so we can reverse it easily
    original_string = str(number)
    reversed_string = original_string[::-1]  # reverse using slicing

    # Palindrome if original equals reversed
    if original_string == reversed_string:
        return True
    else:
        return False


print("\n=========== Exercise 9 ===========")
for n in [121, 125]:
    print("original number", n)
    if is_palindrome(n):
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")


# -----------------------------
# EXERCISE 10
# -----------------------------
def merge_odd_even(list1, list2):
    # odd numbers have remainder 1 when divided by 2
    odds_from_list1 = [n for n in list1 if n % 2 != 0]
    # even numbers have remainder 0 when divided by 2
    evens_from_list2 = [n for n in list2 if n % 2 == 0]
    return odds_from_list1 + evens_from_list2


print("\n=========== Exercise 10 ===========")
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_odd_even(list1, list2))


# -----------------------------
# EXERCISE 11
# -----------------------------
def digits_in_reverse(number):
    # Convert to string, reverse it, then convert each character back to int
    return [int(ch) for ch in str(number)[::-1]]


print("\n=========== Exercise 11 ===========")
number = 7536
reversed_digits = digits_in_reverse(number)
print(" ".join(str(d) for d in reversed_digits))


# -----------------------------
# EXERCISE 12
# -----------------------------
def calculate_income_tax(income):
    tax = 0

    # First 10,000 at 0%
    if income <= 10000:
        return 0

    # Next 10,000 at 10% (income between 10,001 and 20,000)
    if income <= 20000:
        taxable_at_10 = income - 10000
        tax += taxable_at_10 * 0.10
        return int(tax)

    # Income above 20,000:
    # full second bracket is always taxed 10%
    tax += 10000 * 0.10

    # remaining amount is taxed 20%
    remaining = income - 20000
    tax += remaining * 0.20

    return int(tax)


print("\n=========== Exercise 12 ===========")
income = 45000
print("Income:", income)
print("Tax payable:", calculate_income_tax(income))


# -----------------------------
# EXERCISE 13
# -----------------------------
def print_multiplication_table(size=10):
    # Outer loop controls the row number
    for row in range(1, size + 1):
        line_parts = []

        # Inner loop controls the column number
        for col in range(1, size + 1):
            # Multiply row by column and add to the row list
            line_parts.append(str(row * col))

        # Print one full row
        print("  ".join(line_parts))


print("\n=========== Exercise 13 ===========")
print_multiplication_table(10)


# -----------------------------
# EXERCISE 14
# -----------------------------
def print_downward_star_pyramid(rows=5):
    # Start from rows down to 1
    for i in range(rows, 0, -1):
        # Print i stars on the same line separated by spaces
        print(" ".join(["*"] * i))


print("\n=========== Exercise 14 ===========")
print_downward_star_pyramid(5)


# -----------------------------
# EXERCISE 15
# -----------------------------
def exponent(base, exp):
    # Start from 1 because multiplying by 1 doesn't change anything
    result = 1

    # Multiply base by itself exp times
    for _ in range(exp):
        result *= base

    return result


print("\n=========== Exercise 15 ===========")
print("2 raises to the power of 5:", exponent(2, 5))
print("5 raises to the power of 4:", exponent(5, 4))
