from . import MongoDB
from typing import Any, List, Dict, Optional
from bson import ObjectId
from calendar.utils.exception import ScheduleDateException, ScheduleDeleteException, ScheduleUpdateException, ScheduleCreationException

class Schedule(MongoDB):
	def __init__(self) -> None:
		super().__init__()
		self.collection = self.connect()["schedules"]

	async def get_schedules(self, user_id: str) -> List[Dict[str, Any]]:
		try:
			return await self.collection.find({"user_id": user_id}).to_list(None)
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch schedules: {str(e)}")

	async def get_schedule_by_id(self, user_id: str, schedule_id: str) -> Optional[Dict[str, Any]]:
		try:
			return await self.collection.find_one({"user_id": user_id, "_id": ObjectId(schedule_id)})
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch schedule by id: {str(e)}")

	async def get_schedules_by_date(self, user_id: str, date: str) -> List[Dict[str, Any]]:
		try:
			query = {
				"user_id": user_id,
				"start_date": {"$lte": date},
				"end_date": {"$gte": date}
			}
			return await self.collection.find(query).to_list(None)
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch schedules by date: {str(e)}")

	async def get_schedules_by_month(self, user_id: str, month: str) -> List[Dict[str, Any]]:
		try:
			query = {
				"user_id": user_id,
				"start_date": {"$regex": f"^{month}", "$options": "i"}
			}
			return await self.collection.find(query).to_list(None)
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch schedules by month: {str(e)}")

	async def get_schedules_by_year(self, user_id: str, year: str) -> List[Dict[str, Any]]:
		try:
			query = {
				"user_id": user_id,
				"start_date": {"$regex": f"^{year}", "$options": "i"}
			}
			return await self.collection.find(query).to_list(None)
		except Exception as e:
			raise ScheduleDateException(f"Failed to fetch schedules by year: {str(e)}")

	async def create_schedule(self, user_id: str, start_date: str, end_date: str, school_schedule: bool, schedule: str) -> str:
		try:
			document = {
				"user_id": user_id,
				"start_date": start_date,
				"end_date": end_date,
				"schedule": schedule,
				"school_schedule": school_schedule
			}
			result = await self.collection.insert_one(document)
			return str(result.inserted_id)
		except Exception as e:
			raise ScheduleCreationException(f"Failed to create schedule: {str(e)}")

	async def update_schedule(self, user_id: str, schedule_id: str, start_date: str, end_date: str, school_schedule: bool, schedule: str) -> bool:
		try:
			filter_query = {"user_id": user_id, "_id": ObjectId(schedule_id)}
			update_query = {"$set": {"start_date": start_date, "end_date": end_date, "schedule": schedule, "school_schedule": school_schedule}}
			result = await self.collection.update_one(filter_query, update_query)
			return result.modified_count > 0
		except Exception as e:
			raise ScheduleUpdateException(f"Failed to update schedule: {str(e)}")

	async def delete_schedule(self, user_id: str, schedule_id: str) -> bool:
		try:
			result = await self.collection.delete_one({"user_id": user_id, "_id": ObjectId(schedule_id)})
			return result.deleted_count > 0
		except Exception as e:
			raise ScheduleDeleteException(f"Failed to delete schedule: {str(e)}")