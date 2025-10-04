# 1. Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("1. Combined list:", combined)

# 2. Find the largest and smallest elements
numbers = [3, 7, 1, 9, 2]
print("2. Largest:", max(numbers))
print("   Smallest:", min(numbers))

# 3. Square each number in a list
nums = [2, 4, 6]
squared = [x**2 for x in nums]
print("3. Squared values:", squared)

# 4. Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = [x for x in a if x in b]
print("4. Common elements:", common)

# 5. Find the longest word and its length
words = ["apple", "banana", "kiwi", "strawberry"]
longest = max(words, key=len)
print("5. Longest word:", longest, "with length:", len(longest))

# 6. Count occurrences of each element
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
print("6. Occurrences:", counts)

# 7. Remove duplicates from a list of names
names = ["John", "Alice", "John", "Bob", "Alice"]
unique_names = list(set(names))
print("7. Unique names:", unique_names)

# 8. Sort list of strings by length
strings = ["a", "apple", "pear", "banana"]
sorted_by_length = sorted(strings, key=len)
print("8. Sorted by length:", sorted_by_length)

# 9. Check if list is sorted in ascending order
lst = [1, 2, 3, 4, 5]
is_sorted = lst == sorted(lst)
print("9. Is sorted ascending?", is_sorted)

# 10. Union of two lists (unique elements)
list_a = [1, 2, 3]
list_b = [3, 4, 5]
union = list(set(list_a + list_b))
print("10. Union of lists:", union)
