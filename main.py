

# first = input("what is your first name")
# last = input("what is your last name")
# print(f"you are {last}, {first}")


#loops
#-----------------------------
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

#while loop

# while loop takes a boolean epxression (t/f)

#boolean operations
#---------------------

#comparision operators
# x < 5 (less than)
# x > 5 (greater than)
# x <= 5 (less than or equal too)
# x >= 5 (greater than or equal too)
# x == 5(equal)
# x != 5 (not equal to)

#logical operatos
# and
# or
# not
# infinite loop, watch out for
# counter = 0
# while(counter <= 5):
#   print(counter)
#   counter = counter + 1

# for loops
# range(5) => 0,1,2,3,4.
# counter = 0
# for counter in range(5):
#   print(counter + 1)

#list of numbers
numbers = [1,2,3,4,5]
sum = 0
for counter in range(1,6):
 sum = sum + counter
print(sum)

#conditionals
#----------------------
# definition if x then y
# ex. if i go to school then i will learn


# money = 5
# if money == 5:
#  print("i have 5 dollars")
# elif money == 6:
#  print ("i have 6 dollars")
# elif money == 7:
#  print ("i have 7 dollars")
# else:
#   print("i have a different amount of money")  

# winter, fall, summer, spring
# season = input ("what is the season? ")

# if season == "winter":
#   print("go inside")
# if season == "spring":
#   print("go outside and plant")
# if season == "summer":
#   print("go and water plants")
# if season == "fall"
# print("start to pick the plants")





# guess the number game

import random

computernumber = randomnumber (0-10)
numberoftries = 5
win = false
play = true


while play == true:
  while numberoftries > 0:
    playnumber: input("enter a number between 0-10:")
    playernumber = int(playernumber)


    if playernumber > 10:
      print("bad number")
  else:
    if playernumber < "computernumber":
    print("number too low")
  else:
    if playernumber > computernumber:
    print("number too high")









