# Chapter 18 practice
# Linhe Sun

class Topic:
    def __init__(self, name):
        self.name = name
        self.id = 1

class Entry:
    def __init__(self, topic, text):
        self.topic = topic
        self.text = text
        self.date_added = '2023-01-01'
    
    def __str__(self):
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + '...'

def main():
    # practice 18-2: Entry model demonstration
    print("Practice 18-2: Entry Model Demonstration")
    
    # Create a mock topic
    topic = Topic("Python Programming")
    
    # Create entries
    entry1 = Entry(topic, "Learning Python is fun! I'm enjoying the crash course.")
    entry2 = Entry(topic, "Django is a powerful web framework. It makes building web applications easier.")
    entry3 = Entry(topic, "This is a longer entry to demonstrate the __str__ method truncation. " * 5)
    
    # Display entries
    print(f"Entry 1: {entry1}")
    print(f"Entry 2: {entry2}")
    print(f"Entry 3: {entry3}")
    
    print("\nPractice 18-3: Model Structure")
    print("Entry model structure:")
    print("- topic: ForeignKey to Topic")
    print("- text: TextField")
    print("- date_added: DateTimeField (auto_now_add=True)")
    print("- __str__: Returns first 50 characters or full text if shorter")

if __name__ == "__main__":
    main()

