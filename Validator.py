class Validator:

    def __init__(self, b=0, c=0):
        self.bulls = b
        self.cows = c

    def Izogram(slowo):
         for i in range(len(slowo)):
                for j in range(i + 1, len(slowo)):
                    if (slowo[i] == slowo[j]):
                        print("Słowo nie jest izogramem!")
                        return False
         return True