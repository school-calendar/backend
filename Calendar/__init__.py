import os
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI, Depends
from Calendar.router import router
from Calendar.module.sentry import init_sentry

load_dotenv(find_dotenv())

init_sentry(dsn=os.getenv("SENTRY_DSN"))

app = FastAPI(
	title="School Calendar API",
	description="선린인터넷고등학교 소프트웨어과 1학년 웹프로그래밍 실무 수행평가 'School Calendar' API 서버 / Developed by eungyolee",
	version="0.1.0",
)

app.include_router(router)