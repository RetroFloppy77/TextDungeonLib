#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

# Espone le funzioni principali all'esterno per un'importazione pulita
from .state import inizializza_gioco
from .world import crea_stanza
from .core import avvia_ciclo_gioco
