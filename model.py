import math as m

class calcul:
    def multiplication(self, a, b):
        return a * b
    
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def racine(self, a):
        if a < 0:
            raise ValueError("Erreur")
        return a ** 0.5
    
    def puissance(self, a, b):
        return a ** b

    def logarithme(self, a):    
        return m.log(a)

    def exponentielle(self, a):
        return m.exp(a)

    def inverse(self, a):
        if a == 0:
            raise ValueError("Erreur")
        return 1 / a
    
    def sinus(self, a):
        return m.sin(a)
        

    def cosinus(self, a):
        return m.cos(a)

    def tangente(self, a):
        return m.tan(a)
        
