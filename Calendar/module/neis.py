from neispy import Neispy
import asyncio
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def get_academic_calendar(neis: Neispy, school_name: str, year: str):
	school_schedules = []
	need_to_skip = ["토요휴업일", "겨울방학", "여름방학", "봄방학"]
	school_info = await neis.schoolInfo(SCHUL_NM=school_name)
	row = school_info.schoolInfo[1].row[0]

	AE = row.ATPT_OFCDC_SC_CODE  # 교육청 코드
	SE = row.SD_SCHUL_CODE  # 표준학교코드

	for month in range(1, 13):
		AA_YMD = f"{year}{month:02d}"
		try:
			schedule = await neis.SchoolSchedule(
				ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, AA_YMD=AA_YMD
			)
			for row in schedule.SchoolSchedule[1].row:
				if row.EVENT_NM in need_to_skip:
					continue
				school_schedules.append({
					"date": row.AA_YMD,
					"schedule": row.EVENT_NM
				})
		except IndexError:
			continue
		except Exception as e:
			if str(e) == "INFO-200 해당하는 데이터가 없습니다.":
				continue
			print(f"{AA_YMD} An error occurred: {e}")
			continue
	return school_schedules

# 임시로 실행
# async def main():
#     async with Neispy(KEY=os.getenv("NEIS_API_KEY")) as neis:
#         print(await get_academic_calendar(neis, "선린인터넷고등학교", 2024))

# asyncio.run(main())
