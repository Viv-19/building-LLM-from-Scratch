import os
from pathlib import Path

list_of_files = [

    # Core LLM components
    "core/__init__.py",
    "core/attention.py",
    "core/embeddings.py",
    "core/feedforward.py",
    "core/block.py",
    "core/model.py",

    # Data-related components
    "data/__init__.py",
    "data/tokenizer.py",
    "data/dataloader.py",

    # Config, training, generation
    "config.py",
    "train.py",
    "generate.py",

    # Utilities
    "utils.py",

    # Backend API
    "backend/__init__.py",
    "backend/main.py",              # FastAPI app
    "backend/routes.py",            # API endpoints
    "backend/models.py",            # Pydantic models

    # Frontend
    "frontend/__init__.py",
    "frontend/app.py",              # Streamlit/Gradio UI
    "frontend/components.py",       # UI components

    
]

for filepath in list_of_files:
    path = Path(filepath)
    filedir, filename = os.path.split(path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, "w") as f:
            pass
    else:
        print(f"File already exists at: {path}")


