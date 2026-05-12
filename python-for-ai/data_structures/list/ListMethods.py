#List Methods
numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy

nums = [1,2,3,4]

nums.append(5)
print(nums)
nums.insert(1, 10)
print(nums)
nums.remove(2)
print(nums)
nums.pop()
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)