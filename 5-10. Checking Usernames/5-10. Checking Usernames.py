current_users = ["theundertaker", "billytheboss", "timmy134", "ftbll_plyr", "jonathan.turner"]
new_users = ["light_yagami", "billytheboss", "misa_misa", "theundertaker", "L"]
for new_user in new_users:
    if new_user in current_users:
        print("The name", new_user, "has been taken")
    else:
        print("The name"+ " " +new_user+ " " +"is available")


