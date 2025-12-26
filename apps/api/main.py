from fastapi import FastAPI

app = FastAPI(title="SecureCloud Lab API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return [{"id": 1, "name": "demo"}]