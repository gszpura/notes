from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.ext.asyncio import AsyncSession

from notes_backend.core.config import settings
from notes_backend.core.schema import DefaultResponse
from notes_backend.modules.note.api_schema import NotesResponse
# from notes_backend.db.deps import get_db


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
def root() -> dict:
    return {
        "status": True,
        "msg": "Project information",
        "details": {
            "name": f"{settings.PROJECT_NAME}",
            "version": f"{settings.APP_VERSION}",
        },
    }


@router.get("/notes", status_code=status.HTTP_200_OK, response_model=NotesResponse)
def root() -> NotesResponse:
    notes = ["First note", "Second note"]
    print(notes)
    return NotesResponse(notes=notes)


# @router.get("/health", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
# async def get_health(db: AsyncSession = Depends(get_db)) -> dict:
#     try:
#         healthy = await db.execute("SELECT 1")
#         if healthy.scalars().first() is None:
#             raise HTTPException(status_code=404, detail={"msg": "Not Healthy ❌"})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
#     return {"status": True, "msg": "Healthy ✅"}