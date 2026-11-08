#!/usr/bin/env python3

"""
Autore: Stefano Peris
Email: stefanoperis.github@gmail.com
Versione: 1.0 (Python 3.12)
Descrizione: Libreria leggera e modulare in Python 3.12.x
per lo sviluppo di avventure testuali interattive ispirate ai classici come Zork.
"""


import textdungeonlib.state as state

def c_e_luce():
    """Verifica se l'ambiente è illuminato (stanza naturale o lanterna accesa)."""
    stanza = state.stanze[state.stanza_corrente]
    if not stanza["buia"]:
        return True
    if state.lampada_accesa and any(obj.get("luce") for obj in state.inventario):
        return True
    return False

def esegui_vai(direzione):
    """Sposta il giocatore. Muoversi al buio può essere fatale!"""
    if not direzione:
        print("Dove vuoi andare?")
        return

    stanza = state.stanze[state.stanza_corrente]

    if not c_e_luce():
        print("Sei inciampato nel buio e sei caduto in una fossa profondissima! Sei morto.")
        state.gioco_attivo = False
        return

    if direzione not in stanza["collegamenti"]:
        print("Non c'è una via d'uscita in quella direzione.")
        return

    state.stanza_corrente = stanza["collegamenti"][direzione]
    state.turni += 1
    esegui_guarda()

def esegui_guarda(argomento=None):
    """Esamina stanze, oggetti o l'interno di contenitori aperti."""
    stanza = state.stanze[state.stanza_corrente]

    if not c_e_luce():
        print(stanza["descrizione_buia"])
        return

    if not argomento:
        print(f"\n[{state.stanza_corrente.replace('_', ' ').title()}]")
        print(stanza["descrizione"])
        for obj in stanza["oggetti"]:
            print(f"C'è un {obj} qui.")
        for cont in stanza["contenitori"]:
            status = "chiuso" if stanza["contenitori"][cont]["chiuso"] else "aperto"
            print(f"Vedi un {cont} ({status}).")
    else:
        arg_lower = argomento.lower()
        if arg_lower in stanza["oggetti"]:
            print(stanza["oggetti"][arg_lower]["descrizione"])
        elif arg_lower in [x["nome"] for x in state.inventario]:
            obj = next(x for x in state.inventario if x["nome"] == arg_lower)
            print(obj["descrizione"])
        else:
            print(f"Non noti nessun {argomento} speciale qui.")

def esegui_prendi(oggetto):
    """Raccoglie un oggetto rispettando la capacità massima dell'inventario."""
    if not oggetto:
        print("Cosa vorresti prendere?")
        return
    if not c_e_luce():
        print("È troppo buio per raccogliere qualcosa.")
        return
    if len(state.inventario) >= state.CAPACITA_INVENTARIO:
        print("Le tue tasche sono piene! Devi lasciare qualcosa.")
        return

    stanza = state.stanze[state.stanza_corrente]
    obj_lower = oggetto.lower()

    if obj_lower in stanza["oggetti"]:
        info = stanza["oggetti"][obj_lower]
        if not info["prendibile"]:
            print("Non puoi prenderlo, è fissato al suolo!")
            return
        
        state.inventario.append({
            "nome": obj_lower,
            "descrizione": info["descrizione"],
            "luce": info["luce"]
        })
        del stanza["oggetti"][obj_lower]
        print("Preso.")
    else:
        print("Non c'è niente del genere qui.")

def esegui_accendi(oggetto):
    """Accende una fonte di luce portatile (es. la lanterna)."""
    if not oggetto:
        print("Cosa vuoi accendere?")
        return
    
    obj_lower = oggetto.lower()
    in_inventario = any(x["nome"] == obj_lower for x in state.inventario)
    
    if in_inventario:
        obj = next(x for x in state.inventario if x["nome"] == obj_lower)
        if obj["luce"]:
            state.lampada_accesa = True
            print("La lanterna adesso emette una luce chiara e stabile.")
            esegui_guarda()
        else:
            print(f"Non puoi accendere un {oggetto}!")
    else:
        print("Non hai questo oggetto con te.")

def esegui_apri(contenitore):
    """Apre bauli o contenitori per rivelare i tesori nascosti."""
    if not contenitore:
        print("Cosa vuoi aprire?")
        return
    
    stanza = state.stanze[state.stanza_corrente]
    c_lower = contenitore.lower()

    if c_lower in stanza["contenitori"]:
        cont = stanza["contenitori"][c_lower]
        if not cont["chiuso"]:
            print("È già aperto.")
            return
        
        if cont["chiave_richiesta"]:
            possiede_chiave = any(x["nome"] == cont["chiave_richiesta"].lower() for x in state.inventario)
            if not possiede_chiave:
                print(f"È chiuso a chiave. Ti serve una {cont['chiave_richiesta']}.")
                return
        
        cont["chiuso"] = False
        print(f"Hai aperto il {c_lower}. Dentro trovi:")
        for item in cont["contenuto"]:
            print(f" - {item['nome']}")
            stanza["oggetti"][item["nome"]] = {"descrizione": item["descrizione"], "prendibile": True, "luce": False}
        cont["contenuto"] = []
    else:
        print("Non c'è nessun contenitore con quel nome qui.")

def esegui_inventario():
    """Mostra l'inventario."""
    if not state.inventario:
        print("Non stai trasportando nulla.")
    else:
        nomi = [x["nome"] for x in state.inventario]
        print(f"Stai trasportando: {', '.join(nomi)} ({len(state.inventario)}/{state.CAPACITA_INVENTARIO})")

def esegui_punteggio():
    """Mostra i progressi e i turni consumati."""
    print(f"Il tuo punteggio è {state.punteggio} su un massimo di {state.punteggio_massimo}, in {state.turni} turni.")

def mostra_aiuto():
    print("\n--- COMANDI CLASSICI ---")
    print("vai [direzione]  -> Muoviti (nord, sud, est, ovest)")
    print("guarda [oggetto] -> Esamina l'ambiente o una cosa specifica")
    print("prendi [oggetto] -> Raccogli un oggetto")
    print("accendi [luce]   -> Accendi la lanterna o la torcia")
    print("apri [baule]     -> Apri un contenitore chiuso")
    print("inventario       -> Mostra cosa porti dietro")
    print("punteggio        -> Visualizza punti e turni")