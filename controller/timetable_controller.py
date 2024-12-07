# from fastapi import APIRouter, Query
# from module.comp_timetable import CompTimetable
# from models.timetable_model import TimetableModel

# router = APIRouter(prefix="/timetable", tags=["Timetable"])

# comp_timetable = CompTimetable()

# @router.get("", response_model=TimetableModel)
# async def get_timetable(
# 	school_name: str = Query(..., description="School name"),
# 	grade: int = Query(..., description="Grade"),
# 	class_num: int = Query(..., description="Class number"),
# ):
# 	return await comp_timetable.get_timetable(school_name, grade, class_num)