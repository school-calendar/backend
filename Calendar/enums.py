from enum import Enum

class SchoolRegion(Enum):
	SEOUL = "B10"  # 서울특별시교육청
	BUSAN = "C10"  # 부산광역시교육청
	DAEGU = "D10"  # 대구광역시교육청
	INCHEON = "E10"  # 인천광역시교육청
	GWANGJU = "F10"  # 광주광역시교육청
	DAEJEON = "G10"  # 대전광역시교육청
	ULSAN = "H10"  # 울산광역시교육청
	SEJONG = "I10"  # 세종특별자치시교육청
	GYEONGGI = "J10"  # 경기도교육청
	GANGWON = "K10"  # 강원도교육청
	CHUNGBUK = "M10"  # 충청북도교육청
	CHUNGNAM = "N10"  # 충청남도교육청
	JEONBUK = "P10"  # 전라북도교육청
	JEONNAM = "Q10"  # 전라남도교육청
	GYEONGBUK = "R10"  # 경상북도교육청
	GYEONGNAM = "S10"  # 경상남도교육청
	JEJU = "T10"  # 제주특별자치도교육청

class MealType(Enum):
	BREAKFAST = "조식"
	LUNCH = "중식"
	DINNER = "석식"

class ScheduleType(Enum):
	PERSONAL = "개인 일정"
	SCHOOL = "학사 일정"