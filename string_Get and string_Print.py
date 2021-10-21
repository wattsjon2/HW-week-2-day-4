import os
os.system('cls' if os.name == 'nt' else 'clear')

class String():

    def __init__(self, string_input):
        self.string_input = string_input

    def getString(self):
        new_string = input("Please enter a new string ")
        self.string_input = new_string
    
    def printString(self):
        print(self.string_input.upper())

def run():
    my_string = String("")
    my_string.getString()
    my_string.printString()

run()