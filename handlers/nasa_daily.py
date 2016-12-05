import os
from tornado.web import RequestHandler
from handlers import Env
from models import session_scope
from models.app_db import AppDataManager

class NasaDailyHandler(RequestHandler):
    def get(self):
        with session_scope() as session:
            data = AppDataManager.get_data(date, session)
        template = Env.get_template('nasa_daily.j2')
        self.write(template.render())
    def post(self):
        pass

class NasaDataImportHandler(RequestHandler)
    def post(self):
    #get ip, returned data
        host_ip = os.environ['HOST_IP']
        copyright = self.get_argument('copyright')
        date = self.get_argument('date')
        description = self.get_argument('explanation')
        img = self.get_argument('hdurl')
        with session_scope() as session:
            AppDataManager.add_records(host_ip, img, copyright, date, session, description)

