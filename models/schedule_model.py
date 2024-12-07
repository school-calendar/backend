from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class ScheduleModel(BaseModel):
	schedule_id: str = Field(..., description="Schedule ID")
	user_id: str = Field(..., description="User ID")
	start_date: str = Field(..., description="Schedule start date (YYYYMMDD)")
	end_date: str = Field(..., description="Schedule end date (YYYYMMDD)")
	school_schedule: bool = Field(False, description="Indicates if this is a school schedule")
	schedule: str = Field(..., description="Schedule description")

	@classmethod
	def get_schedule_id(cls, document: dict) -> "ScheduleModel":
		document["_id"] = str(document["_id"])
		return cls(**document)