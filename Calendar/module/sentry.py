import sentry_sdk

from sentry_sdk.integrations.pymongo import PyMongoIntegration
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration

def init_sentry(dsn: str):
	sentry_sdk.init(
		dsn=dsn,
		integrations=[
			PyMongoIntegration(),
			AioHttpIntegration(),
			FastApiIntegration()
		],
		send_default_pii=True,
		sample_rate=1.0
	)