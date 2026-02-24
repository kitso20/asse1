def greet_user(name, age):
    if age < 0:
        return "Invalid age"
    return f"Hello {name}, you are {age} years old."

def classify_temperature(celsius):
    if celsius < 0:
        return "Freezing"
    elif celsius <= 20:
        return "Chilly"
    elif celsius <= 35:
        return "Warm"
    else:
        return "Hot"
    