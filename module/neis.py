from neispy import Neispy
from dotenv import load_dotenv
import os

load_dotenv()

class Neis:
	def __init__(self) -> None:
		self.neis = Neispy(KEY=os.getenv("NEIS_API_KEY"))

	async def get_meal_info(self, school_code: str, date: str):
		try:
			meal_info = await self.neis.mealServiceInfo(SD_SCHUL_CODE=school_code, MLSV_YMD=date)
			return meal_info
		except Exception as e:
			print(f"Failed to fetch meal info: {e}")
			return None

	async def get_school_schedule(self, school_code: str, year: str):
		try:
			schedule_info = await self.neis.SchoolSchedule(SD_SCHUL_CODE=school_code, AA_YMD=year)
			return schedule_info
		except Exception as e:
			print(f"Failed to fetch school schedule: {e}")
			return None