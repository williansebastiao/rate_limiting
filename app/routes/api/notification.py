from fastapi import APIRouter, HTTPException, status

from app.schemas import NotificationSchema
from app.services import NotificationService

router = APIRouter()


@router.post(
    "/notification",
    tags=["Notification"],
    response_model=NotificationSchema,
    status_code=status.HTTP_200_OK,
)
async def send_notification(payload: NotificationSchema):
    try:
        service = NotificationService()
        response = await service.send_notification(payload=payload)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        ) from e
