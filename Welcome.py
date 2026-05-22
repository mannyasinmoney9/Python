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


total = 0

for i in range(1, 6):
    if i % 2 != 0:
        total = total + i

print("Sum of odd numbers:", total)