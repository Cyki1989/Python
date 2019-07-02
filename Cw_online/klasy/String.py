'''
class String:

    def get_string(self):
        self.string = input('Enter a string: ')       

    def print_string(self):
        print(self.string.upper())



A = String()
A.get_string()
A.print_string()
'''

class String:

    def __init__(self):
        self.string = input('Enter a string: ')       

    def __str__(self):
        return self.string.upper()

print(String())    
