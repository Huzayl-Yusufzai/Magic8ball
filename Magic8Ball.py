import random

Name = input("What's your name")
question = input("What's your question")

Answer = ""
random_number = random.randint(1, 9)

if random_number == 1: 
  Answer = "Yes - definitely"
elif random_number == 2: 
  Answer = "It is decidedly so."
elif random_number == 3: 
  Answer = "Without a doubt."
elif random_number == 4: 
  Answer = "Reply hazy, try again."
elif random_number == 5: 
  Answer = "Ask again later."
elif random_number == 6: 
  Answer = "Better not tell you now."
elif random_number == 7: 
  Answer = "My sources say no."
elif random_number == 8: 
  Answer = "Outlook not so good"
elif random_number == 9: 
  Answer = "Very doubtful."
else:
  Answer = "Error"

print(Name + " asks: " + question)
print("Magic 8-Ball's answer" + Answer)
