from fastapi import FastAPI
app = FastAPI()

@app.get("/tambah")
def tambah(a: int, b: int):
    return {"hasil": a + b}
