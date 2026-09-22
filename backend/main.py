from fastapi import FastAPI

app = FastAPI(title="AI Customer Recovery")


@app.get("/")
def root():
    return {"message": "AI Customer Recovery API"}