#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


import textdungeonlib.state as state

def crea_stanza(id_stanza, descrizione, collegamenti, oggetti=None, collegamenti_bloccati=None):
    """Aggiunge una stanza allo stato del mondo in modo pulito."""
    if oggetti is None:
        oggetti = []
    if collegamenti_bloccati is None:
        collegamenti_bloccati = {}
        
    state.stanze[id_stanza] = {
        "descrizione": descrizione,
        "collegamenti": collegamenti,
        "collegamenti_bloccati": collegamenti_bloccati,
        "oggetti": oggetti
    }
