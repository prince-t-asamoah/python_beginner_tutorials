config = {"color": "green", "width": 42, "height": 100, "font": "Courier"}

# Access value using its key
print("Access 'color' key value: ", config["color"])

# Update a value
print("Before font update", config)
config["font"] = "Helvetica"

print("After font update", config)


# __dict__ is special attribute mapping attribute names to its value in classes and objects
class Number:
    def __init__(self, value):
        self.value = value


print(Number(42).__dict__)

# Integer, float and boolean object can be used as keys
dict_1 = {42: "aaa", 2.78: "bbb", True: "ccc"}
print(dict_1)

dict_2 = {int: 1, float: 2, bool: 3}
print(dict_2)

dict_3 = {(1, 1): "a", (1, 2): "b"}
print(dict_3[(1, 2)])

# Unhashable objects cannot be used as keys, will throw error
# dict_4 = {[1,2]: 'A list as a key? hmm..'} # type: ignore
# dict_5 = {(1, [1, 1]): 'a'}

# Cannot have multiple keys in dictionary
MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Chicago": "Clubs",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}
MLB_teams["Chicago"] = "Cubs"
print(MLB_teams)


# Dictionary key value can be of any type
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


dict_4 = {
    "colors": ["red", "green", "blue"],
    "plugins": {"py_code", "dev_sugar", "fasting_py"},
    "timeout": 3,
    "position": Point(42, 21),
}
print(dict_4)

# Creating a dictionary with dict constructor using named keys
MLB_teams_dict_constructor = dict(
    Colorado="Rockies",
    Chicago="White Sox",
    Boston="Red Sox",
    Minnesota="Twins",
    Milwaukee="Brewers",
    Seattle="Mariners",
)
print("Dictionary with named keys ", MLB_teams_dict_constructor)

# Creating dictionary with dict constructor using iterable key values
MLB_teams_iterable = dict(
    [
        ("Colorado", "Rockies"),
        ("Chicago", "White Sox"),
        ("Boston", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Milwaukee", "Brewers"),
        ("Seattle", "Mariners"),
    ]
)
print("Dictionary with iterables:", MLB_teams_iterable)

# Creating dictionary with dict constructor using zip with iterables

places = [
    "Colorado",
    "Chicago",
    "Boston",
    "Minnesota",
    "Milwaukee",
    "Seattle",
]
teams = ["Rockies", "White Sox", "Red Sox", "Twins", "Brewers", "Mariners"]

MLB_teams_dict_zip = dict(zip(places, teams))
print("Dictionary with zip: ", MLB_teams_dict_zip)

# Creating dictionary with dict constructor using fromkeys
inventory = dict.fromkeys(["apple", "orange", "banana", "mango"], 0)
print("Dictionary from keys with default value: ", inventory)


# Adding key value pair manually
person = {}

person["first_name"] = "John"
person["last_name"] = "Doe"
person["age"] = 35
person["spouse"] = "Jane"
person["children"] = ["Ralph", "Betty", "Bob"]
person["pets"] = {"dog": "Frieda", "cat": "Sox"}
print(person)

# Adding key value pair with for loop
squares_manually = {}

for integer in range(1, 10):
    squares_manually[integer] = integer**2

print("Dictionary with for loop: ", squares_manually)

squares_with_comprehension = {integer: integer**2 for integer in range(1, 10)}
print("Dictionary with comprehension: ", squares_with_comprehension)


# Using operators with Dictionaries
# Equalityy and Inequality
print([1, 2, 3] == [3, 2, 1])  # False
print({1: 1, 2: 2, 3: 3} == {3: 3, 2: 2, 1: 1})  # True
print([1, 2, 3] != [3, 2, 1])  # True
print({1: 1, 2: 2, 3: 3} != {3: 3, 2: 2, 1: 1})  # False


# Union and Augemented Union
deault_config = {"color": "green", "width": 42, "height": 100, "font": "Courier"}

user_config = {"path": "/home", "color": "red", "font": "Arial", "position": (200, 100)}

config_union = deault_config | user_config
print("Config Union: ", config_union)
config |= user_config
print("Config Augmented Union: ", config)

# Checking for Truthy Data in Dictionaries:
inventory = {"apple": 100, "orange": 80, "banana": 100, "mango": 200}
print("All inventories have values? :", all(inventory.values()))

inventory["mango"] = 0
print("All inventories have values after mango update? :", all(inventory.values()))


# Finding Minimum and Maximum values
computer_parts = {
    "CPU": 299.99,
    "Motherboard": 149.99,
    "RAM": 89.99,
    "GPU": 499.99,
    "SSD": 129.99,
    "Power Supply": 79.99,
    "Case": 99.99,
    "Cooling System": 59.99,
}

print("Min value:", min(computer_parts.values()))
print("Max value:", max(computer_parts.values()))


# Sorting Dictionaries by Keys, Values, and Items: sorted()
students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}
print("Students before sorting: ", students)
print(
    "Students after sorting (asc) by value: ",
    dict(sorted(students.items(), key=lambda item: item[1])),
)
print(
    "Students after sorting (desc) by value: ",
    dict(sorted(students.items(), key=lambda item: item[1], reverse=True)),
)
print(
    "Students after sorting (asc) by key: ",
    dict(sorted(students.items(), key=lambda item: item[0])),
)


# Summing Dictionary Values
daily_sales = {
    "Monday": 1500,
    "Tuesday": 1750,
    "Wednesday": 1600,
    "Thursday": 1800,
    "Friday": 2000,
    "Saturday": 2200,
    "Sunday": 2100,
}
print('Average daily sales:', sum(daily_sales.values()) / len(daily_sales))


# Traversion Dictionaries by Keys
print('Using method 1')
for student in students:
    print(student)
    
print('Using method 2')
for student in students.keys():
    print(student)
    
# Iterating Over Dictionary Values
for student in students.keys():
    print(student)


# Iterating over items
for name, score in students.items():
    print(name, '->', score)

