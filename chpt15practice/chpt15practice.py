# Chapter 15 practice
# Linhe Sun

import matplotlib.pyplot as plt
import numpy as np
from random import choice

class RandomWalk():
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]
        
    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
        
    def fill_walk(self):
        
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            
            if x_step == 0 and y_step == 0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return choice(range(1, self.num_sides + 1))

def main():
    # practice 15-1
    x_values = [1,2,3,4,5]
    y_values = [x**3 for x in x_values]
    
    plt.scatter(x_values, y_values, c='purple', s=40)
    
    plt.title("Cube Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Cube of Value", fontsize=14)
    plt.tick_params(axis='both', labelsize=12)
    
    plt.show()
    
    x_values = list(range(1,5001))
    y_values = [x**3 for x in x_values]
    
    plt.scatter(x_values, y_values, c='purple', s=40)
    
    plt.title("Cube Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Cube of Value", fontsize=14)
    plt.tick_params(axis='both', labelsize=12)
    
    plt.show()
    
    # practice 15-2
    x_values = list(range(1,5001))
    y_values = [x**3 for x in x_values]
    
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=40)
    
    plt.title("Cube Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Cube of Value", fontsize=14)
    plt.tick_params(axis='both', labelsize=12)
    
    plt.show()
    
    # practice 15-3
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()
        
        plt.figure(dpi=128, figsize=(10, 6))
        
        point_numbers = list(range(rw.num_points))
        plt.plot(rw.x_values, rw.y_values, c='violet', linewidth=1)
            
        plt.scatter(0, 0, c='deeppink', edgecolors='none', s=50)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='midnightblue', edgecolors='none',
            s=50)
            
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
            
        plt.show()
        
        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break
            
    # practice 15-6
    try:
        import pygal
        
        die_1 = Die()
        die_2 = Die()
        
        results = []
        for roll_num in range(1000):
            result = die_1.roll() + die_2.roll()
            results.append(result)
            
        frequencies = []
        x_labels = []
        max_result = die_1.num_sides + die_2.num_sides
        for value in range(2, max_result+1):
            frequency = results.count(value)
            frequencies.append(frequency)
            x_labels.append(str(value))
            
        hist = pygal.Bar()
        
        hist.title = "Results of rolling two D6 dice 1000 times."
        hist.x_labels = x_labels
        hist.x_title = "Result"
        hist.y_title = "Frequency of Result"
        
        hist.add('D6 + D6', frequencies)
        hist.render_to_file('dice_visual.svg')
        
        # practice 15-7
        die_1 = Die(8)
        die_2 = Die(8)
        
        results = []
        for roll_num in range(1000):
            result = die_1.roll() + die_2.roll()
            results.append(result)
            
        frequencies = []
        x_labels = []
        max_result = die_1.num_sides + die_2.num_sides
        for value in range(2, max_result+1):
            frequency = results.count(value)
            frequencies.append(frequency)
            x_labels.append(str(value))
            
        hist = pygal.Bar()
        
        hist.title = "Results of rolling two D6 dice 1000 times."
        hist.x_labels = x_labels
        hist.x_title = "Result"
        hist.y_title = "Frequency of Result"
        
        hist.add('D8 + D8', frequencies)
        hist.render_to_file('dice_visual.svg')
        
        # practice 15-8
        die_1 = Die()
        die_2 = Die()
        die_3 = Die()
        
        results = []
        for roll_num in range(1000):
            result = die_1.roll() + die_2.roll() + die_3.roll()
            results.append(result)
            
        frequencies = []
        x_labels = []
        max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
        for value in range(3, max_result+1):
            frequency = results.count(value)
            frequencies.append(frequency)
            x_labels.append(str(value))
            
        hist = pygal.Bar()
        
        hist.title = "Results of rolling two D6 dice 1000 times."
        hist.x_labels = x_labels
        hist.x_title = "Result"
        hist.y_title = "Frequency of Result"
        
        hist.add('D6 + D6 + D6', frequencies)
        hist.render_to_file('dice_visual.svg')
        
        # practice 15-9
        die_1 = Die()
        die_2 = Die()
        
        results = []
        for roll_num in range(1000):
            result = die_1.roll() * die_2.roll()
            results.append(result)
            
        frequencies = []
        x_labels = []
        max_result = die_1.num_sides * die_2.num_sides
        for value in range(1, max_result+1):
            frequency = results.count(value)
            frequencies.append(frequency)
            x_labels.append(str(value))
            
        hist = pygal.Bar()
        
        hist.title = "Results of rolling two D6 dice 1000 times."
        hist.x_labels = x_labels
        hist.x_title = "Result"
        hist.y_title = "Frequency of Result"
        
        hist.add('D6 * D6', frequencies)
        hist.render_to_file('dice_visual.svg')
        
        # II. use pygal draw dot plot
        rw = RandomWalk(5000)
        rw.fill_walk()
        
        xy_chart = pygal.XY(stroke=False)   
        xy_chart.add('Walk', [(rw.x_values[i], rw.y_values[i]) for i in range(0, 5000)])
        
        xy_chart.render_to_file('random_walk.svg')
    except ImportError:
        print("pygal library not found, skipping pygal examples")
    
    # practice 15-10
    # I. use matplotlib draw barplot
    die_1 = Die()
    die_2 = Die()
    
    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)
        
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)
        
    N = len(frequencies)
    ind = np.arange(N) 
    plt.bar(ind, frequencies, 0.35)
    plt.title('Results of rolling two D6 dice 1000 times.', fontsize=18)
    plt.xticks(ind, ('2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))
    plt.xlabel('Result', fontsize=14)
    plt.ylabel('Frequency of Result', fontsize=14)
    plt.tick_params(axis='both', labelsize=14)
    
    plt.show()

if __name__ == "__main__":
    main()
