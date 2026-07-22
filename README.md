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

### 2. Generare il dataset espanso
```bash
python data/dataset_generator.py
```

### 3. Avviare il fine-tuning
```bash
python model/training/fine_tune.py
```
*I risultati (adapter LoRA) verranno salvati nella cartella `model/training/qwen-aidano-checkpoints`.*

## Struttura delle Cartelle

```text
fia-aidano/
├── model/
│   ├── inference/          # Codice per inferenza
│   │   ├── qwen_client.py  # Client QWEN (3B 4-bit)
│   │   ├── test_qwen.py    # Test di base
│   │   └── download_model.py
│   └── training/           # Fine-tuning LoRA
│       ├── fine_tune.py    # Script di addestramento
│       └── requirements-train.txt
├── data/
│   ├── training_data.jsonl # Dataset base dai documenti
│   └── dataset_generator.py # Script per espandere il dataset
├── contracts/              # API contracts
├── backend/                # Integrazione backend
└── requirements.txt
```

# Team

Progetto sviluppato per il corso di **Fondamenti di Intelligenza Artificiale**.

**Componenti del team**

- Nome Cognome
- Nome Cognome
- Nome Cognome

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
