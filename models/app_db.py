from sqlalchemy import Column, Integer, String, DateTime
from models import Base

class AppData(Base):
    __tablename__ = 'app_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    description = Column(String)
    copyright = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)

class AppDataManager(object):
    @staticmethod
    def add_records(ip, url, copyright, date, session, description=None):
    #return session.query(AppTable).add(ip, url, u_time)
        data = AppData(ip_address=ip, img_url=url, description=description, copyright=copyright, date=date)
        return session.add(data)
