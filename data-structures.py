# =============================
# Python Data Structure Exercises 1 - 10
# =============================


# -----------------------------
# EXERCISE 1
# -----------------------------
print("=========== Exercise 1 ===========")
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# Odd-index elements means index 1, 3, 5... (not "odd numbers")
odd_index_l1 = l1[1::2]  # start at index 1, step by 2
even_index_l2 = l2[0::2]  # start at index 0, step by 2

print("Element at odd-index positions from list one")
print(odd_index_l1)

print("Element at even-index positions from list two")
print(even_index_l2)

l3 = odd_index_l1 + even_index_l2
print("\nPrinting Final third list")
print(l3)


# -----------------------------
# EXERCISE 2
# -----------------------------
print("\n=========== Exercise 2 ===========")
list1 = [54, 44, 27, 79, 91, 41]

# Remove item at index 4 (5th element)
removed_item = list1.pop(4)  # pop removes and returns the item

print("List After removing element at index 4 ", list1)

# Add removed item at 2nd position (index 2, same as your instructions style)
list1.insert(2, removed_item)
print("List after Adding element at index 2 ", list1)

# Add removed item at the end
list1.append(removed_item)
print("List after Adding element at last ", list1)


# -----------------------------
# EXERCISE 3
# -----------------------------
print("\n=========== Exercise 3 ===========")
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = 3

# We move in steps of 3: 0, 3, 6
chunk_number = 1
for i in range(0, len(sample_list), chunk_size):
    chunk = sample_list[i : i + chunk_size]  # take 3 items
    print("Chunk ", chunk_number, chunk)
    print("After reversing it ", chunk[::-1])  # reverse using slicing
    chunk_number += 1


# -----------------------------
# EXERCISE 4
# -----------------------------
print("\n=========== Exercise 4 ===========")
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dict = {}

# Count each element
for item in sample_list:
    if item in count_dict:
        count_dict[item] = count_dict[item] + 1
    else:
        count_dict[item] = 1

print("Printing count of each item ", count_dict)


# -----------------------------
# EXERCISE 5
# -----------------------------
print("\n=========== Exercise 5 ===========")
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# zip pairs elements: (2,4), (3,9) ...
pair_set = set(zip(first_list, second_list))

print("Result is ", pair_set)


# -----------------------------
# EXERCISE 6
# -----------------------------
print("\n=========== Exercise 6 ===========")
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Intersection gives common elements
common = first_set.intersection(second_set)
print("Intersection is ", common)

# Remove common elements from first_set
first_set = first_set - common
print("First Set after removing common element ", first_set)


# -----------------------------
# EXERCISE 7
# -----------------------------
print("\n=========== Exercise 7 ===========")
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("\nFirst set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

# If one is subset/superset of the other, clear it
if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("\nFirst Set ", first_set)
print("Second Set ", second_set)


# -----------------------------
# EXERCISE 8
# -----------------------------
print("\n=========== Exercise 8 ===========")
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}

# We only want roll numbers that appear in the dictionary VALUES
valid_values = sample_dict.values()

# Build a new list with only valid roll numbers
filtered_roll = []
for num in roll_number:
    if num in valid_values:
        filtered_roll.append(num)

print("After removing unwanted elements from list", filtered_roll)


# -----------------------------
# EXERCISE 9
# -----------------------------
print("\n=========== Exercise 9 ===========")
speed = {
    "jan": 47,
    "feb": 52,
    "march": 47,
    "April": 44,
    "May": 52,
    "June": 53,
    "july": 54,
    "Aug": 44,
    "Sept": 54,
}

unique_values = []

# Add values only if not already added
for v in speed.values():
    if v not in unique_values:
        unique_values.append(v)

print(unique_values)


# -----------------------------
# EXERCISE 10
# -----------------------------
print("\n=========== Exercise 10 ===========")
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_items = []

# Remove duplicates while keeping original order
for n in sample_list:
    if n not in unique_items:
        unique_items.append(n)

print("unique items", unique_items)

unique_tuple = tuple(unique_items)
print("tuple", unique_tuple)

print("min:", min(unique_tuple))
print("max:", max(unique_tuple))
