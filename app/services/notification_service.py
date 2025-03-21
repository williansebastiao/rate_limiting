from app.schemas import NotificationSchema


class NotificationService:
    def __init__(self): ...

    async def send_notification(
        self, payload: NotificationSchema
    ) -> NotificationSchema:
        return payload
