from pydantic import BaseModel, field_serializer
from typing import Optional
from datetime import datetime, timezone, timedelta


class LogResponse(BaseModel):
    id: int
    task_id: int
    result: Optional[str] = None
    status: str
    account_username: Optional[str] = ""
    site_name: Optional[str] = ""
    task_name: Optional[str] = ""
    created_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime) -> str:
        """将时间统一转换为北京时间 (UTC+8) 后输出 ISO 格式"""
        if value is None:
            return None
        # 如果 value 没有时区信息，假设它是 UTC 时间，先加上 UTC 时区
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        # 转换为北京时间 (UTC+8)
        beijing_tz = timezone(timedelta(hours=8))
        return value.astimezone(beijing_tz).isoformat()

    class Config:
        from_attributes = True
