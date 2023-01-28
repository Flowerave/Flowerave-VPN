import asyncio
from datetime import datetime, timedelta

import config
from utils.db_api.db_gino import db
from utils.db_api import quck_commands as commands


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
