from typing import Dict
from fastapi import APIRouter, HTTPException
from Calendar.database.user import User
from .exception import UserNotFoundException

user_db = User()

async def fetch_user(username: str) -> Dict:
	try:
		user = await user_db.get_user_by_username(username)
		if not user:
			raise UserNotFoundException("User not found")
		return {
			"user_id": str(user["_id"]),
			"username": user["username"],
			"moderator": user["moderator"],
			"school_name": user["school_name"],
			"grade": user["grade"],
			"class_num": user["class_num"],
			"school_schedule_added": user["school_schedule_added"]
		}
	except UserNotFoundException as e:
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))