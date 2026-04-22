## Import entire module
import random
import datetime
import json

number = random.randint(1,10)
choice = random.choice(["Apple","Mango","Banana"])
print(number)
print(choice)


#Common built-in modules
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

today = datetime.date.today()
print(today)  # 2024-01-15