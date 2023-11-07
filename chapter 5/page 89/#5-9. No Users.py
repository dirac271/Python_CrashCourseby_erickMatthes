#5-9. No Users: 
usernames = []
if(usernames):
    for username in usernames:
        if(username == 'admin'):
            print("hey admin, would u like to see a status report")
    else:
        print(f"hello {username} thank u for logging in again")
else:
    print("We need to find some users!")