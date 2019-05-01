

# creating the inputoutput class
class InputOutput(object):
    def __init__(self):
        self.a= ""

    def getString(self):  # getString method
        self.a=input("Enter the string: ")

    def printString(self): # printString method
        print(self.a.upper())

obj=InputOutput() # Creating the object
obj.getString()
obj.printString()