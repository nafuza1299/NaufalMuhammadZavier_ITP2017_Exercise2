cubes = ['1', '8', '27', '64', '125']
print("The first three items in the list are:")
for cube in cubes[:3]:
    print(cube.title())

print("The items in the middle of the list are:")
for cube in cubes[1:4]:
    print(cube.title())

print("The last three items are:")
for cube in cubes[2:5]:
    print(cube.title())
