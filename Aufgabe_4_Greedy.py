class AktivitaetsWaehler:
    def __init__(self, alleAktivitäten):
        self.gesamtAngebotAktivitaeten = alleAktivitäten

    def waehleAktivitaeten(self):
        print("Unsortierte Aktivitäten:", self.gesamtAngebotAktivitaeten)
        # Sortieren der Aktivitäten nach Endzeit mit Hilfe einer anonymen Lambda-Funktion, 
        # die das zweite Element (Endzeit) zurückgibt.
        self.gesamtAngebotAktivitaeten.sort(key=lambda x: x[1])
        print("Sortierte Aktivitäten:", self.gesamtAngebotAktivitaeten)

        # Die erste Aktivität aus der sortierten Aktivitätsliste wird ausgewählt.
        ausgewaehlteAktivitaeten = [self.gesamtAngebotAktivitaeten[0]]
        print("Ausgewählte Aktivitäten:", ausgewaehlteAktivitaeten)
        #last_end_time = self.activities[0][1]
        letzteEndzeit = ausgewaehlteAktivitaeten[0][1]
        print("Letzte Endzeit:", letzteEndzeit)

        for i in range(1, len(self.gesamtAngebotAktivitaeten)):
            # Wenn die Startzeit der aktuellen Aktivität größer oder gleich der Endzeit der letzten Aktivität ist, 
            # wird die Aktivität zu ausgewaehlteAktivitaeten hinzugefügt.
            if self.gesamtAngebotAktivitaeten[i][0] >= letzteEndzeit:
                print("Aktivität", self.gesamtAngebotAktivitaeten[i], "wurde hinzugefügt.")
                ausgewaehlteAktivitaeten.append(self.gesamtAngebotAktivitaeten[i])
                letzteEndzeit = self.gesamtAngebotAktivitaeten[i][1]
        return ausgewaehlteAktivitaeten

# Beispiel: Aktivitäten (Startzeit, Endzeit)
alleAktivitäten = [(2, 6), (2, 5), (1, 5), (6, 8), (5, 6)]
waehler = AktivitaetsWaehler(alleAktivitäten)
ergebnis = waehler.waehleAktivitaeten()
print("Ausgewählte Aktivitäten (Greedy):", ergebnis)
print("Anzahl der ausgewählten Aktivitäten:", len(ergebnis))

