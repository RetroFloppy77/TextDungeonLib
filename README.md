# 🏰 TextDungeonLib

Libreria leggera e modulare in **Python 3.12.x** per lo sviluppo di avventure testuali interattive ispirate ai classici come **Zork**.

Progettata interamente seguendo il **paradigma di programmazione procedurale** (senza programmazione ad oggetti), con codice commentato in italiano e strutturato come pacchetto importabile (`textdungeonlib`).

---

## 📂 Struttura del Progetto

```text
TextDungeonLib/
├── 📁 .github/workflows/           # Automazioni e CI/CD con GitHub Actions.
│   ├── 📄 test.yml                 # Esegue automaticamente i test su Python 3.10-3.13 a ogni push.
│   └── 📄 release.yml              # Pubblica automaticamente la libreria su PyPI alla creazione di un tag (v*)
├── 📁 textdungeonlib/              # Pacchetto principale della libreria procedurale.
│   ├── 📄 __init__.py              # Inizializzatore ed esportatore delle funzioni del pacchetto.
│   ├── 📄 commands.py              # Esecutore procedurale delle azioni di gioco (movimento, comandi, interazioni)
│   ├── 📄 core.py                  # Ciclo principale di gioco (Game Loop) e gestione delle meccaniche di luce.
│   ├── 📄 parser.py                # Analizzatore sintattico per filtrare e pulire l'input testuale dell'utente.
│   ├── 📄 state.py                 # Gestione dello stato globale (stanze, inventario, turni, punteggio)
│   └── 📄 world.py                 # Funzioni per la costruzione del mondo di gioco (stanze, oggetti, contenitori)
├── 📁 tests/                       # Cartella dedicata ai test automatici.
│   └── 📄 test_parser.py           # Test unitari scritti con pytest per validare il parser testuale.
├── 📜 main.py                      # Script di esempio completo per l'avvio e la demo del gioco.
├── 📄 pyproject.toml               # Configurazione di build e metadati del pacchetto Python.
├── 📖 README.md                    # Documentazione ufficiale e guida all'utilizzo della libreria.
└── ⚖️ License                      # Licenza open-source MIT del progetto.
```

---

## 💻 Requisiti di Sistema

- **Python 3.12.x** o superiore (compatibile con Python 3.10+).
- Nessuna dipendenza esterna richiesta.

---

## 🛠️ Guida all'Utilizzo e Importazione

Mantenendo la cartella `textdungeonlib/` nella stessa directory del tuo script di gioco (`main.py`), puoi importare i moduli direttamente con la sintassi richiesta:

```python
import textdungeonlib.state as state
import textdungeonlib.world as world
import textdungeonlib.core as core
```

### 🐧 Linux / macOS
```bash
unzip TextDungeonLib.zip
cd TextDungeonLib
python3 main.py
```

### 🪟 Windows (CMD / PowerShell)
```cmd
python main.py
```

### 📱 Android (Termux)
```bash
pkg install python
python main.py
```

---

## 🕹️ Comandi di Gioco Supportati

| Icona | Comando | Sinonimi / Abbreviazioni | Descrizione |
| :---: | :--- | :--- | :--- |
| 🧭 | `vai [direzione]` | `n`, `s`, `e`, `o`, `nord`, `sud`, `est`, `ovest` | Spostamento tra le stanze. |
| 👁️ | `guarda [oggetto]` | `g`, `esamina`, `l` | Descrizione della stanza o dell'oggetto. |
| 🎒 | `inventario` | `i`, `inv` | Mostra gli oggetti trasportati. |
| 🤲 | `prendi [oggetto]` | `raccogli`, `p` | Raccoglie un oggetto nella stanza. |
| 📦 | `lascia [oggetto]` | `posa`, `scarta` | Lascia un oggetto nell'ambiente. |
| 🔧 | `usa [oggetto]` | `utilizza` | Attiva l'azione speciale di un oggetto. |
| ❓ | `aiuto` | `help` | Mostra la guida in-game. |
| 🚪 | `esci` | `quit`, `fine` | Termina la partita. |

---

## 📝 Licenza
Rilasciato sotto licenza open-source MIT.
