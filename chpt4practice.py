#Chapter 4 practice
# Linhe Sun

def main():
    # practice 4-1
    pizzas = ['pepperoni pizza', 'fruit pizza', 'mushroom pizza']
    for pizza in pizzas:
        print(pizza)
        
    for pizza in pizzas:
        print("I like " + pizza +".")

    print("I really love pizza!")

    # practice 4-2
    animals = ['chicken', 'seagull', 'penguin']
    for animal in animals:
        print(animal)

    for animal in animals:
        print(animal.title() + " have wings!")

    print("All these animals have wings!")

    # practive 4-3
    for i in range(1,21):
        print(i)

    # practive 4-4
    nums = list(range(1,1000001))
    print(nums[-1])
    # for num in nums:
    #	print(num)

    # practive 4-5
    print(min(nums))
    print(max(nums))
    print(sum(nums))

    # practice 4-6
    odds = list(range(1, 21, 2))
    for odd in odds:
        print(odd)

    # practice 4-7
    divnums = list(range(3, 31, 3))
    for divnum in divnums:
        print(divnum)

    # practice 4-8
    cubes = []
    for i in range(1,11):
        cubes.append(i**3)
    for cube in cubes:
        print(cube)
        
    # practice 4-9
    cubes = [value**3 for value in range(1,11)]
    print(cubes)

    # practice 4-10
    print("The first three items in the list Cubes are: " + str(cubes[:3]) +".")
    print("Three items from the middle of the list Cubes are: " + str(cubes[4:7]) +
        ".")
    print("The last three items in the list Cubes are: " + str(cubes[-3:]) +".")

    # practice 4-11
    friend_pizzas = pizzas[:]
    pizzas.append('beef pizza')
    friend_pizzas.append('cucumber pizza')
    print("My favorite pizzas are:")
    for pizza in pizzas:
        print(pizza)
    print("My friend's favorite pizzas are:")
    for pizza in friend_pizzas:
        print(pizza)

    # practice 4-12
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    my_foods.append('cannoli')
    friend_foods.append('ice cream')
    print("My favorite foods are:")
    for food in my_foods:
        print(food)
    print("My friend's favorite foods are:")
    for food in friend_foods:
        print(food)
        
    # practice 4-13
    foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
    print("This resturant serves:")
    for food in foods:
        print(food)

    # foods[0] = 'milk'
    foods = ('pizza', 'falafel', 'carrot cake', 'chips', 'milk')
    print("This resturant now serves:")
    for food in foods:
        print(food)
        
    # practice 4-14
    # http://python.org/dev/peps/pep-0008/

    #practice 4-15

    # practice 4-15
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    my_foods.append('cannoli')
    friend_foods.append('ice cream')
    print("My favorite foods are:")
    for food in my_foods:
        print(food)
    print("My friend's favorite foods are:")
    for food in friend_foods:
        print(food)

if __name__ == "__main__":
    main()
