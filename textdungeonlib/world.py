#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


import textdungeonlib.state as state

def crea_stanza(id_stanza, descrizione, collegamenti, buia=False, descrizione_buia=None):
    """Crea una stanza gestendo nativamente le meccaniche di oscurità stile Zork."""
    state.stanze[id_stanza] = {
        "descrizione": descrizione,
        "descrizione_buia": descrizione_buia or "È buio pesto. Rischi di cadere in una fossa.",
        "collegamenti": collegamenti,
        "collegamenti_bloccati": {},
        "oggetti": {},
        "contenitori": {},
        "buia": buia
    }

def aggiungi_oggetto(id_stanza, nome, descrizione, prendibile=True, luce=False):
    """Aggiunge un oggetto dettagliato in una stanza."""
    if id_stanza in state.stanze:
        state.stanze[id_stanza]["oggetti"][nome.lower()] = {
            "descrizione": descrizione,
            "prendibile": prendibile,
            "luce": luce
        }

def aggiungi_contenitore(id_stanza, nome, chiuso=True, chiave=None):
    """Crea un contenitore stile baule o sacco nella stanza."""
    if id_stanza in state.stanze:
        state.stanze[id_stanza]["contenitori"][nome.lower()] = {
            "chiuso": chiuso,
            "chiave_richiesta": chiave,
            "contenuto": []
        }

def metti_in_contenitore(id_stanza, nome_contenitore, nome_oggetto, descrizione_oggetto):
    """Inserisce un oggetto dentro un contenitore specifico."""
    stanza = state.stanze[id_stanza]
    if nome_contenitore.lower() in stanza["contenitori"]:
        stanza["contenitori"][nome_contenitore.lower()]["contenuto"].append({
            "nome": nome_oggetto.lower(),
            "descrizione": descrizione_oggetto
        })