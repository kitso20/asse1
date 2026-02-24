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
    
def sum_even_numbers(numbers):
    return sum([i for i in numbers if i % 2 == 0])

def fizz_buzz_list(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
