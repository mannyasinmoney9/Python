#def addTwo(a, b):
   # return a + b

#sum = addTwo(40,7)
#print(f"Sum = {sum}")

#def greet2(name="Mann"):
    #return f"Hello, {name}"
#print(greet2("Mann"))

#def rectangle_area(length, width):
    #return length * width

#length = int(input("Enter length: "))
#width = int(input("Enter width: "))
#area = rectangle_area(length, width)
#print(f"Area = {area}")

#def total(*nums):
#    sum_of_num = 0

  #  for n in nums:
  #      sum_of_num += n

  #  return sum_of_num

#print(total(1,2,3,4,5,6))


#square = lambda x : x * x
#cube = lambda mann: mann*mann**3

#print(square(3))
#print(cube(4))


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(4))


# We have triangle mode of blocks. The topcat row has 1 block,
# the next row down has 2 blocks, the next row down has 3 blocks, and so on.
# Compute recursively (no loops or multiplication)
# If we have n rows of blocks, how many blocks do we have in total? Write a recursive function to solve this problem.
# the total numner of blocks in suck a triangle withe the given number of rows.

# Example




# def greet(name):
#     """Takes a name and returns a greeting message."""
#     return f"Hello, {name}!"

# print(greet("Mann"))

# def show(**info):
#     for k,v in info.items():
#         print(f"{k}: {v}")

#         show(name = "")


def odd_numbers(n):
    if n % 2 != 0:
        print(n, "is odd")
    else:
        print(n, "is even")

num = int(input("Enter a number: "))
odd_numbers(num)


def calculate(a, b):
    return {
        "addition":       a + b,
        "subtraction":    a - b,
        "multiplication": a * b,
        "modulus":        a % b,
        "division":       a / b,
    }

result = calculate(10, 3)
for operation, value in result.items():
    print(f"{operation}: {value}")
