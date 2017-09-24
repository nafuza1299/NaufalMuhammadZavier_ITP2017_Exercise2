#This is the correct version of the program
#Tests for equality and inequality with strings
pizza = 'cheese'
print("\nIs pizza == 'cheese'? I predict True.")
print(pizza == 'cheese')
print("\nIs pizza == 'burger'? I predict False.")
print(pizza == 'burger')

pizza = 'cheese'
print("\nIs pizza != 'cheese'? I predict False.")
print(pizza != 'cheese')
print("\nIs pizza == 'burger'? I predict True.")
print(pizza != 'burger')
#-----------------------------------------
#Tests using the lower() function
fruits = "Orange"
print('\nIs orange the same as Orange? I predict True')
print(fruits.lower() == "orange")
print('\nIs orange the same as Orange? I predict False')
print(fruits == "orange")

#-----------------------------------------
#Tests using the and keyword and the or keyword
a = 22
b = 45
print("\nIs a >= 22 or b >= 52? I predict True")
print(a >= 22 or b >= 52)

print("\nIs a >= 52 or b >= 52? I predict False")
print(a >= 52 or b >= 52)

print("\nIs a >= 22 and b >= 22? I predict True")
print(a >= 22 and b >= 22)

print("\nIs a >= 22 and b >= 22? I predict False")
print(a >= 52 and b >= 52)

#-----------------------------------------
#Test whether an item is in a list
list = ["Ice", "Fire","Lightning", "Wind"]
print('\nIs Ice in the list? I predict True')
print("Ice" in list)

print('\nIs Water in the list? I predict False')
print("Water" in list)

print('\nIs Water not in the list? I predict True')
print("Water" not in list)

print('\nIs Ice not in the list? I predict False')
print("Ice" not in list)
#-----------------------------------------
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
value = 19
print("\nIs value < 20? I predict True")
print(value < 20)

print("\nIs value < 18? I predict False")
print(value < 18)

print("\nIs value > 20? I predict False")
print(value > 20)

print("\nIs value > 11? I predict True")
print(value > 11)

print("\nIs value == 19? I predict True")
print(value == 19)

print("\nIs value == 20? I predict False")
print(value == 20)

print("\nIs value >= 19? I predict True")
print(value >= 19)

print("\nIs value >= 23? I predict False")
print(value >= 23)

print("\nIs value <= 19? I predict True")
print(value <= 19)

print("\nIs value <= 18? I predict False")
print(value <= 18)


