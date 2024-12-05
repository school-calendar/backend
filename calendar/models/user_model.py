from pydantic import BaseModel

class User(BaseModel):
	username: str
	password: str
	moderator: bool
	school_name: str
	grade: int
	class_num: int