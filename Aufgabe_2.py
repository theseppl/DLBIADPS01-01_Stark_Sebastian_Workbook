from abc import ABC # Import der abstrakten Basisklasse ABC = "Abstract Base Classes"

# Abstrakte Basisklasse
class Tier(ABC):
    def __init__(self, name, alter, gewicht, mikrochip_id):
        self.name = name
        self.alter = alter
        self.gewicht = gewicht
        self.mikrochip_id = mikrochip_id

    def laut_geben(self):
        return f"{self.name} gibt einen Laut von sich."
    def bewegen(self):
        return f"{self.name} bewegt sich."

# Spezialisierte Unterklasse für Hunde
class Hund(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, gassi_gehen_zeit):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.gassi_gehen_zeit = gassi_gehen_zeit

    def bellen(self):
        return f"{self.name} bellt."
    def gassi_gehen(self):
        return f"{self.name} geht um {self.gassi_gehen_zeit} Gassi."

# Spezialisierte Unterklasse für Katzen
class Katze(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, lieblingsspielzeug):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.lieblingsspielzeug = lieblingsspielzeug

    def miau(self):
        return f"{self.name} miaut."
    def klettern(self):
        return f"{self.name} klettert mit der {self.lieblingsspielzeug} auf einen Baum."

# Spezialisierte Unterklasse für Vögel
class Vogel(Tier):
    def __init__(self, name, alter, gewicht, mikrochip_id, fluegelspannweite):
        super().__init__(name, alter, gewicht, mikrochip_id)
        self.fluegelspannweite = fluegelspannweite

    def zwitschern(self):
        return f"{self.name} zwitschert."
    def fliegen(self):
        return f"{self.name} fliegt mit einer Flügelspannweite von {self.fluegelspannweite} m."

# Beispiel Katze
katze = Katze("Nele", 17, 4, 13062007, "Plüschmaus")

#Ausgabe der Eigenschaften der Katze
print("Die Katze heißt " + katze.name + ".")
print("Die Katze ist " + str(katze.alter) + " Jahre alt.")
print("Die Katze wiegt " + str(katze.gewicht) + " kg.")
print("Die Katze hat die Mikrochip-ID " + str(katze.mikrochip_id) + ".")
print("Die Katze spielt gerne mit ihrer " + katze.lieblingsspielzeug + ".")

#Aufruf der Methoden der Katze
print(katze.miau())
print(katze.klettern())

#Aufruf der von der Basisklasse geerbten Methoden
print(katze.laut_geben()) # Methode der Basisklasse
print(katze.bewegen()) # Methode der Basisklasse