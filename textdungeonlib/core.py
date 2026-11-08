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

import textdungeonlib.state as state
import textdungeonlib.parser as parser
import textdungeonlib.commands as commands

def avvia_ciclo_gioco():
    """Gestisce il ciclo principale di input/output (Game Loop)."""
    # Mostra la descrizione della stanza iniziale all'avvio
    commands.esegui_guarda()
    
    while state.gioco_actvo:
        try:
            stringa_utente = input("\n> ")
            azione, argomento = parser.analizza_input(stringa_utente)
            
            if not azione:
                continue
                
            if azione == "vai":
                commands.esegui_vai(argomento)
            elif azione == "guarda":
                commands.esegui_guarda(argomento)
            elif azione == "prendi":
                commands.esegui_prendi(argomento)
            elif azione == "lascia":
                commands.esegui_lascia(argomento)
            elif azione == "inventario":
                commands.esegui_inventario()
            elif azione == "usa":
                commands.esegui_usa(argomento)
            elif azione == "aiuto":
                commands.mostra_aiuto()
            elif azione == "esci":
                print("Grazie per aver giocato!")
                state.gioco_attivo = False
            else:
                print("Comando non riconosciuto. Scrivi 'aiuto' per i comandi.")
                
        except (KeyboardInterrupt, EOFError):
            print("\nPartita interrotta. Alla prossima!")
            state.gioco_attivo = False
            