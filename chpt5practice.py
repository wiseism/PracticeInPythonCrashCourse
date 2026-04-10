#Chapter 5 practice
# Linhe Sun

def main():
    # practice 5-1
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("Is car == 'audi'? I predict False.")
    print(car == 'audi')
    print("Is car != 'subaru'? I predict False.")
    print(car != 'subaru')
    print("Is car != 'audi'? I predict True.")
    print(car != 'audi')

    cars = ['audi', 'subaru']
    print("\nIs 'BMW' in cars? I predict False.")
    print('BMW' in cars)
    print("Is 'audi' in cars? I predict True.")
    print('audi' in cars)
    print("Is 'BMW' not in cars? I predict True.")
    print('BMW' not in cars)
    print("Is 'audi' not in cars? I predict False.")
    print('audi' not in cars)

    num = 18
    print("\nIs 20 bigger than num? I predict True.")
    print(20 > num)
    print("Is 16 bigger than num? I predict False.")
    print(16 > num)

    # practice 5-2
    car = 'Subaru'
    print("Is car == 'Subaru'? I predict True.")
    print(car == 'Subaru')
    print("Is car == 'Audi'? I predict False.")
    print(car == 'Audi')

    print("\nIs car == 'subaru'? I predict True.")
    print(car.lower() == 'subaru')
    print("Is car == 'audi'? I predict False.")
    print(car.lower == 'audi')

    num = 18
    print("\nIs 18 equal num? I predict True.")
    print(18 == num)
    print("Is 18 un-equal num? I predict False.")
    print(18 != num)
    print("Is 20 bigger than num? I predict True.")
    print(20 > num)
    print("Is 16 bigger than num? I predict False.")
    print(16 < num)
    print("Is 20 >= num? I predict True.")
    print(20 >= num)
    print("Is 18 <= num? I predict True.")
    print(18 <= num)

    print("\nIs 18 equal to num & 20 bigger than num? I predict True")
    print(18 == num and 20 > num)
    print("Is 18 equal to num & 20 less than num? I predict False")
    print(18 == num and 20 < num)
    print("Is 18 equal to num or 20 bigger than num? I predict True")
    print(18 == num or 20 > num)
    print("Is 18 equal to num or 20 less than num? I predict True")
    print(18 == num or 20 < num)

    cars = ['audi', 'subaru']
    print("\nIs 'BMW' in cars? I predict False.")
    print('BMW' in cars)
    print("Is 'audi' in cars? I predict True.")
    print('audi' in cars)
    print("Is 'BMW' not in cars? I predict True.")
    print('BMW' not in cars)
    print("Is 'audi' not in cars? I predict False.")
    print('audi' not in cars)

    # practice 5-3
    alien_colors = ['green', 'yellow', 'red']
    for alien_color in alien_colors:
        if alien_color == 'green':
            print("You got 5 points!")


    # practice 5-4
    for alien_color in alien_colors: 
        if alien_color == 'green':
            print("You got 5 points!")
        else:
            print("You got 10 points!")
        
    # practice 5-5
    for alien_color in alien_colors: 
        if alien_color == 'green':
            print("You got 5 points!")
        elif alien_color == 'yellow':
            print("You got 10 points!")
        else:
            print("You got 15 points!")

    # practice 5-6
    ages = [1, 3, 5, 14, 25, 67]
    for age in ages:
        if age < 2:
            print("He/She is an infant.")
        elif age < 4:
            print("He/She is starting to walk.")
        elif age < 13:
            print("He/She is a child.")
        elif age < 20:
            print("He/She is a teenager.")
        elif age < 65:
            print("He/She is an adult.")
        else:
            print("He/She is old.")

    # practice 5-7
    fruits = ['banana', 'apple', 'peach']
    if 'banana' in fruits:
        print("You really like bananas!")
    if 'watermelon' in fruits:
        print("You really like watermelons!")
    if 'peach' in fruits:
        print("You really like peaches!")
    if 'apple' in fruits:
        print("You really like apples!")
    if 'pear' in fruits:
        print("You really like pears!")

    # practice 5-8
    usrs = ['admin', 'Jiaxin', 'Hanlin', 'Xueqing', 'Linman']
    for usr in usrs:
        if usr == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + usr + ", thank you for logging in again.")

    # practice 5-9
    usrs = []
    if usrs:
        for usr in usrs:
            if usr == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print("Hello " + usr + ", thank you for logging in again.")
    else:
        print("We need to find some users!")
        
    #practice 5-10
    current_users = ['admin', 'Jiaxin', 'Hanlin', 'Xueqing', 'Linman']
    current_users_lower = [current_user.lower() for current_user in current_users]
    new_users = ['Yulin', 'Qiaoxian', 'Hanlin', 'Linman', 'Xiaobin']
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print("You need to use another user name.")
        else:
            print("This name has not been taken.")

    # practice 5-11
    nums = list(range(1,10))
    for num in nums:
        print(num)
    for num in nums:
        if num == 1:
            print(str(num) + "st")
        elif num == 2:
            print(str(num) + "nd")
        elif num == 3:
            print(str(num) + "rd")
        else:
            print(str(num) + "th")
            
    # practice 5-12
    # I think they are all OK.

    # practice 5-13
    # I have more interests in data mining.

if __name__ == "__main__":
    main()