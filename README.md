# 🏰 TextDungeonLib

Libreria leggera e modulare in **Python 3.12.x** per lo sviluppo di avventure testuali interattive ispirate ai classici come **Zork**.

Progettata interamente seguendo il **paradigma di programmazione procedurale** (senza programmazione ad oggetti), con codice commentato in italiano e strutturato come pacchetto importabile (`textdungeonlib`).

---

## 📂 Struttura del Progetto

```text
TextDungeonLib/
│
├── 📜 main.py                  # Esempio di gioco completo pronto all'uso
├── 📖 README.md                # Guida completa e documentazione
└── 📁 textdungeonlib/          # Pacchetto principale della libreria
    ├── 📄 __init__.py          # Inizializzatore del pacchetto
    ├── 📄 state.py             # Stato globale del gioco (stanze, inventario)
    ├── 📄 world.py             # Funzioni per la creazione di stanze e oggetti
    ├── 📄 parser.py            # Analizzatore sintattico del testo utente
    ├── 📄 commands.py          # Esecutore procedurale delle azioni (vai, prendi, usa)
    └── 📄 core.py              # Ciclo di gioco principale (Game Loop)
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
