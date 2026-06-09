from fastapi import APIRouter
from agents.execution import run_workflow

router = APIRouter()


@router.get("/agent")
def agent(query: str):

    return run_workflow(query)


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }