class InfRates:
    def __init__(self):
        pass

    def userInputFunction(self):
        return input("Please enter a value: ")

    def getV(self):
        self.userInput = float(self.userInputFunction())  # Get user input directly and convert it to a float
        self.V = self.userInput * (1 + (136.4 / 100.0))
        return self.V

infRates = InfRates()
result = infRates.getV()
print("result is:")
print(result)