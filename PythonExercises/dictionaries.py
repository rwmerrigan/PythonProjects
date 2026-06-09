
#region Task 1: Create a Dictionary 
student = {
    "name": "Alice", 
    "age": 18, 
    "grade": "A"
}
print(student)
#endregion

#region Task 2: Access Values
car = {
    "brand": "Toyota",
    "model": "Camry", 
    "year": 2022
}
print(car["brand"] + ' ' + car["model"])
#endregion

#region Task 3: Add a New Key
person = {
    "name": "John",
    "age": 25
}
person["city"] = "Chicago"
print(person)
#endregion

#region Task 4: Update a Value 
book = {
    "title": "Python Basics",
    "pages": 200
}
book["pages"] = 250
print(book)
#endregion

#region Task 5: Check if a Key Exists
user = {
    "username": "coder123",
    "email": "coder@example.com"
}
if "email" in user:
    print("Email exists")
else:
    print("Email not found")
#endregion

#region Task 6: Remove a Key
inventory = {
    "apple": 10, 
    "banana": 5, 
    "orange": 8
}
del inventory["banana"]
print(inventory)
#endregion

#region Task 7: Print All Keys
movie = {
    "title": "Inception",
    "year": 2010, 
    "rating": 8.8
}
for key in movie:
    print(key)
#endregion

#region Task 8: Print all Values
for value in movie.values():
    print(value)
#endregion

#region Task 9: Print Key-Value Pairs
scores ={
    "John": 95,
    "Karen": 88,
    "Suzy": 91
}
for name, score in scores.items():
    print(f"{name}: {score}")
#endregion

#region Task 10: Sum All Values
expenses = {
    "food": 120, 
    "transport": 50, 
    "entertainment": 75
}
total = sum(expenses.values())
print(total)
#endregion

#region Task 11: Find the Highest Value
grades = {
    "Alice": 85, 
    "Bob": 92, 
    "Charlie": 78,
    "Diana": 95
}
# the key=grades.get tells the max function to compare the items in the iterable
# of grades.get, .get() is a dictionary method that retrieves the value associated
# with a key
top_student = max(grades, key=grades.get)
print(grades.get)
#endregion




