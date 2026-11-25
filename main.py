def greet(name):
    return f"Hi there, {name}!"
def welcome(name):
    return f"Welcome to our application, {name}!"


print(greet("Python Developer"))
print(welcome("Python Developer"))

def goodbye(name):
    return f"Goodbye, {name}!"

def farewell(name):
    return f"See you later, {name}!"
print(farewell("Python Developer"))


def age_category(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        return "Minor"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"