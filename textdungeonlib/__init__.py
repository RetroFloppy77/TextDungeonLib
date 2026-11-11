#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


from .state import inizializza_gioco, stanze
from .world import crea_stanza, aggiungi_oggetto, aggiungi_contenitore, metti_in_contenitore
from .core import avvia_ciclo_gioco