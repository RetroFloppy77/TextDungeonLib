#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

"""
Modulo di gestione dello stato del gioco.
Mantiene tutte le variabili globali del mondo di gioco, dell'inventario e del giocatore.
"""

stanze = {}
oggetti = {}
inventario = []
stanza_corrente = None
gioco_in_corso = True
punteggio = 0
punteggio_massimo = 0
mappa_azioni = {}

def inizializza_stato():
    """Ripristina lo stato globale del gioco."""
    global stanze, oggetti, inventario, stanza_corrente, gioco_in_corso, punteggio, punteggio_massimo, mappa_azioni
    stanze = {}
    oggetti = {}
    inventario = []
    stanza_corrente = None
    gioco_in_corso = True
    punteggio = 0
    punteggio_massimo = 0
    mappa_azioni = {}
