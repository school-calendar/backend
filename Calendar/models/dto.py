from pydantic import BaseModel, Field
from typing import Optional

class CalendarDefaultInput(BaseModel):
		pass

class CalendarDefaultOutput(BaseModel):
		status: Optional[int] = Field(1, description="Status code")
		message: Optional[str] = Field(None, description="Message")	
