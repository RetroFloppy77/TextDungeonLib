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

# Mappa dei sinonimi e abbreviazioni per uniformare l'input dell'utente
SINONIMI = {
    "n": "nord", "s": "sud", "e": "est", "o": "ovest",
    "vai": "vai", "vai a": "vai", "cammina": "vai",
    "g": "guarda", "esamina": "guarda", "l": "guarda",
    "i": "inventario", "inv": "inventario",
    "raccogli": "prendi", "p": "prendi",
    "posa": "lascia", "scarta": "lascia",
    "utilizza": "usa",
    "help": "aiuto",
    "quit": "esci", "fine": "esci"
}

def analizza_input(stringa_input):
    """Pulisce l'input e lo divide in (azione, argomento)."""
    # Rimuove spazi extra e converte in minuscolo
    parole = stringa_input.strip().lower().split()
    
    if not parole:
        return None, None
        
    prima_parola = parole[0]
    
    # Controlla se la prima parola è un comando diretto o un sinonimo
    azione = SINONIMI.get(prima_parola, prima_parola)
    
    # Se l'azione è direttamente una direzione (es: "nord"), la trasformiamo in "vai nord"
    if azione in ["nord", "sud", "est", "ovest"]:
        return "vai", azione
        
    # Ricostruisce l'argomento se composto da più parole (es: "chiave dorata")
    argomento = " ".join(parole[1:]) if len(parole) > 1 else None
    
    return azione, argomento
