import matplotlib.pyplot as plt


# berechne zinsen auf betrag x
def wende_zinsen_an(anfangswert, zinssatz):
    if zinssatz <= -100:
        print("OOPSIE")
    else:
        neuer_wert = anfangswert * (1 + zinssatz / 100)

    return neuer_wert


ergebnis = wende_zinsen_an(100, 5)
print(ergebnis)  # 105


def zinseszins(anfangswert, zinssatz, anzahl_jahre):
    ergebnis = anfangswert * (1 + zinssatz / 100) ** anzahl_jahre
    return ergebnis


def sparplan(anfangswert, einzahlung, zinssatz, anzahl_jahre):
    aktueller_wert = anfangswert
    summe_einzahlungen = anfangswert
    for jahr in range(anzahl_jahre):
        aktueller_wert = aktueller_wert + 12 * einzahlung
        summe_einzahlungen = summe_einzahlungen + 12 * einzahlung
        aktueller_wert = wende_zinsen_an(anfangswert=aktueller_wert, zinssatz=zinssatz)

    return aktueller_wert, summe_einzahlungen


print(sparplan(anfangswert=500, einzahlung=10, zinssatz=6, anzahl_jahre=50))


# liste = [1,2,3,4,5]
# liste[-1] -> 5
# liste[0] -> 1


def sparplan_mit_listen(anfangswert, einzahlung, zinssatz, anzahl_jahre):
    aktueller_wert = [
        anfangswert,
    ]
    summe_einzahlungen = [
        anfangswert,
    ]
    for jahr in range(anzahl_jahre):
        wert_dieses_jahr = aktueller_wert[-1] + 12 * einzahlung
        summe_einzahlungen = summe_einzahlungen + [
            summe_einzahlungen[-1] + 12 * einzahlung,
        ]
        wert_dieses_jahr = wende_zinsen_an(wert_dieses_jahr, zinssatz)
        aktueller_wert = aktueller_wert + [
            wert_dieses_jahr,
        ]

    return aktueller_wert, summe_einzahlungen, list(range(anzahl_jahre + 1))


print(sparplan_mit_listen(500, 10, 6, 50))

werte, einzahlungen, jahre = sparplan_mit_listen(500, 10, 6, 50)

plt.plot(jahre, einzahlungen, label="Summe der Einzahlungen")
plt.plot(jahre, werte, label="Aktuelle Wert")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
