# Chatbot knowledge-based basato su QWEN 2.5-3B per assistenza utenti su piattaforma di beneficenza.

# Ottimizzato con quantizzazione a 4-bit per girare su GPU con poca VRAM (<6GB).

# 

# \### 1. Installare le dipendenze

# 

# ```bash

# cd chatbot

# pip install -r requirements.txt

# ```

# 

# \### 2. Scaricare il modello QWEN (\~3.5GB)

# 

# ```bash

# python model/inference/download\_model.py

# ```

# 

# Il modello verrà scaricato in `C:\\Users\\<username>\\.cache\\huggingface\\hub\\`

# 

# \### 3. Testare il modello

# 

# ```bash

# python model/inference/test\_qwen.py

# ```

# 

# Struttura del Progetto

# 

# ```

# chatbot/

# ├── model/

# │   ├── inference/          # Codice per inferenza

# │   │   ├── qwen\_client.py  # Client QWEN (3B 4-bit)

# │   │   ├── test\_qwen.py    # Test di base

# │   │   └── download\_model.py

# │   └── training/           # Fine-tuning LoRA (futuro)

# ├── data/

# │   ├── kb/                 # Knowledge base del sito

# │   └── datasets/           # Dataset per training

# ├── contracts/              # API contracts

# ├── backend/                # Integrazione backend

# └── requirements.txt

# ```

# 

# 

# 



