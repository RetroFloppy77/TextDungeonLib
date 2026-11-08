#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

"""
Modulo per la creazione e la manipolazione del mondo di gioco (stanze ed oggetti).
"""

from . import state

def crea_stanza(id_stanza, titolo, descrizione):
    """Crea una nuova stanza e la aggiunge al mondo di gioco."""
    state.stanze[id_stanza] = {
        "titolo": titolo,
        "descrizione": descrizione,
        "uscite": {},
        "oggetti": []
    }

def connetti_stanze(id_origine, direzione, id_destinazione, bidirezionale=True):
    """Collega due stanze tra loro in una direzione specifica."""
    opposti = {
        "nord": "sud", "sud": "nord",
        "est": "ovest", "ovest": "est",
        "alto": "basso", "basso": "alto",
        "dentro": "fuori", "fuori": "dentro"
    }
    
    if id_origine in state.stanze and id_destinazione in state.stanze:
        state.stanze[id_origine]["uscite"][direzione] = id_destinazione
        if bidirezionale and direzione in opposti:
            state.stanze[id_destinazione]["uscite"][opposti[direzione]] = id_origine

def crea_oggetto(id_oggetto, nome, descrizione, prendibile=True, visibile=True):
    """Crea un nuovo oggetto del gioco."""
    state.oggetti[id_oggetto] = {
        "nome": nome,
        "descrizione": descrizione,
        "prendibile": prendibile,
        "visibile": visibile,
        "stato": {}
    }

def posiziona_oggetto(id_oggetto, id_stanza):
    """Mette un oggetto all'interno di una stanza."""
    if id_stanza in state.stanze and id_oggetto in state.oggetti:
        state.stanze[id_stanza]["oggetti"].append(id_oggetto)

def imposta_stanza_iniziale(id_stanza):
    """Imposta la stanza di partenza del giocatore."""
    state.stanza_corrente = id_stanza

def registra_azione(id_entita, azione, funzione_callback):
    """Registra una funzione personalizzata da eseguire quando l'utente usa un'azione."""
    state.mappa_azioni[(id_entita, azione)] = funzione_callback
