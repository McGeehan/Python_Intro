name = input("What is your name?") #this is an input for a user to type
print("Hi there, " + name) #it "prints" or shows text in the terminal
#then it concatenates a string with the person's input
print(name + " is a lovely name.")
print("Hi " + name + "! Let me make sure your name is " + name + "?")

email = input("What is your email?")
nickname = input("What is your nickname?")
address = input("What is your address?")

age = int(input("Please enter your age: "))

print("Wow " + name + "you are " + str(age)
      + "!" + "I didn't know they made email for someone so old!"
      + "Thanks for your email:"
      + email + "and" + address
      + "and your nickname: " + nickname)
