def greet_user(name, age):
    if age < 0:
        return "Invalid age"
    return f"Hello {name}, you are {age} years old."