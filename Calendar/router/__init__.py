from fastapi import APIRouter
from Calendar.controller.calendar_controller import router as calendar_router
from Calendar.controller.user_controller import router as user_router

router = APIRouter()

router.include_router(calendar_router)
router.include_router(user_router)