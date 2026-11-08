#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


import textdungeonlib.state as state
import textdungeonlib.parser as parser
import textdungeonlib.commands as commands

def avvia_ciclo_gioco():
    """Ciclo principale interattivo dell'avventura."""
    commands.esegui_guarda()
    
    while state.gioco_attivo:
        try:
            if state.lampada_accesa:
                state.mosse_luce_rimaste -= 1
                if state.mosse_luce_rimaste == 10:
                    print("\n[ATTENZIONE: La tua lanterna inizia ad affievolirsi!]")
                elif state.mosse_luce_rimaste <= 0:
                    state.lampada_accesa = False
                    print("\n[La tua lanterna si è spenta completamente. Le batterie sono scariche!]")

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
            elif azione == "accendi":
                commands.esegui_accendi(argomento)
            elif azione == "apri":
                commands.esegui_apri(argomento)
            elif azione == "inventario":
                commands.esegui_inventario()
            elif azione == "punteggio":
                commands.esegui_punteggio()
            elif azione == "aiuto":
                commands.mostra_aiuto()
            elif azione == "esci":
                print("Hai abbandonato l'esplorazione.")
                state.gioco_attivo = False
            else:
                print("Non capisco questo comando. Digita 'aiuto'.")
                
        except (KeyboardInterrupt, EOFError):
            print("\nSessione chiusa.")
            state.gioco_attivo = False