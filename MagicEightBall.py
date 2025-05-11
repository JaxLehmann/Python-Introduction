# Write code below 💖
import random
num = random.randint(1,9)
userinput = input("Ask a yes or no question: ")
if num == 1:
  answer = ("Yes - definitely.")
elif num == 2:
  answer = ("Better not tell you now.")
elif num == 3:
  answer = ("My sources say so.")
elif num == 4:
  answer = ("Very Doubtful.")
elif num == 5:
  answer = ("Outlook not so good.")
elif num == 6:
  answer = ("It is decidedly so")
elif num == 7:
  answer = ("Reply hazy, try again.")
elif num == 8:
  answer = ("Ask again later.")
elif num == 9:
  answer = ("It is very uncertain.")
else:
  answer = ("error!")
print ('Magic 8 Ball: ' + answer)