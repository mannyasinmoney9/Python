prices = (10,20,30,40,50)

# Update price 30 to 300
prices_list: list[int] = list(prices)
index = prices_list.index(30)
prices_list[index] = 300
prices = tuple(prices_list)

print(prices)  # (10, 20, 300, 40, 50)

# for price in prices:
#  if price < 30:

#  print(price)



#  membership operator
# print(30 in prices)  # True-----|this is a boolean
# print(60 in prices)  # False----|this is a boolean

# numbers = (1,2,1,3,1)
# # print(numbers.count(1))

# print (prices.index(40))
# matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))


def calculate(a, b):
    return (
        ("addition",       a + b),
        ("subtraction",    a - b),
        ("multiplication", a * b),
        ("modulus",        a % b),
        ("division",       a / b),
    )

result = calculate(10, 3)
for a, b in result:
    print(f"{a}: {b}")

