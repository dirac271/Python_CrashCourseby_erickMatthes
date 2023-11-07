#5-10. Checking Usernames:
current_users = ['dirac','robert','albert','werner','enrico']
new_users = ['richard','ROBERT','sabrina','werner','ale']
for new_user in new_users:
    if(new_user.lower() in current_users):
        print("you will need to enter a new username")
    else:
        print("the username is available")