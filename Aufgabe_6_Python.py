class ZaehlGerade:
    @staticmethod
    def zaehlen(numbers):
        count = 0
        for number in numbers:
            if number % 2 == 0:
                count += 1
        return count

beispiel_liste = [1, 2, 3, 4, 5, 6]
ergebnis = ZaehlGerade.zaehlen(beispiel_liste)
print(f"Die Anzahl der geraden Zahlen in {beispiel_liste} ist: {ergebnis}")

