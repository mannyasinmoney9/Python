
low = 1
high = 100
attempts = 0

print("Think of a number between 1 and 100. I will guess it!")
print("Type: 'too low', 'too high', or 'correct'")

while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"\nMy guess: {guess}")

    result = input("Your response: ").strip().lower()

    if result == "correct":
        print(f"Got it in {attempts} attempts!")
        break
    if result == "too low":
        low = guess + 1
    elif result == "too high":
        high = guess - 1
    else:
        print("Please type 'too low', 'too high', or 'correct'")
