# Definition der Klasse "GaussSumme"
class GaussSumme:
    # Statische Methode zur Berechnung der Summe der ersten n natürlichen Zahlen
    @staticmethod
    def berechneSumme(n):
        # Basisfall: Wenn n gleich 1 ist, endet die Rekursion hier und es wird 1 zurückgegeben
        if n == 1:
            return 1
        else:
            # Rekursiver Aufruf: Addiere n zur Summe der vorherigen (n-1) Zahlen
            return n + GaussSumme.berechneSumme(n - 1)

# Die Zahl, bis zu der die Summe berechnet werden soll
n = 100

# Aufruf der Methode und Speichern des Ergebnisses in der Variable "ergebnis"
ergebnis = GaussSumme.berechneSumme(n)

# Ausgabe des Ergebnisses
print(f"Die Summe der ersten {n} natürlichen Zahlen ist: {ergebnis}")
