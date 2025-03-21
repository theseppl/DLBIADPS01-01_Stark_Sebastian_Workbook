class DynamischerAktivitaetsWaehler:
    def __init__(self, alleAktivitaeten):
        self.gesamtAngebotAktivitaeten = alleAktivitaeten
    def waehleAktivitaeten(self):
        # Sortiert Aktivitäten nach Endzeit
        self.gesamtAngebotAktivitaeten.sort(key=lambda x: x[1])
        laengeGesamtListe = len(self.gesamtAngebotAktivitaeten)

        # Array welches die maximale Anzahl an Aktivitäten bis zur i-ten Aktivität speichert
        arrayMaxAnzahlAktivitaeten = [0] * laengeGesamtListe
        # Array welches die Position der vorhergehenden Aktivität speichert.
        # -1 bedeutet, dass keine Aktivität gewählt wurde.
        arrayVorhergehendeAktivitaeten = [-1] * laengeGesamtListe
        # Die erste Aktivität kann aus der sortierten Liste immer gewählt werden.
        arrayMaxAnzahlAktivitaeten[0] = 1  

        for i in range(1, laengeGesamtListe):
            # Aktivität auswählen. 
            # Die Variable letzteOhneUeberschneidung erhält solange den Index -1 bis eine Aktivität ohne Überschneidung gefunden wird.
            waehlen = 1
            letzteOhneUeberschneidung = -1
            # for-Schleife wird rückwärts durchlaufen, um die letzte Aktivität ohne Überschneidung zu finden.
            for j in range(i - 1, -1, -1):
                # Wenn die Endzeit der j-ten Aktivität kleiner oder gleich der 
                # Startzeit der i-ten Aktivität ist, dann gibt es keine Überschneidung.
                if self.gesamtAngebotAktivitaeten[j][1] <= self.gesamtAngebotAktivitaeten[i][0]:
                    # waehlen wird um die Anzahl der Aktivitäten erhöht, die bis zur j-ten Aktivität gewählt wurden.
                    waehlen += arrayMaxAnzahlAktivitaeten[j]
                    letzteOhneUeberschneidung = j
                    break

            # Variable auschliessen erhält den Wert der Anzahl der Aktivitäten, die bis zur i-ten Aktivität gewählt wurden.
            auschliessen = arrayMaxAnzahlAktivitaeten[i - 1]

            # Aktivitäten wählen oder ausschließen und Entscheidung speichern.
            if waehlen > auschliessen:
                arrayMaxAnzahlAktivitaeten[i] = waehlen
                arrayVorhergehendeAktivitaeten[i] = letzteOhneUeberschneidung
            else:
                arrayMaxAnzahlAktivitaeten[i] = auschliessen
                arrayVorhergehendeAktivitaeten[i] = arrayVorhergehendeAktivitaeten[i - 1]

        # Zusätzliche Ausgabe der ausgewählten Aktivitäten
        ausgewaehlteAktivitaeten = []
        i = laengeGesamtListe - 1
        while i >= 0:
            if arrayVorhergehendeAktivitaeten[i] != arrayVorhergehendeAktivitaeten[i - 1]:
                ausgewaehlteAktivitaeten.append(self.gesamtAngebotAktivitaeten[i])
                i = arrayVorhergehendeAktivitaeten[i]
            else:
                i -= 1
        # Aktivitäten in chronologischer Reihenfolge ausgeben
        ausgewaehlteAktivitaeten.reverse()  
        return arrayMaxAnzahlAktivitaeten[-1], ausgewaehlteAktivitaeten
# Beispiel
aktivitaeten = [(2, 4), (2, 5), (5, 6), (6, 8), (1, 6)]
waehler = DynamischerAktivitaetsWaehler(aktivitaeten)
maxAnzahlAktivitaeten, ausgewaehlteAktivitaeten = waehler.waehleAktivitaeten()
print("Maximale Anzahl Aktivitäten (Dynamisch):", maxAnzahlAktivitaeten)
print("Ausgewählte Aktivitäten:", ausgewaehlteAktivitaeten)


