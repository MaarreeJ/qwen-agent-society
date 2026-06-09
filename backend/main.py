from fastapi import FastAPI

from api.routes import router
from api.memory_routes import router as memory_router


app = FastAPI(
    title="Qwen Agent Society",
    version="1.0.0"
)

app.include_router(router)

app.include_router(memory_router)


@app.get("/")
def root():

    return {
        "message": "Qwen Agent Society Running"
    }