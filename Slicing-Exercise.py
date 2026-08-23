# Übungen zum String slicing

# extrahiere "Welt" aus dem foglenden String
#welcome = 'Hallo Welt!!!'
#print(welcome[6:10])

#Gegeben ist der String wort = "Programmierung". Gib die ersten 5 Zeichen aus.
#wort = 'Programmierung'
#print(wort[:5])

#Gegeben ist derselbe String wort = "Programmierung". Gib die letzten 4 Zeichen aus – ohne die Länge des Strings manuell zu zählen (Tipp: negative Indizes)
#x = 'Programmierung'
#print(x[-4:])

#Gegeben ist stadt = "Rostock". Gib mit Hilfe von negativen Indizes die letzten 3 Zeichen aus
#stadt = "Rostock" 
#print(stadt[-3:])

#Gegeben ist satz = "Der Hund läuft schnell". Extrahiere nur das Wort "Hund" mithilfe von Slicing (du darfst die Start- und End-Position selbst abzählen).
#satz = "Der Hund läuft schnell" 
#print(satz[4:8])

#Gegeben ist text = "Katze". Kehre den String mithilfe von Slicing um, sodass "eztaK" ausgegeben wird (Tipp: Schrittweite/Step-Parameter)
#text = "Katze"
#print (text[::-1])

#   !!!    string[start:stop:step] ist die Volle Slicing Syntax    !!!

#Gegeben ist alphabet = "abcdefghij". Gib mithilfe von Slicing nur jeden zweiten Buchstaben aus, beginnend bei "a" (also "acegi").
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#print(alphabet[::2])

#   !!!     len() = Längenzählfunktion

log_eintrag =  "2026-08-21 14:32:07 ERROR Datenbankverbindung fehlgeschlagen"

print("Die Gesamtlänge des Logs beträgt ", len(log_eintrag), " Zeichen")

# hier wird manuell über "index" die Postion des Leerzeichens bestimmt.
#position = log_eintrag.index (" ")
#print(position)
#position_zwei = log_eintrag.index (" ", position + 1)
#print(position_zwei)
#position_drei = log_eintrag.index (" ", position_zwei + 1)
#print(position_drei)
#position_vier = log_eintrag.index (" ", position_drei + 1)
#print(position_vier)

#Diese Funktion teilt das Log auf und benennt die Komponenten über die vorher ermittelten Positionen der Leerzeichen
#def log_parsen(log_eintrag):
 #   datum = log_eintrag[0:position]
 #   uhrzeit = log_eintrag[position+1:position_zwei]
 #   status = log_eintrag[position_zwei+1:position_drei]
 #   meldung = log_eintrag[position_drei+1::]
 #   return(datum, uhrzeit, status, meldung)

#print(log_parsen(log_eintrag))


for index, zeichen in enumerate(log_eintrag):
    print(index, zeichen)

#Erklärung zu enumerate (Aufzählung)
"""
Syntax
enumerate(iterable, start)

Parameter Values

Parameter	    Description
iterable	    An iterable object
start	        A Number. Defining the start number of the enumerate object. Default 0 
"""