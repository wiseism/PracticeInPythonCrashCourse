#Chapter 6 practice
# Linhe Sun

def main():
    # practice 6-1
    information = {
        'first_name': 'Hanlin',
        'last_name': 'Wang',
        'age': 25,
        'city': 'Chengdu'
        }

    # practice 6-2
    lucky_nums = {
        'Hanlin': 8,
        'Linhe': 7,
        'Yulin': 6
        }
    print("Hanlin's lucky number is: " + str(lucky_nums['Hanlin']))
    print("Linhe's lucky number is: " + str(lucky_nums['Linhe']))
    print("Yulin's lucky number is: " + str(lucky_nums['Yulin']))

    # practice 6-3
    words = {
        'sum': 'sum all the numbers',
        'min': 'find the smallest number',
        'max': 'find the biggest number',
        'str': 'turn number to character string',
        'lower': 'lower case all the letters'
        }
    print("sum: " + words['sum'] + "\nmin: " + words['min'] + "\nmax: " + 
        words['max'] + "\nstr: " + words['str'] + "\nlower: " + words['lower'])

    # practice 6-4
    print("\n")
    words = {
        'sum': 'sum all the numbers',
        'min': 'find the smallest number',
        'max': 'find the biggest number',
        'str': 'turn number to character string',
        'lower': 'lower case all the letters',
        'set': 'gather the lists',
        'items': 'return keys and values in a dict',
        'keys': 'return keys in a dict',
        'values': 'return values in a dict',
        'title': 'capital the 1st letter in a word'
        }
    for key, value in words.items():
        print(key + ": " + value)
        
    # practice 6-5
    rivers = {'nile': 'egypt', 'ganges': 'india', 'yangzi': 'china'}
    for key, value in rivers.items():
        print("The " + key.title() + " runs through " + value.title() + ".")
    for river in rivers.keys():
        print(river)
    for nation in rivers.values():
        print(nation)

    # practice 6-6
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
        }

    survey_names = ['edward', 'sarah', 'hanlin', 'linman']
    for name in survey_names:
        if name in favorite_languages.keys():
            print(name.title() + ", thanks for taking the survey!")
        else:
            print(name.title() + ", we are inviting you to take an easy survey.")

    # practice 6-7
    information1 = {
        'first_name': 'Hanlin',
        'last_name': 'Wang',
        'age': 25,
        'city': 'Chengdu'
        }
    information2 = {
        'first_name': 'Linman',
        'last_name': 'Zhu',
        'age': 25,
        'city': 'Shenzhen'
        }
    information3 = {
        'first_name': 'Qiaoxian',
        'last_name': 'Li',
        'age': 24,
        'city': 'Shenzhen'
        }
    informations = [information1, information2, information3]
    for inform in informations:
        print("\n")
        for key, value in inform.items():
            print(key + ": " + str(value))

    # practice 6-8
    mimi = {'name': 'mimi', 'type': 'dog', 'master': 'Shuo Wang'}
    shining = {'name': 'shining', 'type': 'cat', 'master': 'Linhe Sun'}
    liaoge = {'name': 'liaoge', 'type': 'parrot', 'master': 'Tenglong Song'}
    pets = [mimi, shining, liaoge]
    for pet in pets:
        print("\n")
        for key, value in pet.items():
            print(key + ": " + value)

    # practice 6-9
    favorite_places = {
        'Linhe': ['Nanjing', 'Chengdu', 'Tokyo'],
        'Yaoyao': ['Nanjing', 'Beijing', 'New York'],
        'Kuanye': ['Beijing', 'Nanjing', 'Qiqihar', 'Qingdao']
        }
    for name, places in favorite_places.items():
        print(name + "'s favorite places are:")
        for place in places:
            print("    " + place)

    # practice 6-10
    lucky_nums = {
        'Hanlin': [8, 16, 99, 999],
        'Linhe': [7, 9, 108],
        'Yulin': [6, 666]
        }
    for name, nums in lucky_nums.items():
        print(name + " likes these numbers:")
        for num in nums:
            print("    " + str(num))

    # practice 6-11
    cities = {
        'Beijing': {
            'coutry': 'China',
            'population': '20 million',
            'fact': 'It is the capital of China.'
            },
        'Tokyo': {
            'coutry': 'Japan',
            'population': '9.2 million',
            'fact': 'It is the capital of Japan.'
            },
        'New York': {
            'coutry': 'USA',
            'population': '8.2 million',
            'fact': 'It has 2 MLB baseball teams inside.'
            }
        }
    for city, infos in cities.items():
        print("Here are some information of " + city + ":")
        for key, value in infos.items():
            print("    " + key + ": " + value)
            
    # practice 6-12
    # modify the 6-11
    for city in sorted(cities.keys()):
        print("Here are some information of " + city + ":\n    " + "It's in " + 
            cities[city]['coutry'] + " with a population of " + 
            cities[city]['population'] + ". " + cities[city]['fact'])

if __name__ == "__main__":
    main()