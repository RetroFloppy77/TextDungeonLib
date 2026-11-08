#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


import textdungeonlib as tdl

# 1. Creiamo le stanze (Superficie luminosa e caverne buie)
tdl.crea_stanza(
    id_stanza="superficie",
    descrizione="Ti trovi davanti a una piccola baracca di mattoni in una valle isolata. Una grata a terra conduce a sud.",
    collegamenti={"sud": "caverna_buia"}
)

tdl.crea_stanza(
    id_stanza="caverna_buia",
    descrizione="Sei entrato nel reticolo sotterraneo. Le pareti trasudano acqua. C'è un passaggio a est.",
    collegamenti={"nord": "superficie", "est": "stanza_del_tesoro"},
    buia=True,
    descrizione_buia="È buio pesto. Senti strani squittii ed echi sinistri. Muoversi alla cieca è pericoloso."
)

tdl.crea_stanza(
    id_stanza="stanza_del_tesoro",
    descrizione="Una magnifica volta sotterranea scintillante! La via d'uscita è a ovest.",
    collegamenti={"ovest": "caverna_buia"},
    buia=True
)

# 2. Posizioniamo gli oggetti e i contenitori classici
tdl.aggiungi_oggetto("superficie", "lanterna", "Una solida lanterna d'ottone vecchio stile.", prendibile=True, luce=True)
tdl.aggiungi_oggetto("superficie", "chiave", "Una piccola chiave d'acciaio arrugginita.", prendibile=True)

tdl.aggiungi_contenitore("stanza_del_tesoro", "forziere", chiuso=True, chiave="chiave")
tdl.metti_in_contenitore("stanza_del_tesoro", "forziere", "monete", "Un sacchetto pieno di doblò d'oro zecchino!")

# 3. Setup e Inizio Avventura
tdl.inizializza_gioco(tdl.stanze, "superficie", punti_max=100)

print("COLOSSAL CAVE TEXT DUNGEON")
print("==========================")
tdl.avvia_ciclo_gioco()