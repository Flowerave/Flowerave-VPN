
from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, end_sub_date='None'):
    try:
        user = User(user_id=user_id, end_sub_date=end_sub_date)
        await user.create()
    except UniqueViolationError:
        print('Юзер не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_endsub_date(user_id, new_date: str):
    user = await select_user(user_id)
    await user.update(end_sub_date=new_date).apply()


async def get_user_endsub_date(user_id):
    users_endsub_date = await User.select('end_sub_date').where(User.user_id == user_id).gino.scalar()
    return users_endsub_date
