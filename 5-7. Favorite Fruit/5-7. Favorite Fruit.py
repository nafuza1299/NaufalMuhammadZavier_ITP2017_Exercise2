favorite_fruits = ["Apple", "Orange", 'Watermelon']
if "Apple" in favorite_fruits:
    print("I really like apples")
if "Banana" in favorite_fruits:
    print("I really like bananas!")
else:
    print("I don't like bananas that much.")
if "Orange" in favorite_fruits:
    print("Nothing rhymes with"+ " "+favorite_fruits[1])
if "Watermelon" in favorite_fruits:
    print(favorite_fruits[2]+ " "+"is perfect for summer!")
if "Grapes" in favorite_fruits:
    print("I love grapes!")
else:
    print("I like"+ " " +str(favorite_fruits[:]), 'better')
