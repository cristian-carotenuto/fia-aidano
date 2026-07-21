import sys
import os

# Aggiunge la cartella inference al path per importare QwenClient
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../model/inference"))

from fastapi import FastAPI
from pydantic import BaseModel
from qwen_client import QwenClient

app = FastAPI()

# Carica il modello una sola volta all'avvio (con adapter fine-tuned se disponibile)
client = QwenClient()
client.load_model()

class Req(BaseModel):
    message: str
    history: list[dict] | None = None  # opzionale

@app.post("/chat")
def chat(req: Req):
    # Ripristina la history nel client se fornita dal frontend
    if req.history:
        client.history = [client.history[0]] if client.history else []
        for msg in req.history[-10:]:
            client.history.append(msg)

    # Usa la pipeline completa: intent classification + fallback gate
    reply = client.generate_response_gated(req.message)
    return {"reply": reply}