from fastapi import APIRouter
from controller.calendar_controller import router as calendar_router
from controller.user_controller import router as user_router
# from controller.timetable_controller import router as timetable_router
# from controller.meal_controller import router as meal_router

router = APIRouter()

router.include_router(calendar_router)
router.include_router(user_router)
# router.include_router(timetable_router)
# router.include_router(meal_router)