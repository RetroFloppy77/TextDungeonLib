#!/usr/bin/env python3
"""

Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""

"""
Modulo principale del loop di gioco (Game Loop) per TextDungeonLib.
"""

from . import state, parser, commands

def avvia_gioco():
    """Avvia la sessione di gioco."""
    if not state.stanza_corrente:
        print("Errore: Nessuna stanza iniziale impostata.")
        return
    
    print("=" * 60)
    print(" TEXTDUNGEONLIB - Avventura Testuale")
    print(" Scrivi 'aiuto' per l'elenco dei comandi o 'esci' per terminare.")
    print("=" * 60)
    
    commands.mostra_descrizione_stanza()
    
    while state.gioco_in_corso:
        try:
            input_utente = input("\n> ")
            esegui_turno(input_utente)
        except (KeyboardInterrupt, EOFError):
            print("\nPartita interrotta.")
            break

def esegui_turno(input_utente):
    """Gestisce un singolo turno del giocatore."""
    comando, argomento = parser.analizza_input(input_utente)
    
    if not comando:
        return
    
    if comando == "fine":
        print("Grazie per aver giocato! Alla prossima.")
        state.gioco_in_corso = False
    elif comando == "vai":
        commands.esegui_vai(argomento)
    elif comando == "guarda":
        commands.esegui_guarda(argomento)
    elif comando == "prendi":
        commands.esegui_prendi(argomento)
    elif comando == "lascia":
        commands.esegui_lascia(argomento)
    elif comando == "inventario":
        commands.esegui_inventario()
    elif comando == "usa":
        commands.esegui_usa(argomento)
    elif comando == "aiuto":
        mostra_aiuto()
    else:
        print("Non ho capito cosa vuoi fare. Scrivi 'aiuto' per le azioni disponibili.")

def mostra_aiuto():
    """Stampa l'elenco delle istruzioni di base."""
    print("\n--- COMANDI DISPONIBILI ---")
    print(" Movimento:  nord, sud, est, ovest, alto, basso (o n, s, e, o, a, b)")
    print(" Azioni:     guarda [oggetto], prendi [oggetto], lascia [oggetto]")
    print(" Altri:      usa [oggetto], inventario, aiuto, esci")
    print("---------------------------")
