from models.app_db import AppData
from models import engine, Base, session
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column, Integer, String

metadata = MetaData()
app_data = Table(
    'app_data',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('ip_address', String(15), nullable=False),
    Column('img_url', String(128), nullable=False),
    Column('description', String(255)),
    Column('copyright', String(255), nullable=False),
    Column('date', String(15), nullable=False)
)
metadata.create_all(engine)
