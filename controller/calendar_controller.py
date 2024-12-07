from fastapi import APIRouter, HTTPException, Query
from database.schedule import Schedule
from module.neis import Neis
from models.schedule_model import ScheduleModel
from utils.exception import ScheduleNotFoundException
from pydantic import BaseModel

router = APIRouter(prefix="/calendar", tags=["Calendar"])

schedule_db = Schedule()
neis_module = Neis()

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
