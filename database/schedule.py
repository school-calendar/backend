from .db import MongoDB
from typing import Any, List, Dict, Optional
from bson import ObjectId
from utils.exception import ScheduleDateException, ScheduleDeleteException, ScheduleUpdateException, ScheduleCreationException
from models.schedule_model import ScheduleModel

class Schedule(MongoDB):
	def __init__(self) -> None:
		super().__init__()
		self.collection = self.connect()["schedules"]

	async def get_schedule_by_id(self, user_id: str, schedule_id: str) -> Optional[Dict[str, Any]]:
		try:
			return await self.collection.find_one({"user_id": user_id, "_id": ObjectId(schedule_id)})
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch schedule by id: {str(e)}")

	async def get_schedules(self, user_id: str, date: str) -> List[ScheduleModel]:
		try:
			query = {
				"user_id": user_id,
				"start_date": {"$lte": date},
				"end_date": {"$gte": date}
			}
			documents = await self.collection.find(query).to_list(None)
			return [ScheduleModel.get_schedule_id({**doc, "schedule_id": str(doc["_id"])}) for doc in documents]
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch schedules by date: {str(e)}")

	async def get_all_schedules(self, user_id: str) -> List[ScheduleModel]:
		try:
			documents = await self.collection.find({"user_id": user_id}).to_list(None)
			return [ScheduleModel.get_schedule_id({**doc, "schedule_id": str(doc["_id"])}) for doc in documents]
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch all schedules: {str(e)}")


	async def create_schedule(self, user_id: str, start_date: str, end_date: str, school_schedule: bool, schedule: str) -> str:
		try:
			document = {
				"user_id": user_id,
				"start_date": start_date,
				"end_date": end_date,
				"school_schedule": school_schedule,
				"schedule": schedule
			}
			result = await self.collection.insert_one(document)
			return str(result.inserted_id)
		except Exception as e:
			raise ScheduleCreationException(f"Failed to create schedule: {str(e)}")

	async def update_schedule(self, schedule_id: str, user_id: str, start_date: str, end_date: str, school_schedule: bool, schedule: str) -> str:
		try:
			document = {
				"start_date": start_date,
				"end_date": end_date,
				"school_schedule": school_schedule,
				"schedule": schedule
			}
			result = await self.collection.update_one({"user_id": user_id, "_id": ObjectId(schedule_id)}, {"$set": document})
			if result.modified_count == 0:
				raise ScheduleUpdateException("Schedule not found")
			return schedule_id
		except Exception as e:
			raise ScheduleUpdateException(f"Failed to update schedule: {str(e)}")
		
	async def delete_schedule(self, user_id: str, schedule_id: str) -> str:
		try:
			result = await self.collection.delete_one({"user_id": user_id, "_id": ObjectId(schedule_id)})
			if result.deleted_count == 0:
				raise ScheduleDeleteException("Schedule not found")
			return schedule_id
		except Exception as e:
			raise ScheduleDeleteException(f"Failed to delete schedule: {str(e)}")