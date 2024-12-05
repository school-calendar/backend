import os
from dotenv import load_dotenv, find_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any

load_dotenv(find_dotenv())

class MongoDB:
	def __init__(self) -> None:
		self.client = AsyncIOMotorClient(
			os.getenv("MONGO_URI", "mongodb://localhost:27017"),
			serverSelectionTimeoutMS=5000
		)
		self.db = self.client[os.getenv("MONGO_DB", "default")]

	def connect(self) -> Any:
		return self.db

	async def close(self) -> None:
		self.client.close()
