# from fastapi import APIRouter, Query
# from module.neis import Neis
# from models.meal_model import MealModel

# router = APIRouter(prefix="/meal", tags=["Meal"])

# neis_module = Neis()

# @router.get("/", response_model=MealModel)
# async def get_meal(
# 	school_name: str = Query(..., description="School name"),
# 	date: str = Query(..., description="Date (YYYYMMDD)"),
# ):
# 	return await neis_module.get_meal_info(school_name, date)
