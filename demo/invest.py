# wir importieren das Modul pyplot aus dem Paket matplotlib
# damit wir nicht jedes Mal, wenn wir das Modul verwenden
# "matplotlib.pyplot" schreiben müssen, geben wir dem ganzen
# den kürzeren Namen "plt"
import matplotlib.pyplot as plt


# wir definieren eine Funktion, die einen bestimmten Zinssatz (in Prozent)
# auf einen Startwert anwendet
def wende_zinsen_an(anfangswert, zinssatz):
    # Wenn der Zinssatz -100% ist, haben wir ein Problem...
    if zinssatz <= -100:
        print("OOPSIE")
        neuer_wert = 0
    else:
        neuer_wert = anfangswert * (1 + zinssatz / 100)

    # damit die Funktion nicht "ins Leere läuft", müssen wir das Ergebnis zurückgeben
    return neuer_wert


# zum Ausprobieren:
print(wende_zinsen_an(100, 5))
# -> 105
print(wende_zinsen_an(100, -200))
# -> OOPSIE
# -> 0


# gleiches Konzept, wir definieren eine Funktion, dieses Mal für den Zinseszins
# über mehrere Jahre
def zinseszins(anfangswert, zinssatz, anzahl_jahre):
    # in Python kann man mit "**" eine Potenz ausrechnen
    ergebnis = anfangswert * (1 + zinssatz / 100) ** anzahl_jahre
    return ergebnis


# Jetzt wollen wir ausrechnen, was passiert, wenn wir jeden Monat eine bestimmte Summe
# Geld investieren und am Ende des Jahres darauf Zinsen erhalten
def sparplan(anfangswert, einzahlung, zinssatz, anzahl_jahre):
    # wir brauchen zwei sogenannte Helfervariablen, die den Wert unseres Geldes "tracken"
    aktueller_wert = anfangswert
    summe_einzahlungen = anfangswert

    # wir müssen jetzt den gleichen Code sehr oft hintereinander ausführen
    # dazu benutzen wir eine "for Schleife"
    # range(n) zählt hier einfach on 0 bis n-1 hoch: 0 1 2 3 4 .... n-1
    for jahr in range(anzahl_jahre):
        aktueller_wert = aktueller_wert + 12 * einzahlung
        summe_einzahlungen = summe_einzahlungen + 12 * einzahlung

        # hier benutzen wir jetzt eine Funktion, die wir selbst geschrieben haben
        # Damit wir einfacher verstehen, was für Parameter wir der Funktion geben,
        # können wir diese benennen
        aktueller_wert = wende_zinsen_an(anfangswert=aktueller_wert, zinssatz=zinssatz)
        # die folgenden Beispiele würden alle das gleiche tun
        #              = wende_zinsen_an(aktueller_wert, zinssatz) ✅
        #              = wende_zinsen_an(zinssatz=zinssatz, anfangswert=aktueller_wert) ✅
        #              = wende_zinsen_an(anfangswert=aktueller_wert, zinssatz) ✅
        # diese Varianten funktionieren nicht!
        #              = wende_zinsen_an(zinssatz, aktueller_wert) ❌
        #              = wende_zinsen_an(anfangswert=aktueller_wert, zinssatz) ❌

    # wir können ganz einfach mehrere Ergebnisse zurückgeben
    return aktueller_wert, summe_einzahlungen


# zum ausprobieren
print(sparplan(anfangswert=500, einzahlung=10, zinssatz=6, anzahl_jahre=50))


# damit wir uns die Entwicklung anschauen können, brauchen wir nicht nur das
# Endergebnis, sondern auch die Werte aus allen Jahren davor
# Dazu benutzen wir eine Liste


# eine Liste kann viele Elemente des gleichen Typs haben:
# Beispiel:
liste = ["a", "b", "hallo"]
# wir können einzelne Elemente aus der Liste so abfragen:
print(liste[0])  # a
print(liste[2])  # hallo
# wir können auch von hinten anfangen zu zählen:
print(liste[-1])  # hallo
print(liste[-2])  # b
# wir können der Liste mit + Elemente hinzufügen:
liste = liste + ["guten", "tag"]
print(liste[-1])  # "tag"


def sparplan_mit_listen(anfangswert, einzahlung, zinssatz, anzahl_jahre):
    # Anstatt einen einzigen Wert zu "tracken", schreiben wir jedes Jahr einen
    # neuen Wert in eine Liste
    aktueller_wert = [
        anfangswert,
    ]
    summe_einzahlungen = [
        anfangswert,
    ]

    for jahr in range(anzahl_jahre):
        # hier machen wir genau das gleiche wie vorher, aber fügen den neuen Wert immer am Ende der Liste hinzu
        # damit wir den neuen Wert ausrechnen können, brauchen wir allerdings den Wert aus dem letzten Jahr,
        # also das letzte Element aus der Liste.
        wert_dieses_jahr = aktueller_wert[-1] + 12 * einzahlung
        summe_einzahlungen = summe_einzahlungen + [
            summe_einzahlungen[-1] + 12 * einzahlung,
        ]
        wert_dieses_jahr = wende_zinsen_an(wert_dieses_jahr, zinssatz)
        aktueller_wert = aktueller_wert + [
            wert_dieses_jahr,
        ]

    # wir geben zusätzlich noch eine Liste mit den Jahren zurück
    # mit list(range(n)) erzeugen wir aus der Aufzählung eine Liste
    return aktueller_wert, summe_einzahlungen, list(range(anzahl_jahre + 1))


print(sparplan_mit_listen(500, 10, 6, 50))


# wenn wir mehrere Werte zurückgeben, können wir die auch direkt wieder aufteilen
# hier weisen wir folgendermaßen zu:
# aktueller_wert -> werte, summe_einzahlungen -> einzahlungen, list(range(anzahl_jahre + 1)) -> jahre
werte, einzahlungen, jahre = sparplan_mit_listen(500, 10, 6, 50)


# Zum Schluss benutzen wir noch das Modul, was wir ganz am Anfang importiert haben,
# um das Ergebnis schon in einem Graph darzustellen
plt.plot(jahre, einzahlungen, label="Summe der Einzahlungen")
plt.plot(jahre, werte, label="Aktueller Wert")
plt.grid()  # fügt dem Plot ein Grid hinzu
plt.legend()  # sorgt dafür, dass die label, die wir oben definiert haben, auch im plot auftauchen
plt.show()  # öffnet ein neues Fenster mit dem Ergebnis
