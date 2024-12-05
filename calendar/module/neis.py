from neispy import Neispy
from types import SimpleNamespace
from dotenv import load_dotenv
import os

load_dotenv()

class Neis:
	def __init__(self) -> None:
		self.neis = Neispy(KEY=os.getenv("NEIS_API_KEY"))

	async def get_school_code(self, school_name: str, school_region: str) -> SimpleNamespace:
		async with self.neis as neis:
			school_code = await neis.schoolCode(SCHUL_NM=school_name, ATPT_OFCDC_SC_CODE=school_region)
			return school_code

	async def get_school_schedule(self, school_name: str, school_region: str, school_type: str, school_code: str, year: str) -> SimpleNamespace:
		async with self.neis as neis:
			school_schedule = await neis.schedule(SCHUL_NM=school_name, ATPT_OFCDC_SC_CODE=school_region, SD_SCHUL_CODE=school_code, AY=year, DGHT_CRSE_SC_CODE=school_type)
			return school_schedule
