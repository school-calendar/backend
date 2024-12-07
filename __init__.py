from fastapi import FastAPI, Depends

from router import router

app = FastAPI(
	title="School Calendar API",
	description="선린인터넷고등학교 소프트웨어과 1학년 웹프로그래밍 실무 수행평가 'School Calendar' API 서버 / Developed by eungyolee",
	version="0.1.0",
)

app.include_router(router)