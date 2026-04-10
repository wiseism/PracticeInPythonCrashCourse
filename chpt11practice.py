# Chapter 11 practice
# Linhe Sun

# practice 11-1
def city_function(city, country, population=''):
    if population:
        result = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        result = city.title() + ', ' + country.title()
    return result

# practice 11-3
class Employee():
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
    
    def give_raise(self, increace=5000):
        self.salary += increace

import unittest

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formated_city = city_function('beijing', 'china')
        self.assertEqual(formated_city, 'Beijing, China')
        
    def test_city_country_population(self):
        formated_city  = city_function('beijing', 'china', 20000000)
        self.assertEqual(formated_city, 'Beijing, China - population 20000000')

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_test = Employee('Linhe', 'Sun', 2000)
        self.increace = 6000
    
    def test_give_default_raise(self):
        self.my_test.give_raise()
        self.assertEqual(self.my_test.salary, 7000)

    def test_give_custom_raise(self):
        self.my_test.give_raise(self.increace)
        self.assertEqual(self.my_test.salary, 8000)

class TestAll(unittest.TestCase):
    def test_city_function(self):
        result = city_function('tokyo', 'japan')
        self.assertEqual(result, 'Tokyo, Japan')
        
    def test_employee_raise(self):
        emp = Employee('John', 'Doe', 50000)
        emp.give_raise(10000)
        self.assertEqual(emp.salary, 60000)

if __name__ == '__main__':
    # Run all tests
    unittest.main()
    
    # Example usage of the functions
    print("\nExample usage:")
    print(city_function('paris', 'france'))
    print(city_function('new york', 'usa', 8000000))
    
    emp = Employee('Alice', 'Smith', 60000)
    print(f"Employee: {emp.first_name} {emp.last_name}, Salary: ${emp.salary}")
    emp.give_raise()
    print(f"After raise: ${emp.salary}")
    emp.give_raise(3000)
    print(f"After custom raise: ${emp.salary}")

