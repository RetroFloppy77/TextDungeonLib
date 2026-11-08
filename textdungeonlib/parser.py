#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


SINONIMI = {
    "n": "nord", "s": "sud", "e": "est", "o": "ovest",
    "accendi": "accendi", "attiva": "accendi",
    "g": "guarda", "esamina": "guarda", "l": "guarda",
    "i": "inventario", "inv": "inventario",
    "raccogli": "prendi", "p": "prendi",
    "apri": "apri", "scassina": "apri",
    "score": "punteggio", "punti": "punteggio",
    "help": "aiuto", "quit": "esci", "fine": "esci"
}

ARTICOLI_E_PREPOSIZIONI = {"il", "lo", "la", "i", "gli", "le", "un", "uno", "una", "del", "della", "di", "con", "a"}

def analizza_input(stringa_input):
    """Pulisce l'input filtrando il rumore grammaticale ed estrae Azione e Argomento."""
    parole = stringa_input.strip().lower().split()
    if not parole:
        return None, None

    parole_filtrate = [p for p in parole if p not in ARTICOLI_E_PREPOSIZIONI]
    if not parole_filtrate:
        return None, None

    prima_parola = parole_filtrate[0]
    azione = SINONIMI.get(prima_parola, prima_parola)

    if azione in ["nord", "sud", "est", "ovest"]:
        return "vai", azione

    argomento = " ".join(parole_filtrate[1:]) if len(parole_filtrate) > 1 else None
    return azione, argomento