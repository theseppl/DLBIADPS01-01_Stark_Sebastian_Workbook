class GaussSumme:
    # Statische Methode zur Berechnung der Summe der ersten n natürlichen Zahlen.
    @staticmethod
    def berechneSumme(n):
        # Speicherplatz wird für diesen Funktionsaufruf reserviert (Stack).
        
        # Basisfall: Wenn n gleich 1 ist, wird 1 zurückgegeben
        if n == 1:  
            return 1
        
        # Rekursiver Fall: Die Funktion ruft sich mit (n-1) erneut auf, 
        # ohne den aktuellen Aufruf zu beenden.
        # Stack wird genutzt, um die Zwischenergebnisse zu speichern.
        else: 
            return n + GaussSumme.berechneSumme(n - 1)
        # Sobald die Rekursion auf den Basisfall zurückkehrt, werden die Zwischenergebnisse kombiniert.

n = 2
ergebnis = GaussSumme.berechneSumme(n)

# Ausgabe des Ergebnisses.
print(f"Die Summe der ersten {n} natürlichen Zahlen ist: {ergebnis}")
