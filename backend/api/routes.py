from fastapi import APIRouter
from agents.supervisor import supervisor_agent

router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


@router.get("/agent")
def run_agent(query: str):

    result = supervisor_agent(query)

    return {
        "query": query,
        "response": result
    }