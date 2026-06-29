# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def sumEven(num):
#     total = 0
#     for i in range(num + 1):
#         if i % 2 == 0:
#             total += i
#     return total


def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    if guess < secret:
        return "too low"
    return "too high"
