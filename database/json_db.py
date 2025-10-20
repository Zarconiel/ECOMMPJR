import json
import os
from datetime import datetime
from typing import Dict, Any


#salvar informaçoes sem permanencia de dados
DB_FILE = "data.json"

def load_db() -> Dict[str, dict]:
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def _serialize_for_json(obj: Any):
    if isinstance(obj, dict):
        return {k: _serialize_for_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_serialize_for_json(i) for i in obj]
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj

def save_db(db: Dict[str, dict]):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(_serialize_for_json(db), f, indent=4, ensure_ascii=False)

# Carrega o "banco" em memória
db: Dict[str, dict] = load_db()
