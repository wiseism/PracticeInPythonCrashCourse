#Chapter 7 practice
# Linhe Sun

def main():
    # practice 7-1
    car = input("Tell me what type of cars you want?\n")
    print("Let me see if I can find you a(n) " + car.title() + ".")

    # practice 7-2
    number = input("Hello, could you tell me how many people will come for dinner?")
    if int(number) > 8:
        print("Sorry, there are no empty tables now.")
    else:
        print("Welcome, the waitress will show you the way.")

    # practice 7-3
    number = input("Type a number to test if it can be exact divided by 10:\n")
    if int(number) % 10 == 0:
        print("Yes")
    else:
        print("No")
        
    # practice 7-4
    prompt = "Please tell us what you want to add in your pizza:"
    prompt += "\n(Type quit to quit)\n"

    message = ""
    while message.lower() != "quit":
        message = input(prompt)
        if message.lower() != "quit":
            print("OK, we will add " + message + " in your pizza!")

    # practice 7-5
    age = input("Please tell us your age:\n")
    if int(age) < 3:
        print("You can watch the film free.")
    elif int(age) < 12:
        print("You should pay $10.")
    else:
        print("You should pay $15.")

    # practice 7-6
    prompt = "Please tell us your age:\n"
    age = ""
    while age == "":
        age = input(prompt)
        if int(age) < 3:
            print("You can watch the film free.")
        elif int(age) < 12:
            print("You should pay $10.")
        else:
            print("You should pay $15.")

    prompt = "Please tell us your age:\n"
    age = ""
    active = True
    while active == True:
        age = input(prompt)
        if int(age) < 3:
            print("You can watch the film free.")
        elif int(age) < 12:
            print("You should pay $10.")
        else:
            print("You should pay $15.")
        active = False
        
    prompt = "Please tell us your age:"
    prompt += "\n(Type quit to quit)\n"
    age = ""
    active = True
    while active == True:
        age = input(prompt)
        if age.lower() == "quit":
            break
        elif int(age) < 3:
            print("You can watch the film free.")
        elif int(age) < 12:
            print("You should pay $10.")
        else:
            print("You should pay $15.")

    # practice 7-7
    prompt = "Please tell us your age:"
    prompt += "\n(This is a infinite loop)\n"
    age = ""
    active = True
    while active == True:
        age = input(prompt)
        if age.isdigit():
            if int(age) < 3:
                print("You can watch the film free.")
            elif int(age) < 12:
                print("You should pay $10.")
            else:
                print("You should pay $15.")
        else:
            print("You should type a number!")

    # practice 7-8
    sandwich_orders = ['tuna', 'vegetable', 'chicken']
    finished_sandwiches = []
    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        print("I made your " + sandwich + " sandwich.")
        finished_sandwiches.append(sandwich)
    print("These sandwiches are made:")
    for sandwich in finished_sandwiches:
        print(sandwich.title() + " Sandwich.")

    # practice7-9
    sandwich_orders = ['tuna', 'vegetable', 'chicken']
    sandwich_orders += ['pastrami', 'apple', 'pastrami', 'chicken', 'pastrami']
    print(sandwich_orders)
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        print(sandwich_orders)

    #practice 7-10
    places = {}
    active = True
    while active == True:
        name = input("Please tell us your name:\n")
        place = input("If you could visit one place in the world, where would you go?\n")
        places[name] = place
        repeat = 'yes'
        while repeat:
            repeat = input("Would you like to let another person respond?(yes/no)\n")
            if repeat.lower() == 'yes':
                print("Thanks.")
                break
            elif repeat.lower() == 'no':
                active = False
                break
            else:
                print("Please type yes or no.\n")

    for name, place in places.items():
        print(name.title() + " want to visit " + place.title() + " the most in the world.")

if __name__ == "__main__":
    main()