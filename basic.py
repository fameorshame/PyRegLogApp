reg = input(str("Enter the username you would like: "))
if reg == '':
    print("Incorrect, enter a valid username")
else:
    password = input("Nice, " + reg + ", now enter a password: ")
if reg != '':
    login = input("Awesome! Now log in the system using your username: ")
    if login == reg:
        loginPass = input("Nice work, now enter your password: ")
        if loginPass == password:
            print("Yup got it. Your username is " + reg + " and your password is " + password)
        else:
            print("Nope, ending program...")
    else:
        print("Nope, ending program...")
