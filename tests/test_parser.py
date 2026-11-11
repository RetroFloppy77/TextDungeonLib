#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


from textdungeonlib.parser import analizza_input

def test_analizza_input_direzioni():
    # Verifica la conversione delle abbreviazioni delle direzioni
    azione, argomento = analizza_input("n")
    assert azione == "vai"
    assert argomento == "nord"

def test_analizza_input_con_articoli():
    # Verifica che il parser filtri correttamente gli articoli e le preposizioni
    azione, argomento = analizza_input("prendi la lanterna")
    assert azione == "prendi"
    assert argomento == "lanterna"

def test_analizza_input_vuoto():
    azione, argomento = analizza_input("")
    assert azione is None
    assert argomento is None