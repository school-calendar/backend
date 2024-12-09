from fastapi import APIRouter, HTTPException
from Calendar.database.user import User
from Calendar.models.user_model import UserModel
from Calendar.utils.exception import UserNotFoundException
from Calendar.utils.password import hash_password
from Calendar.utils.user import fetch_user
from Calendar.utils.jwt import create_access_token
from typing import Dict
from bcrypt import checkpw

router = APIRouter(prefix="/user", tags=["User"])

user_db = User()

@router.get("/signin", response_model=str)
async def sign_in(username: str, password: str):
	try:
		user = await user_db.get_user_by_username(username)
		if not user:
			raise UserNotFoundException("User not found")
		if not checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
			raise HTTPException(status_code=401, detail="Invalid password")
		return create_access_token({"sub": str(user["_id"])})
	except UserNotFoundException as e:
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.get("/{username}", response_model=Dict)
async def get_user(username: str):
	return await fetch_user(username)

@router.post("/signup", response_model=str)
async def create_user(user: UserModel):
	existing_user = await user_db.get_user_by_username(user.username)
	if existing_user:
		raise HTTPException(status_code=400, detail="User already exists")
	
	hashed_password = hash_password(user.password)

	try:
		result = await user_db.create_user(
			username=user.username,
			password=hashed_password,
			moderator=user.moderator,
			school_name=user.school_name,
			grade=user.grade,
			class_num=user.class_num
		)
		return str(result.inserted_id)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.put("/{user_id}", response_model=str)
async def update_user(user_id: str, user: UserModel):
	try:
		result = await user_db.update_user(
			userId=user_id,
			username=user.username,
			password=hash_password(user.password),
			moderator=user.moderator,
			school_name=user.school_name,
			grade=user.grade,
			class_num=user.class_num,
			school_schedule_added=user.school_schedule_added
		)
		if result.modified_count == 0:
			raise HTTPException(status_code=404, detail="User not found")
		return str(user_id)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{user_id}", response_model=str)
async def delete_user(user_id: str):
	try:
		result = await user_db.delete_user(user_id)
		if result.deleted_count == 0:
			raise HTTPException(status_code=404, detail="User not found")
		return str(user_id)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
