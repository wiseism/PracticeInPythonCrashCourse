# Python Crash Course chapter 2 practice
# Linhe

def main():
    # practice 2-1
    msg1 = "This is practise 2-1."
    print(msg1)

    # practice 2-2
    msg2 = "This is practise 2-2."
    print(msg2)

    msg2 = "Now the message has changed."
    print(msg2)

    # practice 2-3
    usrname = "Linhe"
    msg = "Hello " + usrname + ", would you like to learn some Python today?"
    print(msg)
    print("Hello " + usrname + ", would you like to learn some Python today?")

    # practice 2-4
    name = 'linhe sun'
    print(name.title())
    print(name.upper())
    print(name.lower())

    # practice 2-5
    print('Albert Einstein said, "A person who never made a mistake never tried anything new."')

    # practice 2-6
    famous_person = "albert einstein"
    message = '"A person who never made a mistake never tried anything new."'
    print(famous_person.title() + " said, " + message)

    # practice 2-7
    name = "\tLinhe Sun\n"
    print(name)
    print(name.lstrip())
    print(name.rstrip())
    print(name.strip()) 
    # the strip() will not delete the space in the middle of it.

    #practice 2-8
    print(2 + 6)
    print(11 -3)
    print(2 * 4)
    print(8 / 1)
    print(24 / 3)

    # practice 2-9
    number = 7
    print("My lucky number is " + str(number) + ".")

    # practice 2-10
    # this line is an annotation

    # practice 2-11
    import this

if __name__ == "__main__":
    main()