#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

"""
Esempio pratico di un'avventura testuale completa costruita con TextDungeonLib.
"""

from textdungeonlib import state
from textdungeonlib import world
from textdungeonlib import core

def aziona_lanterna():
    """Callback personalizzato per l'uso della lanterna."""
    lanterna = state.oggetti["lanterna"]
    if lanterna["stato"].get("accesa", False):
        lanterna["stato"]["accesa"] = False
        lanterna["descrizione"] = "Una lanterna di ottone spenta."
        print("Hai spento la lanterna. Un'ombra fredda ti avvolge.")
    else:
        lanterna["stato"]["accesa"] = True
        lanterna["descrizione"] = "Una lanterna di ottone che emette una calda luce dorata."
        print("Hai acceso la lanterna. Una brillante luce dorata illumina l'area!")

def aziona_chiave():
    """Callback personalizzato per sbloccare il cancello con la chiave."""
    if state.stanza_corrente == "giardino":
        print("Inserisci la pesante chiave di ferro nella serratura del cancello...")
        print("Con un cigolio metallico, il cancello si apre verso NORD rivelando un passaggio segreto!")
        world.connetti_stanze("giardino", "nord", "tempio", bidirezionale=True)
    else:
        print("Non c'è nulla da sbloccare con la chiave in questa stanza.")

def aziona_trofeo():
    """Callback personalizzato quando si prende il trofeo."""
    print("Nel momento in cui sollevi il trofeo d'oro, senti un click risuonare nel tempio!")
    state.punteggio += 100
    print(f"*** HAI VINTO LA PARTITA! Punteggio finale: {state.punteggio} punti. ***")
    state.gioco_in_corso = False

def costruisci_mondo():
    """Inizializza le stanze, gli oggetti e le connessioni del gioco."""
    state.inizializza_stato()
    
    world.crea_stanza(
        "atrio",
        "Atrio della Casa Bianca",
        "Ti trovi in una stanza spoglia con pareti di legno chiaro. C'è una porta aperta ad EST."
    )
    world.crea_stanza(
        "giardino",
        "Giardino Recintato",
        "Un lussureggiante giardino circondato da alte mura. A OVEST torni all'atrio. A NORD c'è un cancello d'acciaio chiuso a chiave."
    )
    world.crea_stanza(
        "tempio",
        "Tempio Sotterraneo",
        "Un antico tempio sotterraneo illuminato da strane rune blu. Al centro c'è un altare in marmo."
    )
    
    world.connetti_stanze("atrio", "est", "giardino")
    
    world.crea_oggetto("lanterna", "una lanterna di ottone", "Una classica lanterna a olio in ottone.")
    world.crea_oggetto("chiave", "una chiave di ferro", "Una chiave di ferro massiccio, vecchia e arrugginita.")
    world.crea_oggetto("trofeo", "un trofeo d'oro", "Un favoloso trofeo dorato tempestato di rubini!", prendibile=True)
    
    world.posiziona_oggetto("lanterna", "atrio")
    world.posiziona_oggetto("chiave", "giardino")
    world.posiziona_oggetto("trofeo", "tempio")
    
    world.registra_azione("lanterna", "usa", aziona_lanterna)
    world.registra_azione("chiave", "usa", aziona_chiave)
    world.registra_azione("trofeo", "prendi", aziona_trofeo)
    
    world.imposta_stanza_iniziale("atrio")

if __name__ == "__main__":
    costruisci_mondo()
    core.avvia_gioco()
