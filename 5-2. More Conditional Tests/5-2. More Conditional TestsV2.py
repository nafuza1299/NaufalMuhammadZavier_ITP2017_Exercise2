#This version of the program is wrong, but I left it in for reference
#Tests for equality and inequality with strings
burger = "McDonalds"
if burger == "McDonalds":
        print(True)
else:
    print(False)
burger = "McDonalds"
if burger == "BurgerKing":
        print(True)
else:
    print(False)
number = 14
if number != 41:
    print(False)
else:
    print(True)
number = 14
if number != 14:
    print(True)
else:
    print(False)
#-----------------------------------------
#Tests using the lower() function
fruits = ["ORANGE", "BANANA", "GRAPE"]
for fruit in fruits:
    if fruit == "ORANGE":
        print(fruit.lower())
    else:
        print(fruit.title())
#-----------------------------------------
#Tests using the and keyword and the or keyword
a = 22
b = 45
if a >= 22 or b >= 22:
    print(True)
else:
    print(False)

if a >= 52 or b >= 52:
    print(True)
else:
    print(False)

if a >= 22 and b >= 22:
    print(True)
else:
    print(False)

if a >= 52 and b >= 52:
    print(True)
else:
    print(False)
#-----------------------------------------
#Test whether an item is in a list
list = ["Ice", "Fire","Lightning", "Wind"]
if "ee" in list:
    print(True)
else:
    print(False)

list = ["Ice", "Fire","Lightning", "Wind"]
if "Ice" in list:
    print(True)
else:
    print(False)
#-----------------------------------------
#Test whether an item is not in a list
list = ["Apple", "HTC","Samsung", "Nokia"]
if "ee" in list:
    print(True)
else:
    print(False)

list = ["Apple", "HTC","Samsung", "Nokia"]
if "Apple" in list:
    print(True)
else:
    print(False)
#-----------------------------------------
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
value = 19
if value < 20:
    print(True)
else:
    print(False)

if value > 20:
    print(True)
else:
    print(False)

if value == 19:
    print(True)
else:
    print(False)

if value == 20:
    print(True)
else:
    print(False)

if value >= 23:
 print(True)
else:
    print(False)

if value >= 19:
 print(True)
else:
    print(False)

if value >= 23:
 print(True)
else:
    print(False)

if value <= 19:
 print(True)
else:
    print(False)

if value <= 18:
 print(True)
else:
    print(False)



