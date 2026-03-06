from fastapi import FastAPI
from app.routes import example

app = FastAPI(title="DevFlow API")

# endpoints existentes
@app.get("/")
def read_root():
    return {"message": "DevFlow API is running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# incluir futuras rotas
app.include_router(example.router)
