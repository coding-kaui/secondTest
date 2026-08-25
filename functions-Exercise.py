def sag_hallo():
    print("Hallo Welt")


sag_hallo()

#Aufgabe 1 (Einstieg): Einfache Funktion ohne Rückgabe
#Schreibe eine Funktion begruesse_tag(), die (ohne Parameter) den Text "Schönen Tag noch!" ausgibt. Rufe die Funktion danach auf.


def begruesse_tag():
    print("Schönen Tag noch!") 

begruesse_tag()

"""Aufgabe 2: Ein Parameter, ein Rückgabewert

Schreibe eine Funktion verdopple(zahl), die eine Zahl als Parameter entgegennimmt und das Doppelte dieser Zahl zurückgibt (nicht ausgibt!). Speichere das Ergebnis für verdopple(7) in einer Variable und gib es dann mit print() aus.
"""

def verdopple(zahl):
    summe=zahl*2
    return summe

ergebnis=verdopple(7)

print(ergebnis)

"""
Aufgabe 3: Mehrere Parameter mit Bedingung
Schreibe eine Funktion ist_volljaehrig(alter), die prüft, ob eine Person mit dem übergebenen Alter volljährig ist (18 Jahre oder älter). 
Die Funktion soll True oder False zurückgeben (Tipp: du brauchst dafür ein if/else). Teste sie mit mindestens zwei verschiedenen Altersangaben.
"""

def ist_volljaehrig(alter):
    if alter >= 18:
        return True
    else:
        return False

pruefung=ist_volljaehrig(19)

print(pruefung)

"""
Schreibe eine Funktion berechne_rabattpreis(preis, rabatt=10), die einen Preis entgegennimmt und den Preis abzüglich eines Rabatts in Prozent 
zurückgibt. Der Rabatt soll standardmäßig 10 % betragen, falls beim Aufruf keiner angegeben wird.

Teste einmal berechne_rabattpreis(100) (soll 90 ergeben)
Teste einmal berechne_rabattpreis(100, 25) (soll 75 ergeben)
"""

def berechne_rabattpreis(preis, rabatt=10):
    berechnung=preis - (preis / 100 * rabatt)
    return berechnung

ausgabe=berechne_rabattpreis(100,25)
print(ausgabe)

"""
Aufgabe 5: Mehrere Funktionen kombinieren

Schreibe zwei Funktionen:

ist_gerade(zahl) — gibt True zurück, wenn die Zahl gerade ist, sonst False
summe_gerader_zahlen(liste) — nimmt eine Liste von Zahlen entgegen und gibt die Summe aller geraden Zahlen in der Liste zurück. Nutze dabei ist_gerade() innerhalb dieser Funktion.

Teste mit: summe_gerader_zahlen([1, 2, 3, 4, 5, 6]) (Ergebnis sollte 12 sein: 2+4+6)
"""
zahlenListe=[1, 2, 3, 4, 5, 6, 7, 8, 9]

def ist_gerade(zahl):
    return zahl %2 == 0
    

def summe_gerader_zahlen(zahlenListe):
    summe = 0
    for zahl in zahlenListe:
        if ist_gerade(zahl):
            summe = summe + zahl
    return summe
                 
            
print (summe_gerader_zahlen(zahlenListe))    

"""
Praxisaufgabe: Warenkorb-Rechner

Stell dir vor, du entwickelst für einen kleinen Onlineshop eine Funktion zur Berechnung des Gesamtpreises im Warenkorb.

Schreibe eine Funktion berechne_gesamtpreis(preise, versandkosten=4.99, mindestbestellwert=50), die folgendes tut:

preise ist eine Liste mit den Einzelpreisen aller Artikel im Warenkorb (z. B. [19.99, 5.50, 12.00])
Berechne die Summe aller Artikelpreise
Wenn die Summe der Artikelpreise den mindestbestellwert erreicht oder überschreitet, entfallen die Versandkosten (Versand ist dann kostenlos)
Andernfalls werden die versandkosten zur Summe addiert
Die Funktion gibt den Gesamtpreis zurück

Teste die Funktion mit:

berechne_gesamtpreis([19.99, 5.50, 12.00]) → sollte Versandkosten enthalten, da unter 50 €
berechne_gesamtpreis([29.99, 25.00]) → sollte keine Versandkosten enthalten, da über 50 €
"""
  
def berechne_gesamtpreis(preise, versandkosten=4.99, mindestbestellwert=50):
    summe_artikel = 0
    for artikel in preise:
        summe_artikel = summe_artikel + artikel
    

    if summe_artikel<mindestbestellwert:
        gesamtpreis = summe_artikel + versandkosten
        return gesamtpreis
    else:
        return summe_artikel

print (berechne_gesamtpreis([19.99,5.5,12.00]))
print (berechne_gesamtpreis([29.99,25.00]))

"""
Übung 1: Notendurchschnitt-Rechner

Ein Lehrer möchte für eine Liste von Schülernoten den Durchschnitt berechnen und direkt wissen, ob die Klasse im Schnitt "bestanden" hat.

Schreibe eine Funktion berechne_notendurchschnitt(noten, bestehensgrenze=4.0):

noten ist eine Liste mit Zahlen (z. B. Schulnoten, wo niedrigere Zahlen besser sind, wie in Deutschland üblich: 1 = sehr gut, 6 = ungenügend)
Berechne die Summe aller Noten (Sammelvariable + for-Schleife)
Berechne daraus den Durchschnitt (Tipp: Summe geteilt durch die Anzahl der Noten — für die Anzahl gibt es die eingebaute Funktion len(noten), die dir sagt, wie viele Elemente in der Liste sind)
Prüfe mit if/else, ob der Durchschnitt kleiner oder gleich der bestehensgrenze ist
Die Funktion soll den Durchschnitt zurückgeben (nicht ausgeben!)

Teste mit:

berechne_notendurchschnitt([2, 3, 1, 4, 2])
Gib das Ergebnis danach separat mit print() aus
"""

noten=[2 ,3 ,5 ,4 ,2, 5, 6, 6, 5, 4, 4 ]

def berechne_notendurchschnitt(noten, bestehensgrenze=4.0):
    notensumme = 0
    for einzelnote in noten:
        notensumme = notensumme + einzelnote

    if (notensumme/ len(noten))< bestehensgrenze:
        durchschnitt_bestanden = notensumme/ len(noten)
        return durchschnitt_bestanden 

    else:
        durchschnitt_nicht_bestanden = notensumme/ len(noten)
        return durchschnitt_nicht_bestanden

print(berechne_notendurchschnitt(noten))

"""
Übung 2: Tankstellen-Kostenrechner

Ein kleines Programm für eine Spedition soll die Gesamtkosten mehrerer Tankfüllungen berechnen — mit einem Mengenrabatt ab einer bestimmten 
Gesamtmenge.

Schreibe eine Funktion berechne_tankkosten(liter_pro_tankfuellung, preis_pro_liter=1.75, rabattgrenze=200):

liter_pro_tankfuellung ist eine Liste (z. B. [45, 60, 55, 50] — Liter pro einzelner Tankfüllung)
Summiere alle Liter-Angaben zur Gesamtmenge
Berechne die Grundkosten: Gesamtmenge × preis_pro_liter
Wenn die Gesamtmenge die rabattgrenze erreicht oder überschreitet, gibt es 5 % Rabatt auf die Grundkosten 
(denk an die Rabatt-Berechnung aus Aufgabe 4 von vorhin!)
Gib die finalen Kosten zurück
"""

"""liter_pro_tankfuellung = [45, 60, 55, 50]   
preis_pro_liter = 1.75
rabattgrenze = 200

def berechne_tankkosten(liter_pro_tankfuellung, preis_pro_liter, rabattgrenze):

"""

#hier hatte ich Claude gefragt ob es einen Unterschied macht wenn ich die Standardwerte aus dem Funktionskopf in separate Variablen setze. 
# Ja macht es, denn die Standardwerte "variable=Standardwert" werden somit zu Pflichtparametern die zwingend aufgerufen werden müssen, da ansonsten die Funktion nicht mehr durchläuft.

#korrigiert muss es also besser lauten (das andere ist nicht gänzlich falsch, aber erzeugt ein anderes Szenario)



liter_pro_tankfuellung = [45, 60, 55, 50] # hier kann die Liste in einer separaten Variable stehen bleiben, da es keinen Standardwert geben kann, die Werte müssen irgendwoher kommen und in einer Liste/Tupel gespeichert werden

def berechne_tankkosten(liter_pro_tankfuellung, preis_pro_liter=1.75, rabattgrenze=200, rabatt=5):
    grundmenge = 0

    for tankvorgang in liter_pro_tankfuellung:
        grundmenge = grundmenge + tankvorgang

    grundkosten = grundmenge * preis_pro_liter

    if grundmenge >= rabattgrenze:
        gesamtkosten_rabattiert = grundkosten - (grundkosten / 100 * rabatt) 
        return gesamtkosten_rabattiert

    else: 
        gesamtkosten_ungesenkt = grundkosten
        return gesamtkosten_ungesenkt

print("Die gesamten Kosten abzüglich des Rabattes betragen " + str(berechne_tankkosten(liter_pro_tankfuellung)))


"""
Übung 3: Praxisfall — Gehaltsabrechnung mit Überstunden

Eine kleine Firma berechnet den Monatslohn ihrer Mitarbeiter. Gearbeitet wird an mehreren Tagen im Monat, 
und ab einer bestimmten Gesamtstundenzahl gibt es einen Überstundenzuschlag.

Schreibe eine Funktion berechne_monatslohn(arbeitsstunden_pro_tag, stundenlohn=15.0, normalstunden_monat=160):

arbeitsstunden_pro_tag ist eine Liste mit den geleisteten Stunden pro Arbeitstag (z. B. [8, 7.5, 9, 8, 8.5])
Summiere alle Tagesstunden zur Gesamtstundenzahl im Monat
Wenn die Gesamtstundenzahl die normalstunden_monat überschreitet:
Die ersten normalstunden_monat Stunden werden normal bezahlt (Stunden × stundenlohn)
Alle Stunden darüber hinaus (die Überstunden) werden mit einem 25 % höheren Stundenlohn bezahlt
Tipp: Überstunden = Gesamtstunden − normalstunden_monat
Wenn die Gesamtstundenzahl die normalstunden_monat nicht überschreitet, wird einfach alles normal bezahlt (Gesamtstunden × stundenlohn)
Gib den finalen Lohn zurück

Teste mit:

berechne_monatslohn([8, 7.5, 9, 8, 8.5]) (vermutlich unter 160 Std. bei einer Woche — probier auch eine Liste mit mehr Tagen/Stunden, #
um den Überstundenfall zu testen)
"""

arbeitsstunden_pro_tag = [8,7.5,9,10,8,9,7,9,8,8,8,9,8.5,7.9,8,9,9,12,6,8,9,7,8,8,9,8,8,9,8,7]

def berechne_monatslohn(arbeitsstunden_pro_tag, stundenlohn=15.00, normalstunden_monat=160, aufschlag_mehrarbeit=25):
    gesamtstunden_monat = 0
    for tagesstunden in arbeitsstunden_pro_tag:
        gesamtstunden_monat = gesamtstunden_monat + tagesstunden

    anteil_ueberstunden = gesamtstunden_monat - normalstunden_monat

    if anteil_ueberstunden> 0:
        gesamt_lohn = normalstunden_monat * stundenlohn + ((anteil_ueberstunden * stundenlohn) / 100 * aufschlag_mehrarbeit + (anteil_ueberstunden * stundenlohn))
        return gesamt_lohn
    else:
        gesamt_lohn = gesamtstunden_monat * stundenlohn
        return gesamt_lohn

print(berechne_monatslohn(arbeitsstunden_pro_tag))


    