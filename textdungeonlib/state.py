#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

# textdungeonlib/state.py

# Lo stato del gioco viene memorizzato in dizionari globali nativi.
# Manteniamo l'approccio procedurale aggiornando direttamente queste strutture.

# Dizionario delle stanze. Struttura prevista:
# "nome_stanza": {
#     "descrizione": "Testo descrittivo...",
#     "collegamenti": {"nord": "altra_stanza", "est": "stanza_chiusa"},
#     "collegamenti_bloccati": {"est": {"chiave_richiesta": "chiave_dorata", "messaggio_blocco": "La porta è serrata a chiave."}},
#     "oggetti": ["spada", "chiave_dorata"]
# }


stanze = {}

# Inventario del giocatore (lista di stringhe con i nomi degli oggetti)
inventario = []

# ID della stanza in cui si trova attualmente il giocatore
stanza_corrente = ""

# Flag per determinare se il gioco è ancora in esecuzione
gioco_attivo = True

def inizializza_gioco(mappa_stanze, stanza_iniziale):
    """Inizializza lo stato globale del mondo di gioco."""
    global stanze, stanza_corrente, inventario, gioco_attivo
    stanze = mappa_stanze
    stanza_corrente = stanza_iniziale
    inventario = []
    gioco_attivo = True