from fastapi import FastAPI

app = FastAPI(title="Markethub API")

@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "healthy"}