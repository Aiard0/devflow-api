from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routes import example

app = FastAPI(title="DevFlow API")


@app.get("/", response_class=HTMLResponse)
def read_root():
    html = (Path(__file__).parent / "static" / "index.html").read_text()
    return HTMLResponse(content=html)

@app.get("/health")
def health_check():
    return {"status": "ok"}

# incluir futuras rotas
app.include_router(example.router)
