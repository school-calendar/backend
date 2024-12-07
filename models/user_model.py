from pydantic import BaseModel

class UserModel(BaseModel):
	username: str
	password: str
	moderator: bool = False
	school_name: str
	grade: int
	class_num: int