from fastapi import APIRouter, UploadFile, File
import os

from services.pdf_service import extract_pdf_text
from services.chunking_service import chunk_text
from services.embedding_service import create_embedding

from database.qdrant import store_vector

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    text = extract_pdf_text(
        file_path
    )

    chunks = chunk_text(
        text
    )

    for chunk in chunks:

        embedding = create_embedding(
            chunk
        )

        store_vector(
            chunk,
            embedding
        )

    return {
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks),
        "message": "Stored in vector database"
    }