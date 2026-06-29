# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///


#def main() -> None:
   # name = input("Enter your name: ")
    #age = int(input("Enter your age: "))
  #  email = input("Enter your email: ")
   # location = input("Enter your location: ")
   # birth_year = input("Enter your birth year:")

    #print("\n--- USER PROFILE ---")
   # print("Name:", name)
    #print("Age: ", age)
   # print("Email:", email)
   # print("Location:", location)
   # print("Birth_year:", birth_year)
    #print("--------------------")

#main()

#user_score = int(input("Enter your survival score (0-100): "))

#print("--- Calculating Results ---")

#if user_score >= 70:
   # print("Rank: Elite Explorer. You mastered the terrain!")

#elif user_score >= 50:
    #print("Rank: Scout. Good run, you made it through safe.")

#elif user_score >= 40:
    #print("Rank: Scavenger. Scraping by, but you are still standing.")

#else:
  #  print("Rank: Ghost. The wild got the best of you this time.")

#for i in range(1, 6):
    #print(i)

#Write only to sum only the odd numbers


#odd = 0

#for i in range(1, 6):
    #if i % 2 != 0:
       # odd = odd + i

#print("Sum of odd numbers:", odd)

#take input from the user to sum odd numbers up to a certain limit using the while loop using int and input

#total = 0

#while True:
    #num = int(input("enter number, 0 to Stop: "))
    #if num ==0:
        #break
    #total += num
    #print(f"SUm = {total}")

    #Write a python program use range from 1-6 but once it reaches 3 break and then print out the result.

#for row in range(1, 6):
    #for column in range(1, 6):
        #print(row * column, end=" ")
    #print()


print("Star triangle")
rows = 5
# rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    for column in range(row):
        print("*", end=" ")
    print()

print()
print("Square")
size = 5
# size = int(input("Enter size of square: "))

for row in range(size):
    for column in range(size):
        print("*", end=" ")
    print()

print()
print("Heart")
print(" **   ** ")
print("**** ****")
print(" ********")
print("  ******")
print("   ****")
print("    **")
