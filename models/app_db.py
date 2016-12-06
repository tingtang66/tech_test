from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import func
from models import Base

class AppData(Base):
    __tablename__ = 'app_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    description = Column(Text)
    copyright = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)

class AppDataManager(object):
    @staticmethod
    def add_records(ip, url, date, session, copyright=None, description=None):
        data = AppData(ip_address=ip, img_url=url, description=description, copyright=copyright, date=date)
        session.add(data)
    @staticmethod
    def get_record(date, session):
        return session.query(AppData).filter(AppData.date == date)
    @staticmethod
    def get_all_date(session):
        return session.query(AppData.date).group_by(AppData.date).all()
