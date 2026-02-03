# =============================
# PYTHON DICTIONARY EXERCISES
# =============================

# -----------------------------
# DICT EXERCISE 1
# -----------------------------
print("=========== DICT Exercise 1 ===========")
my_dict = {"name": "Alice", "age": 35, "city": "New York"}
print("Original dictionary:", my_dict)

# Add new key-value pair
my_dict["profession"] = "Doctor"
print("\nUpdated dictionary after adding 'profession':", my_dict)

# Modify value
my_dict["age"] = 40
print("\nUpdated dictionary after modification:", my_dict)

# Access key
print("\nCity:", my_dict["city"])


# -----------------------------
# DICT EXERCISE 2
# -----------------------------
print("\n=========== DICT Exercise 2 ===========")
my_dict = {"name": "Alice", "age": 35, "city": "New York", "profession": "Doctor"}
print("Original dictionary:", my_dict)

# Remove key-value pair
my_dict.pop("profession")
print("\nUpdated dictionary after removing 'profession':", my_dict)

# Print all key-value pairs
print("\nPrinting all key-value pairs:")
for key, value in my_dict.items():
    print(key + ":", value)

# Check if key exists
print("\nDoes 'age' exist?", "age" in my_dict)


# -----------------------------
# DICT EXERCISE 3
# -----------------------------
print("\n=========== DICT Exercise 3 ===========")
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

# zip pairs items together: ('Ten', 10), ('Twenty', 20)...
result_dict = dict(zip(keys, values))
print(result_dict)


# -----------------------------
# DICT EXERCISE 4
# -----------------------------
print("\n=========== DICT Exercise 4 ===========")
my_dict = {"name": "Alice", "age": 35, "city": "New York"}

# clear removes everything inside the dictionary
my_dict.clear()
print(my_dict)


# -----------------------------
# DICT EXERCISE 5
# -----------------------------
print("\n=========== DICT Exercise 5 ===========")
dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

# Create a new dict so we don't change dict1 directly
merged = dict1.copy()
merged.update(dict2)
print(merged)


# -----------------------------
# DICT EXERCISE 6
# -----------------------------
print("\n=========== DICT Exercise 6 ===========")
string1 = "Jessa"
freq = {}

# Count each character
for ch in string1:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print("Frequencies for 'Jessa':", freq)


# -----------------------------
# DICT EXERCISE 7
# -----------------------------
print("\n=========== DICT Exercise 7 ===========")
data = {"person": {"name": "Alice", "age": 30}}

# Access nested dictionary step by step
age = data["person"]["age"]
print("Alice's age is:", age)


# -----------------------------
# DICT EXERCISE 8
# -----------------------------
print("\n=========== DICT Exercise 8 ===========")
sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}

history_mark = sampleDict["class"]["student"]["marks"]["history"]
print(history_mark)


# -----------------------------
# DICT EXERCISE 9
# -----------------------------
print("\n=========== DICT Exercise 9 ===========")
nested_student_dict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}

nested_student_dict["class"]["student"]["name"] = "Jessa"
print(nested_student_dict)


# -----------------------------
# DICT EXERCISE 10
# -----------------------------
print("\n=========== DICT Exercise 10 ===========")
employees = ["Kelly", "Emma"]
defaults = {"designation": "Developer", "salary": 8000}

result = {}

# Each employee gets the same defaults dictionary content
for name in employees:
    result[name] = defaults.copy()

print(result)


# =============================
# PYTHON TUPLE EXERCISES
# =============================

# -----------------------------
# TUPLE EXERCISE 1
# -----------------------------
print("\n=========== TUPLE Exercise 1 ===========")
my_tuple = (1, 2, 3, 4, 5)
print("My tuple:", my_tuple)

# Third element is at index 2 because index starts from 0
print("The third element of my_tuple:", my_tuple[2])

print("The length of my_tuple:", len(my_tuple))


# -----------------------------
# TUPLE EXERCISE 2
# -----------------------------
print("\n=========== TUPLE Exercise 2 ===========")
original_tuple = ("a", "b")

# Repetition using *
repeated = original_tuple * 3
print(repeated)


# -----------------------------
# TUPLE EXERCISE 3
# -----------------------------
print("\n=========== TUPLE Exercise 3 ===========")
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slice from index 3 to index 7 (7 not included)
slice_tuple = numbers[3:7]
print(slice_tuple)


# -----------------------------
# TUPLE EXERCISE 4
# -----------------------------
print("\n=========== TUPLE Exercise 4 ===========")
tuple1 = (10, 20, 30, 40, 50)

# Reverse using slicing
reversed_tuple = tuple1[::-1]
print(reversed_tuple)


# -----------------------------
# TUPLE EXERCISE 5
# -----------------------------
print("\n=========== TUPLE Exercise 5 ===========")
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# 20 is inside the list at index 1, and 20 is at index 1 inside that list
print(tuple1[1][1])


# -----------------------------
# TUPLE EXERCISE 6
# -----------------------------
print("\n=========== TUPLE Exercise 6 ===========")
# Single item tuple MUST have a comma
single_item = (50,)
print(single_item)


# -----------------------------
# TUPLE EXERCISE 7
# -----------------------------
print("\n=========== TUPLE Exercise 7 ===========")
tuple1 = (10, 20, 30, 40)
print("tuple1 =", tuple1)

# Unpacking assigns each element to a variable
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)


# -----------------------------
# TUPLE EXERCISE 8
# -----------------------------
print("\n=========== TUPLE Exercise 8 ===========")
tuple1 = (11, 22)
tuple2 = (99, 88)

# Python can swap in one line
tuple1, tuple2 = tuple2, tuple1

print("tuple1:", tuple1)
print("tuple2:", tuple2)


# -----------------------------
# TUPLE EXERCISE 9
# -----------------------------
print("\n=========== TUPLE Exercise 9 ===========")
tuple1 = (11, 22, 33, 44, 55, 66)

# Copy 44 and 55 (index 3 and 4)
tuple2 = (tuple1[3], tuple1[4])
print("tuple2:", tuple2)


# -----------------------------
# TUPLE EXERCISE 10
# -----------------------------
print("\n=========== TUPLE Exercise 10 ===========")
my_list = [10, 20, 30]

# Convert list to tuple
converted = tuple(my_list)
print(converted)
