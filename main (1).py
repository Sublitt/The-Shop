#Building a shop with Python commands
#strings equal ""
#varibles are an object

#Greet customer
print("Hello! Welcome to the coffee shop.")

#Ask your customer what their name is with the input() function and store that in the variable NAME
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation
#NESTED ifs
if name == "Ben" or name == "Patricia" or name == "Loki":
  trespassing_status = input("Are you trespassing?\n")
  good_deeds = int(input("How many good deeds have you done today?\n"))
  if trespassing_status == "Yes" and good_deeds < 4:
    print("You're not welcome here " + name + "! Please leave!")
    exit()
  else:
    print("I'm sorry about that, welcome to the shop " + name + "!")
else:
  print("Hello " + name + ", thank you for coming in today!\n\n\n")

#Coffee menu
menu = "Black Coffee, Latte, Cappucino, Espresso, Frappuccino"

#Ask the customer what they would like feom the menu and store it in the variable order
print(name + ", what would you like from our menu today?\n Here is what we are serving.\n"  + menu)

order = input()


#Ask customer how many coffee they would like and store it in the variable Quantity
quantity = input("How many coffees would you like?\n")

#setting individual prices
if order == "Frappuccino":
  price = 13
elif order == "Black Coffee":
  price = 3
elif order == "Espresso":
  price = 4
elif order == "Latte":
  price = 9
elif order == "Capuccino":
  price = 10
else:
  print("Sorry, we don't have that here.")
  price = 0

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")

total = price * int(quantity)

print("Your total is: $" + str(total))

