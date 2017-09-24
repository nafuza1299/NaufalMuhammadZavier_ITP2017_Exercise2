guest = ["Father","Son","Spirit"]
message = "Welcome to the party has been invited to the party this evening"
print("Hello"+ " "+guest[0], message)
print("Hello"+ " "+guest[1], message)
print("Hello"+ " "+guest[2], message)
unable = "However,"+ " " +guest[0], 'could not attend to the event'
print(unable)
guest[0] = "Mother"
message2 = ",Father was unable to make it to the event, instead mother has been invited. Best Regards to all."
print("Hello"+ " "+guest[0]+ " " +message2)
print("Hello"+ " "+guest[1]+ " " +message2)
print("Hello"+ " "+guest[2]+ " " +message2)
print("We have found a bigger table.")
guest.insert( 0, "Kentucky")
guest.insert( 1, "John")
guest.append("Tim")
print("Hello"+ " "+guest[0], message)
print("Hello"+ " "+guest[1], message)
print("Hello"+ " "+guest[2], message)
print("Hello"+ " "+guest[3], message)
print("Hello"+ " "+guest[4], message)
print("We can only invite two people to dinner")
apology = "Sorry your are no longer invited"+ " " +guest.pop(0)
print(apology)
apology = "Sorry your are no longer invited"+ " " +guest.pop(1)
print(apology)
apology = "Sorry your are no longer invited"+ " " +guest.pop(2)
print(apology)
apology = "Sorry your are no longer invited"+ " " +guest.pop(2)
print(apology)
dont_worry = "You are still invited"+ " " +guest[0]
print(dont_worry)
dont_worry = "You are still invited"+ " " +guest[1]
print(dont_worry)
del guest[:]
print(guest[:])
