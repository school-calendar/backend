import os
from dotenv import load_dotenv, find_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any

load_dotenv(find_dotenv())

MONGO_URI = os.getenv("MONGODB_URI")

class MongoDB:
	def __init__(self) -> None:
		self.client = AsyncIOMotorClient(MONGO_URI)
		self.db = self.client["calendar"]

	def connect(self) -> Any:
		print("Connected Successfully to MongoDB")
		print(MONGO_URI)
		return self.db

	async def close(self) -> None:
		print("Closing MongoDB connection")
		self.client.close()
