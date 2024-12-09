from .db import MongoDB
from .schedule import Schedule as schedule_db
from typing import Any, Dict, Optional
from pymongo.results import InsertOneResult, UpdateResult, DeleteResult
from bson import ObjectId

class User(MongoDB):
	def __init__(self) -> None:
		super().__init__()
		self.collection = self.connect()["users"]

	async def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
		return await self.collection.find_one({"_id": ObjectId(user_id)})
	
	async def get_user_by_username(self, username: str) -> Optional[Dict[str, Any]]:
		return await self.collection.find_one({"username": username})

	async def create_user(
		self, 
		username: str, 
		password: str, 
		moderator: bool, 
		school_name: str, 
		grade: int, 
		class_num: int,
	) -> InsertOneResult:
		user_data = {
			"username": username,
			"password": password,
			"moderator": moderator,
			"school_name": school_name,
			"grade": grade,
			"class_num": class_num,
			"school_schedule_added": False
		}
		return await self.collection.insert_one(user_data)

	async def update_user(
		self,
		user_id: str,
		username: str,
		password: str,
		moderator: bool,
		school_name: str,
		grade: int,
		class_num: int,
		school_schedule_added: bool,
	) -> UpdateResult:
		update_data = {
			"username": username,
			"password": password,
			"moderator": moderator,
			"school_name": school_name,
			"grade": grade,
			"class_num": class_num,
			"school_schedule_added": school_schedule_added
		}
		return await self.collection.update_one(
			{"_id": ObjectId(user_id)},
			{"$set": update_data}
		)

	async def delete_user(self, user_id: str) -> DeleteResult:
		# Delete user's schedules
		await schedule_db().delete_schedules(user_id)
		return await self.collection.delete_one({"_id": ObjectId(user_id)})