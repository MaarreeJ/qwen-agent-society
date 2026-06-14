from fastapi import APIRouter

from agents.execution import run_workflow
from memory.retrieval import retrieve_relevant_chunks

router = APIRouter()


@router.get("/agent")
def agent(query: str):

    chunks = retrieve_relevant_chunks(query)

    context = "\n".join(chunks)

    return run_workflow(
        query=query,
        context=context
    )


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }