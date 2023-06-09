import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import TOKEN, RESERVE_TOKEN


###### APP ######
bot = Bot(RESERVE_TOKEN if sys.platform == 'win32' else TOKEN, parse_mode=None)
dp = Dispatcher(bot, storage=MemoryStorage())

###### DATABASE ######
engine = create_engine("sqlite:///database/base")

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)()