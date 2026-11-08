#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

"""
Modulo per l'analisi del testo (Parsing) immesso dall'utente.
"""

SINONIMI_DIREZIONI = {
    "n": "nord", "nord": "nord",
    "s": "sud", "sud": "sud",
    "e": "est", "est": "est",
    "o": "ovest", "ovest": "ovest", "w": "ovest",
    "a": "alto", "alto": "alto", "su": "alto",
    "b": "basso", "basso": "basso", "giu": "basso", "giù": "basso",
    "dentro": "dentro", "entra": "dentro",
    "fuori": "fuori", "esci": "fuori"
}

SINONIMI_COMANDI = {
    "guarda": "guarda", "g": "guarda", "esamina": "guarda", "l": "guarda",
    "prendi": "prendi", "raccogli": "prendi", "p": "prendi",
    "lascia": "lascia", "posa": "lascia", "scarta": "lascia",
    "inventario": "inventario", "i": "inventario", "inv": "inventario",
    "usa": "usa", "utilizza": "usa",
    "apri": "apri", "chiudi": "chiudi", "leggi": "leggi",
    "accendi": "accendi", "spegni": "spegni",
    "aiuto": "aiuto", "help": "aiuto",
    "esci": "fine", "quit": "fine", "fine": "fine"
}

def analizza_input(testo):
    """Pulisce e analizza la frase inserita dall'utente. Restituisce (comando, argomento)."""
    parole = testo.strip().lower().split()
    if not parole:
        return ("", "")
    
    prima_parola = parole[0]
    if prima_parola in SINONIMI_DIREZIONI:
        return ("vai", SINONIMI_DIREZIONI[prima_parola])
    
    comando = SINONIMI_COMANDI.get(prima_parola, prima_parola)
    argomento = " ".join(parole[1:]) if len(parole) > 1 else ""
    return (comando, argomento)
