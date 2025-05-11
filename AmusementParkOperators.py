# Write code below 💖

#and
#or
#not

# equivalent to Java's &&, ||, !

height = int(input("How tall are you? "))
credits = int(input("How many credits do you have? "))

if height >= 137 and credits >= 10:
  print ("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print ("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print ("You don't have enough credits.")
else:
  print ("You have not met either requirement.")