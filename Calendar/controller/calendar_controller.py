from fastapi import APIRouter, HTTPException, Query
from Calendar.database.schedule import Schedule
from Calendar.database.user import User
from Calendar.models.schedule_model import ScheduleModel
from Calendar.module.neis import get_academic_calendar
from Calendar.utils.exception import ScheduleNotFoundException, UserNotFoundException
from pydantic import BaseModel
from neispy import Neispy
import os
from dotenv import load_dotenv, find_dotenv
from Calendar.utils.user import fetch_user
from typing import Dict, List

router = APIRouter(prefix="/calendar", tags=["Calendar"])

load_dotenv(find_dotenv())

schedule_db = Schedule()
user_db = User()
neis = Neispy(KEY=os.getenv("NEIS_API_KEY"))

@router.get("/school", response_model=List[Dict[str, str]])
async def get_school_calendar(username: str, year: str):
	try:
		user = await user_db.get_user_by_username(username)
		if not user:
			raise UserNotFoundException("User not found")
		
		if user["school_schedule_added"]:
			raise HTTPException(status_code=400, detail="School schedule already added")

		school_name = user["school_name"]
		
		school_schedules = await get_academic_calendar(neis, school_name, year)

		for schedule in school_schedules:
			print(schedule)
			await schedule_db.create_schedule(
				user_id = str(user["_id"]),
				start_date = schedule["date"],
				end_date = schedule["date"],
				school_schedule = True,
				schedule = schedule["schedule"]
			)

		await user_db.update_user(
			user_id = str(user["_id"]),
			username = user["username"],
			password = user["password"],
			moderator = user["moderator"],
			school_name = user["school_name"],
			grade = user["grade"],
			class_num = user["class_num"],
			school_schedule_added = True
		)
		return school_schedules
	
	except UserNotFoundException as e:
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		print(e)
		raise HTTPException(status_code=500, detail=str(e))
	
@router.get("", response_model=list[ScheduleModel])
async def get_schedules(user_id: str = Query(..., description="User ID"), date: str = Query(None, description="Specific date (optional)")):
	try:
		return await schedule_db.get_schedules(user_id, date)
	except ScheduleNotFoundException as e:
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}", response_model=list[ScheduleModel])
async def get_all_schedules(user_id: str):
	try:
		return await schedule_db.get_all_schedules(user_id)
	except ScheduleNotFoundException as e:
		raise HTTPException(status_code=404, detail=str(e))
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

class CreateScheduleRequest(BaseModel):
	user_id: str
	start_date: str
	end_date: str
	school_schedule: bool = False
	schedule: str

@router.post("", response_model=str)
async def create_schedule(request: CreateScheduleRequest):
	try:
		return await schedule_db.create_schedule(
			request.user_id, request.start_date, request.end_date, request.school_schedule, request.schedule
		)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.put("/update", response_model=str)
async def update_schedule(schedule: ScheduleModel):
	try:
		return await schedule_db.update_schedule(**schedule.model_dump())
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete", response_model=str)
async def delete_schedule(user_id: str, schedule_id: str):
	try:
		return await schedule_db.delete_schedule(user_id, schedule_id)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
	
@router.delete("/delete_all", response_model=str)
async def delete_all_schedules(user_id: str):
	try:
		await schedule_db.delete_schedules(user_id)
		user = await user_db.get_user(user_id)
		await user_db.update_user(
			user_id = user_id,
			username = user["username"],
			password = user["password"],
			moderator = user["moderator"],
			school_name = user["school_name"],
			grade = user["grade"],
			class_num = user["class_num"],
			school_schedule_added = False
		)
		return user_id
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))