#Let's start a coffee shop togther!! We're 
# going to build a coffee shop using some new
# python programming concepts!!! Robot Barista.......

print("Hello, Welcome  to Sharp Jr. Coffee sessions!!!!!!!!!!")

name = input("What is your name?\n")

print("Hello" +" " + name + "," " thank you so much for coming in today\n")  
menu = "Expresso, Black Coffee, Latte, Cappuciano"

print(name +", " + "What would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = input("How many Coffees would you like?\n")

total = price * int(quantity)

print("Thank you"".Your total price is: $" + str(total))

print("Sounds good "+name+ ", we'll have your"+" " +quantity+" " +order+" "+"ready for you in a moment.")