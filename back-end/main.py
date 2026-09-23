from fastapi import FastAPI

app = FastAPI(title="Conversor de Criptomoedas API")
@app.get("/")
def home():
    return {"mensagem": "API do conversor de Criptomoedas rodando perfeitamente!"}
