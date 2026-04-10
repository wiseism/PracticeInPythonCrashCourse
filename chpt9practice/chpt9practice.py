#Chapter 9 practice
# Linhe Sun

# practice 9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a(n) " + self.cuisine_type + 
            " restaurant.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now.")

# practice 9-3
class User():
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + 
            " is a user of our production.")
    
    def greet_user(self):
        print("Hi " + self.first_name.title() + ", welcome back!")

# practice 9-4
class RestaurantWithServed():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a(n) " + self.cuisine_type + 
            " restaurant.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now.")
        
    def set_number_served(self, sv_number):
        if sv_number >= self.number_served:
            self.number_served = sv_number
        print(str(self.number_served) + " people are served.")
    
    def increment_number_served(self, in_number):
        if in_number >= 0:
            self.number_served += in_number
        print(str(self.number_served) + " people are served.")

# practice 9-5
class UserWithLogin():
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0
        
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + 
            " is a user of our production.")
    
    def greet_user(self):
        print("Hi " + self.first_name.title() + ", welcome back!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# practice 9-6
class RestaurantWithServedDefault():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a(n) " + self.cuisine_type + 
            " restaurant.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now.")
        
    def set_number_served(self, sv_number):
        if sv_number >= self.number_served:
            self.number_served = sv_number
        print(str(self.number_served) + " people are served.")
    
    def increment_number_served(self, in_number):
        if in_number >= 0:
            self.number_served += in_number
        print(str(self.number_served) + " people are served.")

class IceCreamStand(RestaurantWithServedDefault):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = ['strawberry', 'chocolate', 'apple']
        
    def describe_icecreams(self):
        print("We have these kinds of icecreams:")
        for flavor in self.flavors:
            print("    - " + flavor)

# practice 9-7
class Admin(UserWithLogin):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self, nums=[2]):
        for num in nums:
            print(self.first_name.title() + " " + self.last_name.title() + " " +
                self.privileges[num] + ".")

# practice 9-8
class Previleges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self, nums=[2]):
        for num in nums:
            print("This admin " + self.privileges[num] + ".")
    
class AdminWithPrivileges(UserWithLogin):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.previleges = Previleges()

# practice 9-9
class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        
class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

# practice 9-14
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

def main():
    # practice 9-1
    restaurant = Restaurant('qiaojiangnan', 'Chinese dish')
    print("If you want to eat " + restaurant.cuisine_type + ", go to " + 
        restaurant.restaurant_name.title() + ".")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    # practice 9-2
    restaurant1 = Restaurant('K F C', 'hamburger')
    restaurant2 = Restaurant('dairy queen', 'ice cream')
    restaurant3 = Restaurant('haidilao', 'hot pot')
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    # practice 9-3
    userwang = User('Hanlin', 'Wang')
    userniu = User('yulin', 'niu')
    userli = User('hua', 'li')
    userwang.describe_user()
    userwang.greet_user()
    userniu.describe_user()
    userniu.greet_user()
    userli.describe_user()
    userli.greet_user()

    # practice 9-4
    restaurant = RestaurantWithServed('qiaojiangnan', 'Chinese dish')
    restaurant.describe_restaurant()
    restaurant.set_number_served(6)
    restaurant.increment_number_served(3)

    # practice 9-5
    userniu = UserWithLogin('yulin', 'niu')
    userniu.increment_login_attempts()
    userniu.increment_login_attempts()
    userniu.increment_login_attempts()
    print(userniu.login_attempts)
    userniu.reset_login_attempts()
    print(userniu.login_attempts)

    # practice 9-6
    dq = IceCreamStand('dairy queen', 'ice cream')
    dq.describe_icecreams()

    # practice 9-7
    admin = Admin('yulin', 'niu')
    admin.show_privileges()
    nums = [0,1,2]
    admin.show_privileges(nums)
    admin.show_privileges([1,2])

    print("\n")
    # practice 9-8
    admin = AdminWithPrivileges('qiaoxian', 'li')
    admin.previleges.show_privileges([0,1])

    # practice 9-9
    newcar = ElectricCar('tesla', 'model', 2016)
    newcar.battery.get_range()
    newcar.battery.upgrade_battery()
    newcar.battery.get_range()

    # practice 9-10
    # the file is restaurant.py
    try:
        from restaurant import Restaurant
        restaurant = Restaurant('qiaojiangnan', 'Chinese dish')
        restaurant.describe_restaurant()
        restaurant.set_number_served(6)
        restaurant.increment_number_served(3)
    except ImportError:
        print("restaurant module not found")

    # practice 9-11
    # the file is usr.py
    try:
        from usr import User, Previleges, Admin
        admin = Admin('jiaxin', 'luo')
        admin.previleges.show_privileges([0,1])
    except ImportError:
        print("usr module not found")

    # practice 9-12
    # the files are user.py prevad.py
    try:
        from user import User   # without this line still OK
        from prevad import Previleges, Admin
        admin = Admin('lijian', 'huang')
        admin.previleges.show_privileges([0,1])
    except ImportError:
        print("user or prevad module not found")

    # practice 9-13
    from collections import OrderedDict
    words = OrderedDict()

    words['sum'] = 'sum all the numbers'
    words['min'] = 'find the smallest number'
    words['max'] = 'find the biggest number'
    words['str'] = 'turn number to character string'
    words['lower'] = 'lower case all the letters'
    words['set'] = 'gather the lists'
    words['items'] = 'return keys and values in a dict'
    words['keys'] = 'return keys in a dict'
    words['values'] = 'return values in a dict'
    words['title'] = 'capital the 1st letter in a word'
        
    for key, value in words.items():
        print(key + ": " + value)
        
    # practice 9-14
    die6 = Die()
    for i in range(0,10):
        die6.roll_die()

    die10 = Die(10)
    die20 = Die(20)
    for i in range(0,10):
        die10.roll_die()
    for i in range(0,10):
        die20.roll_die()
        
    # practice 9-15
    # http://pymotw.com/

if __name__ == "__main__":
    main()
