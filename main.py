#Lets build a robot Barista.......

print("Hello, Welcome  to Sharp Jr. Coffee sessions!!!!!!!!!!")

name = input("What is your name?\n")

print("Hello" +" " + name + "," " thank you so much for coming in today\n")  
menu = "Expresso, Black Coffee, Latte, Cappuciano"

print(name +", " + "What would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = input("How many Coffees would you like?\n")

total = price * int(quantity)

print("Thank you "+name+ ".Your total price is: $" + str(total))

print("Sounds good, we will have that"+" " +order+" "+"ready for you in a moment.")