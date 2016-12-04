from sqlalchemy import Column, Integer, String, DateTime
from models import Base

class AppTable(Base):
    __tablename__ = 'app_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String, nullable=False)
    api_url = Column(String, nullable=False)
    call_time = Column(DateTime, nullable=False)

class AppTableManager(object):
	@staticmethod
	def add_records(ip, url, u_time, session):
		#return session.query(AppTable).add(ip, url, u_time)
		pass