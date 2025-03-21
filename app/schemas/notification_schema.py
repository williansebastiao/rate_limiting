from pydantic import BaseModel, EmailStr

from app.enums import NotificationType


class NotificationSchema(BaseModel):
    email: EmailStr
    message: str
    notification_type: NotificationType
