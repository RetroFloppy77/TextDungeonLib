#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

"""
Modulo di gestione ed esecuzione dei comandi di gioco.
"""

import textdungeonlib.state as state

def esegui_vai(direzione):
    """Sposta il giocatore tra le stanze gestendo eventuali blocchi."""
    if not direzione:
        print("Dove vuoi andare? (es: vai nord)")
        return

    stanza = state.stanze[state.stanza_corrente]
    
    # Verifica se la direzione esiste
    if direzione not in stanza["collegamenti"]:
        print(f"Non puoi andare a {direzione} da qui.")
        return
        
    # Verifica se il passaggio è bloccato da un enigma/oggetto
    if direzione in stanza.get("collegamenti_bloccati", {}):
        blocco = stanza["collegamenti_bloccati"][direzione]
        print(blocco.get("messaggio_blocco", "Il passaggio è bloccato."))
        return
        
    # Cambia stanza
    state.stanza_corrente = stanza["collegamenti"][direzione]
    esegui_guarda()

def esegui_guarda(oggetto=None):
    """Esamina la stanza corrente o un oggetto specifico."""
    stanza = state.stanze[state.stanza_corrente]
    
    if not oggetto:
        # Descrizione dell'ambiente
        print(f"\n--- {state.stanza_corrente.replace('_', ' ').title()} ---")
        print(stanza["descrizione"])
        if stanza["oggetti"]:
            print(f"In questa stanza vedi: {', '.join(stanza['oggetti'])}")
    else:
        # Esame di un oggetto nell'ambiente o nell'inventario
        if oggetto in state.inventario or oggetto in stanza["oggetti"]:
            print(f"Esamini '{oggetto}', ma non noti nulla di insolito.")
        else:
            print(f"Non vedi alcun '{oggetto}' qui.")

def esegui_prendi(oggetto):
    """Raccoglie un oggetto dalla stanza e lo mette nell'inventario."""
    if not oggetto:
        print("Cosa vuoi prendere?")
        return
        
    stanza = state.stanze[state.stanza_corrente]
    if oggetto in stanza["oggetti"]:
        stanza["oggetti"].remove(oggetto)
        state.inventario.append(oggetto)
        print(f"Hai preso: {oggetto}.")
    else:
        print(f"Non c'è nessun '{oggetto}' in questa stanza.")

def esegui_lascia(oggetto):
    """Lascia un oggetto dell'inventario nella stanza corrente."""
    if not oggetto:
        print("Cosa vuoi lasciare?")
        return
        
    if oggetto in state.inventario:
        state.inventario.remove(oggetto)
        state.stanze[state.stanza_corrente]["oggetti"].append(oggetto)
        print(f"Hai lasciato: {oggetto}.")
    else:
        print(f"Non hai '{oggetto}' nel tuo inventario.")

def esegui_inventario():
    """Mostra gli oggetti trasportati dal giocatore."""
    if state.inventario:
        print(f"Nel tuo inventario ci sono: {', '.join(state.inventario)}")
    else:
        print("Il tuo inventario è vuoto.")

def esegui_usa(oggetto):
    """Usa un oggetto per risolvere enigmi o sbloccare passaggi."""
    if not oggetto:
        print("Cosa vuoi usare?")
        return
        
    if oggetto prejudices not in state.inventario:
        print(f"Non possiedi '{oggetto}'.")
        return
        
    stanza = state.stanze[state.stanza_corrente]
    blocco_rimosso = False
    
    # Controlla se l'oggetto sblocca una direzione nella stanza corrente
    direzioni_da_rimuovere = []
    for dir_bloccata, info_blocco in stanza.get("collegamenti_bloccati", {}).items():
        if info_blocco.get("chiave_richiesta") == oggetto:
            print(f"Hai usato {oggetto}! Un passaggio si è aperto verso {dir_bloccata}.")
            direzioni_da_rimuovere.append(dir_bloccata)
            blocco_rimosso = True
            
    for dir_bloccata in direzioni_da_rimuovere:
        del stanza["collegamenti_bloccati"][dir_bloccata]
        
    if not blocco_rimosso:
        print(f"Usi '{oggetto}', ma non succede nulla qui.")

def mostra_aiuto():
    """Mostra la lista dei comandi disponibili."""
    print("\n--- COMANDI DISPONIBILI ---")
    print("vai [direzione]  -> Muoviti (nord, sud, est, ovest / n, s, e, o)")
    print("guarda [oggetto] -> Esamina la stanza o un oggetto specifico")
    print("prendi [oggetto] -> Raccogli un oggetto da terra")
    print("lascia [oggetto] -> Deponi un oggetto nella stanza")
    print("usa [oggetto]    -> Utilizza un oggetto del tuo inventario")
    print("inventario       -> Mostra gli oggetti che stai trasportando")
    print("aiuto            -> Mostra questa guida")
    print("esci             -> Chiudi il gioco")
    