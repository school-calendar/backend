from pydantic import BaseModel, Field
from typing import Optional

class CalenderOuput(BaseModel):
	status: int = Field(..., description="Status code")
	message: Optional[str] = Field(None, description="Message")