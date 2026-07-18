# 🤖 Chatbot QWEN per Map4Aid

Chatbot knowledge-based basato su QWEN 2.5-3B per assistenza utenti su piattaforma di beneficenza.
Ottimizzato con quantizzazione a 4-bit per girare su GPU con poca VRAM (<6GB).

## 🚀 Setup Iniziale

### 1. Installare le dipendenze

```bash
cd chatbot
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

## 🏋️ Addestramento (Fine-tuning)

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

## 📁 Struttura del Progetto

```
chatbot/
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