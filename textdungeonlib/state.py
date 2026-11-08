#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


stanze = {}
inventario = []
stanza_corrente = ""
gioco_attivo = True
punteggio = 0
punteggio_massimo = 100
turni = 0
lampada_accesa = False
mosse_luce_rimaste = 300
CAPACITA_INVENTARIO = 5

def inizializza_gioco(mappa_stanze, stanza_iniziale, punti_max=100):
    """Resetta e configura lo stato globale per una nuova partita."""
    global stanze, stanza_corrente, inventario, gioco_attivo, punteggio, punteggio_massimo, turni, lampada_accesa, mosse_luce_rimaste
    stanze = mappa_stanze
    stanza_corrente = stanza_iniziale
    inventario = []
    gioco_attivo = True
    punteggio = 0
    punteggio_massimo = punti_max
    turni = 0
    lampada_accesa = False
    mosse_luce_rimaste = 300