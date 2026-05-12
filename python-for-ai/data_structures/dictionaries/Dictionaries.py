# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Different ways to create
scores = dict(math=95, english=87, science=92)


# Accessing values
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get values by key
print(person["name"])       # "Alice"
print(person["age"])        # 30

# Safer with get()
print(person.get("job"))    # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)

#Changing dictionaries
person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 31                   # Update existing

# Remove items
del person["email"]              # Remove by key
age = person.pop("age")          # Remove and return
person.clear()                   # Remove all items