class GaussSumme:
    @staticmethod
    def berechneSumme(n):
        if n == 1:
            return 1
        else:
            return n + GaussSumme.berechneSumme(n - 1)

n = 100
ergebnis = GaussSumme.berechneSumme(n)
print(f"Die Summe der ersten {n} natürlichen Zahlen ist: {ergebnis}")
