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

from . import state

def mostra_descrizione_stanza():
    """Stampa a schermo la descrizione della stanza corrente e gli oggetti visibili."""
    stanza = state.stanze.get(state.stanza_corrente)
    if not stanza:
        print("Ti trovi nel nulla assoluto...")
        return
    
    print(f"\n=== {stanza['titolo']} ===")
    print(stanza["descrizione"])
    
    oggetti_visibili = []
    for id_obj in stanza["oggetti"]:
        obj = state.oggetti.get(id_obj)
        if obj and obj["visibile"]:
            oggetti_visibili.append(obj["nome"])
    
    if oggetti_visibili:
        print("\nQui puoi vedere:")
        for nome_obj in oggetti_visibili:
            print(f" - {nome_obj}")
            
    uscite = list(stanza["uscite"].keys())
    if uscite:
        print(f"\nUscite disponibili: {', '.join(uscite)}")
    else:
        print("\nNon sembrano esserci uscite evidenti.")

def esegui_vai(direzione):
    """Sposta il giocatore in una stanza adiacente."""
    stanza = state.stanze.get(state.stanza_corrente)
    if not direzione:
        print("In quale direzione vuoi andare?")
        return
    
    chiave_azione = (state.stanza_corrente, f"vai_{direzione}")
    if chiave_azione in state.mappa_azioni:
        esito = state.mappa_azioni[chiave_azione]()
        if esito is False:
            return

    if direzione in stanza["uscite"]:
        state.stanza_corrente = stanza["uscite"][direzione]
        mostra_descrizione_stanza()
    else:
        print(f"Non puoi andare a '{direzione}'.")

def esegui_guarda(bersaglio):
    """Esamina l'ambiente o un oggetto specifico."""
    if not bersaglio:
        mostra_descrizione_stanza()
        return
    
    for id_obj in state.inventario:
        obj = state.oggetti[id_obj]
        if bersaglio in obj["nome"].lower():
            print(obj["descrizione"])
            return
            
    stanza = state.stanze[state.stanza_corrente]
    for id_obj in stanza["oggetti"]:
        obj = state.oggetti[id_obj]
        if obj["visibile"] and bersaglio in obj["nome"].lower():
            print(obj["descrizione"])
            return

    print(f"Non vedi alcun '{bersaglio}' qui intorno.")

def esegui_prendi(nome_oggetto):
    """Raccoglie un oggetto dalla stanza e lo aggiunge all'inventario."""
    if not nome_oggetto:
        print("Cosa vorresti prendere?")
        return
    
    stanza = state.stanze[state.stanza_corrente]
    for id_obj in stanza["oggetti"]:
        obj = state.oggetti[id_obj]
        if obj["visibile"] and nome_oggetto in obj["nome"].lower():
            if not obj["prendibile"]:
                print(f"Non puoi prendere {obj['nome']}.")
                return
            
            chiave_azione = (id_obj, "prendi")
            if chiave_azione in state.mappa_azioni:
                esito = state.mappa_azioni[chiave_azione]()
                if esito is False:
                    return

            stanza["oggetti"].remove(id_obj)
            state.inventario.append(id_obj)
            print(f"Hai preso: {obj['nome']}.")
            return

    print(f"Non c'è alcun '{nome_oggetto}' che tu possa prendere.")

def esegui_lascia(nome_oggetto):
    """Rimuove un oggetto dall'inventario e lo posiziona nella stanza."""
    if not nome_oggetto:
        print("Cosa vorresti lasciare?")
        return
    
    for id_obj in state.inventario:
        obj = state.oggetti[id_obj]
        if nome_oggetto in obj["nome"].lower():
            state.inventario.remove(id_obj)
            state.stanze[state.stanza_corrente]["oggetti"].append(id_obj)
            print(f"Hai lasciato: {obj['nome']}.")
            return

    print(f"Non possiedi alcun '{nome_oggetto}'.")

def esegui_inventario():
    """Mostra l'elenco degli oggetti nell'inventario."""
    if not state.inventario:
        print("Il tuo inventario è vuoto.")
        return
    
    print("\nStai trasportando:")
    for id_obj in state.inventario:
        obj = state.oggetti[id_obj]
        print(f" - {obj['nome']}")

def esegui_usa(nome_oggetto):
    """Utilizza un oggetto."""
    if not nome_oggetto:
        print("Cosa vuoi usare?")
        return
    
    id_trovato = None
    for id_obj in state.inventario:
        if nome_oggetto in state.oggetti[id_obj]["nome"].lower():
            id_trovato = id_obj
            break
            
    if not id_trovato:
        for id_obj in state.stanze[state.stanza_corrente]["oggetti"]:
            if nome_oggetto in state.oggetti[id_obj]["nome"].lower():
                id_trovato = id_obj
                break

    if not id_trovato:
        print(f"Non hai o non vedi alcun '{nome_oggetto}'.")
        return

    chiave_azione = (id_trovato, "usa")
    if chiave_azione in state.mappa_azioni:
        state.mappa_azioni[chiave_azione]()
    else:
        print(f"Non succede nulla di particolare usando {state.oggetti[id_trovato]['nome']}.")
