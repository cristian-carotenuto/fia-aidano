# Aidano - Assistente Intelligente per Map4Aid

Aidano è un assistente virtuale knowledge-based sviluppato nell'ambito del progetto **Map4Aid**.

Il chatbot è stato progettato per assistere gli utenti della piattaforma fornendo risposte rapide, coerenti e contestualizzate riguardo ai servizi offerti da Map4Aid. Il sistema utilizza il modello **Qwen 2.5-3B**, specializzato mediante fine-tuning e integrato all'interno del backend dell'applicazione.

Questo repository raccoglie tutti i componenti sviluppati per Aidano, inclusi il codice sorgente, gli script di addestramento, il dataset, gli strumenti di inferenza e gli elementi necessari per replicare il chatbot.

---

# Obiettivi del progetto

Il progetto è stato sviluppato con i seguenti obiettivi:

- fornire un sistema di assistenza automatica agli utenti di Map4Aid;
- riconoscere correttamente le richieste formulate dagli utenti;
- restituire risposte coerenti con le informazioni presenti sulla piattaforma;
- garantire tempi di risposta ridotti;

---

# Caratteristiche principali

- Modello linguistico **Qwen 2.5-3B**.
- Fine-tuning tramite tecnica **LoRA**.
- Classificazione degli intent dell'utente.
- Risposte controllate e coerenti con la base di conoscenza del progetto.
- Ottimizzazione a 4-bit per GPU con meno di 6 GB di VRAM.

---

# Architettura del sistema

Il sistema è composto dai seguenti componenti principali:

```
       Utente
         │
  Frontend Map4Aid
         │
  Backend FastAPI
         │
Aidano (Qwen 2.5-3B)
         │
  Intent → Risposta
```

---

# Struttura del progetto

## Setup Iniziale per replicare il progetto

### 1. Installare le dipendenze all'interno della cartella principale

```bash
cd fia-aidano
pip install -r requirements.txt
```

### 2. Scaricare il modello QWEN (~3.5GB)

```bash
python model/inference/download_model.py
```

Il modello verrà scaricato in `C:\Users\<username>\.cache\huggingface\hub\`

### 3. Testare il modello

Esistono due modalità di test:
- **Base (Tempo/Memoria)**: 
  ```bash
  python model/inference/test_qwen_basic.py
  ```
- **Specialistico (Fine-tuning)**:
  ```bash
  python model/inference/test_qwen_tuning.py
  ```

## Addestramento (Fine-tuning)

Se si desidera specializzare il modello sui dati di progetto:

### 1. Installare le dipendenze di training

```bash
pip install -r model/training/requirements-train.txt
```

### 2. Dataset di addestramento

Il dataset esteso utilizzato per il fine-tuning è già incluso nel repository e non deve essere generato manualmente.

### 3. Avviare il fine-tuning

Il fine-tuning viene eseguito in **quattro sessioni consecutive da 25 step**, per un totale di **100 step**.

Per ogni sessione eseguire:

```bash
python model/training/fine_tune.py
```

Al termine di ogni esecuzione verrà salvato automaticamente un checkpoint nella cartella:

```text
model/training/qwen-aidano-checkpoints
```

Lo script riprenderà automaticamente l'addestramento dall'ultimo checkpoint disponibile. Dopo la quarta esecuzione il modello avrà completato i 100 step previsti.

## Test del modello fine-tuned

Una volta completato il fine-tuning è possibile verificare il corretto funzionamento di Aidano eseguendo:

```bash
python model/inference/test_aidano_ft.py
```

Lo script carica il modello fine-tuned e permette di interagire direttamente con Aidano per verificarne il comportamento.

## Struttura delle Cartelle

```text
fia-aidano/
├── backend/
│   └── qwen_service.py          # Servizio FastAPI per l'integrazione di Aidano
│
├── contracts/                   
│
├── data/
│   ├── training_data.jsonl          # Dataset originale
│   ├── training_data_expanded.jsonl # Dataset esteso per il fine-tuning
│   └── dataset_generator.py         # Script per generare il dataset esteso
│
├── model/
│   ├── inference/
│   │   ├── download_model.py        # Download automatico del modello Qwen
│   │   ├── qwen_client.py           # Client per l'inferenza
│   │   ├── test_qwen.py             # Test generici del modello
│   │   ├── test_qwen_basic.py       # Test prestazionale del modello base
│   │   ├── test_qwen_tuning.py      # Test del modello durante il fine-tuning
│   │   ├── test_aidano_ft.py        # Test del modello fine-tuned
│   │   └── test_static_responses.py # Verifica delle risposte statiche
│   │
│   └── training/
│       ├── fine_tune.py             # Script di fine-tuning
│       ├── tune_reset.py            # Ripristino dell'ambiente di training
│       └── requirements-train.txt   # Dipendenze per l'addestramento
│
├── requirements.txt                 # Dipendenze principali
├── README.md
└── .gitignore
```

# Team

Progetto sviluppato per il corso di **Fondamenti di Intelligenza Artificiale**.

**Componenti del team**

- Luciano Corvino 0512120518
- Cristian Carotenuto 0512119840

---

# Repository

Il repository contiene:

- il codice sorgente del chatbot;
- gli script di inferenza;
- gli script di addestramento;
- il dataset utilizzato per il fine-tuning;
- il backend di integrazione con Map4Aid;
- la documentazione del progetto.

---
