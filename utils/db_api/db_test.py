import asyncio

import config
from utils.db_api.db_gino import db
from utils.db_api import quck_commands as commands


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1)
    await commands.add_user(2)
    await commands.add_user(3)
    await commands.add_user(4)
    await commands.add_user(5)
    await commands.add_user(6)
    await commands.add_user(7)

    users = await commands.select_all_users()
    print(users)
    count = await commands.count_users()
    print(count)
    user = await commands.select_user(4)
    print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())