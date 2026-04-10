# Chapter 10 practice
# Linhe Sun

import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def check_username():
    username = get_stored_username()
    if username:
        msg = "Please check if the username is yours(yes/no)?\n" + username + "\n"
        check = input(msg)
        if check == 'yes':
            return username
        if check == 'no':
            return None
    else:
        return None

def greet_user():
    username = check_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

def main():
    # practice 10-1
    with open('learning_python.txt') as file_object:
        print(file_object.read())
        
    with open('learning_python.txt') as file_object:
        for line in file_object:
            print(line.strip())
            
    with open('learning_python.txt') as file_object:
        lines = file_object.readlines()
        
    for line in lines:
        print(line.strip())
        
    # practice 10-2
    with open('learning_python.txt') as file_object:
        for line in file_object:
            print(line.replace('Python', 'C').strip())
            
    # practice 10-3
    name = input("Please write down your name.\n")
    with open('guest.txt', 'w') as file_object:
        file_object.write(name.title())
    print('Thank you!')

    # practice 10-4
    active = True
    while active == True:
        name = input("Please write down your name.\n(Input q or quit to quit)\n")
        if name.lower() == 'q' or name.lower() == 'quit':
            active = False
        else:
            with open('guest_book.txt', 'a') as file_object:
                line = name.title() + '\n'
                file_object.write(line)
            print(name.title() + ", welcome back!")

    # practice 10-5
    active = True
    while active == True:
        reason = input("Please tell us why you love programming.\n(Input q or quit to quit)\n")
        if reason.lower() == 'q' or reason.lower() == 'quit':
            active = False
        else:
            with open('reasons.txt', 'a') as file_object:
                file_object.write(reason)
                
    # practice 10-6
    print("Input two number. I will give you the sum.")
    num1 = input("First  number:")
    num2 = input("Second number:")
    try:
        thesum = int(num1) + int(num2)
    except ValueError:
        print("Sorry, at least one of them is/are not number(s).")
    else:
        print(thesum)

    # practice 10-7
    while True:
        print("Input two number. I will give you the sum.\n(Input q to quit)")
        num1 = input("First  number:")
        if num1 == 'q':
            break
        num2 = input("Second number:")
        if num2 == 'q':
            break
        try:
            thesum = int(num1) + int(num2)
        except ValueError:
            print("Sorry, at least one of them is/are not number(s).")
        else:
            print(thesum)

    # practice 10-8
    files = ['cats.txt', 'dogs.txt']
    for file in files:
        try:
            with open(file) as f_obj:
                print(f_obj.read())
        except FileNotFoundError:
            print("The file '" + file + "' does not exist.")

    # practice 10-9
    files = ['cats.txt', 'dogs.txt']
    for file in files:
        try:
            with open(file) as f_obj:
                print(f_obj.read())
        except FileNotFoundError:
            pass

    # practice 10-10
    files = ['emma.txt', 'warandpeace.txt', 'TheAdventuresofTomSawyer.txt']
    for file in files:
        try:
            with open(file,'r',encoding='UTF-8') as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            print("The file '" + file + "' does not exist.")
        else:
            times = contents.lower().count('love')
            print("The file " + file + " repeats 'love' for " + str(times) + " times!")
            
    # practice 10-11
    fav_number = input("Please imput your favorite number:\n")
    with open('favorite_number.json', 'w') as f_obj:
        json.dump(fav_number, f_obj)

    with open('favorite_number.json') as f_obj:
        fav_num = json.load(f_obj)
        print("I know your favorite number! It's " + fav_num)
        
    # practice 10-12
    try:
        with open('favorite_number.json') as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        fav_number = input("Please imput your favorite number:\n")
        with open('favorite_number.json', 'w') as f_obj:
            json.dump(fav_number, f_obj)
    else:
        print("I know your favorite number! It's " + fav_num)
        
    # practice 10-13
    greet_user()

if __name__ == "__main__":
    main()

