from pycomcigan import TimeTable, get_school_code

class CompTimetable:
	def __init__(self) -> None:
		self.timetable = TimeTable()

	async def get_timetable(self, school_name: str, grade: int, class_num: int):
		school_code = await get_school_code(school_name)
		return await self.timetable.get_timetable(school_code, grade, class_num)