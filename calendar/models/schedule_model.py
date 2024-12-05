from pydantic import BaseModel

class Schedule(BaseModel):
	user_id: str
	start_date: str
	end_date: str
	school_schedule: bool
	schedule: str