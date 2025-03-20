class ZaehlGerade:
    @staticmethod
    def zaehlen(zahlenListe):
        zaehler = 0
        for zahl in zahlenListe:
            # Wenn die Zahl durch 2 teilbar ist, wird der Zähler erhöht.
            if zahl % 2 == 0:
                zaehler += 1
        return zaehler

zahlenListe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ergebnis = ZaehlGerade.zaehlen(zahlenListe)
print(f"Die Anzahl der geraden Zahlen in {zahlenListe} ist: {ergebnis}")

