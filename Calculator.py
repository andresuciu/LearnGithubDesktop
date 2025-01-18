class Calculator_AS:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def adunare(self):
        return print(f"Rezultatul adunarii este: {self.a + self.b}")

    def scadere(self):
        return print(f"Rezultatul scaderii este: {self.a - self.b}")

Calculator_AS(2,3).adunare()
Calculator_AS(2,3).scadere()
