from fastapi import FastAPI, Depends

from .router import router

app = FastAPI(
		title="Calendar API",
		description="A simple calendar API",
		version="0.1.0",
)


app.include_router(router)