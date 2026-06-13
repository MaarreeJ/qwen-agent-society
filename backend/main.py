from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from api.memory_routes import router as memory_router

app = FastAPI(
    title="Qwen Agent Society",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(memory_router)

@app.get("/")
def root():
    return {
        "message": "Qwen Agent Society Running"
    }
    
    