from neispy import Neispy
from asyncio.events import get_event_loop
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

skip = ["토요휴업일", "겨울방학", "여름방학", "봄방학"]

async def main():
	# 필수 인자가 들어가는 곳입니다. API키 등등..
	# 아무런 값이 없으니 샘플 키로 요청합니다.
	async with Neispy(KEY=os.getenv("NEIS_API_KEY")) as neis:
		# 학교 이름으로 학교 정보를 요청하고 교육청 코드 와 학교 코드로 가져옵니다.
		scinfo = await neis.schoolInfo(SCHUL_NM="선린인터넷고등학교")
		row = scinfo.schoolInfo[1].row[0]

		AE = row.ATPT_OFCDC_SC_CODE  # 교육청 코드
		SE = row.SD_SCHUL_CODE  # 학교 코드

		# 학교 코드와 교육청 코드로 2022년 6월 1일날 학사일정 요청
		scschedule = await neis.SchoolSchedule(
			ATPT_OFCDC_SC_CODE=AE, SD_SCHUL_CODE=SE, AA_YMD=202412
		)
		
		for schedule in scschedule.SchoolSchedule[1].row:
			if schedule.EVENT_NM in skip:
				continue
			print(schedule.AA_YMD, schedule.EVENT_NM)

get_event_loop().run_until_complete(main())	

# 출력값

# E10
# 7341025
# 보리밥c
# 감자국c  (5.6.9.13.)
# 순대볶음c  (5.6.10.13.)
# 고구마돈가스c  (1.2.5.6.10.12.13.)
# 배추김치  (9.13.)
# 참외
# 지방선거일
# A+수학교습소
# ['1', '2', '3', '4', '1']
# ['국어', '수학', '즐거운생활', '즐거운생활', '봉사활동']
# ['공동실습소', '건축과', '건축디자인과', '금속과', '기계공작과']
# ['공동실습소', '공업계', '공업계']
# ['건축1-1', '건축1-2', '도시1-1', '도시1-2', '메카1-1']