from fastapi import APIRouter, Depends, HTTPException, status

from calendar.database import Schedule

class ScheduleController:
	def __init__(self) -> None:
		self.database = Schedule()