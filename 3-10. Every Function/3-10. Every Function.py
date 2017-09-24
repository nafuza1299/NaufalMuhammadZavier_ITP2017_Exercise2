items = ["Mountain", "sky", "Ocean", "Cyclone"]
items.sort()
print(items)
items.reverse()
print(items)
print(items[0])
print(items[1].title(), items[0].upper(), items[3].lower())
print(items[-1])
message = "I want to fly to the"+ " " +items[0]
print(message)
items[0] = "Volcano"
print(items)
items.append("Forest")
print(items)
items.insert(0, "Jungle")
print(items)
del items[2]
print(items)
removed_items = items.pop(3)
print(items)
print(removed_items)
items.remove("Jungle")
print(items)
items.sort(reverse=True)
print(sorted(items))
print(reversed(items))
items[:] = []
print(items)
