import os
from handlers.homepage import IndexHandler
from handlers.nasa_daily import NasaDailyHandler
from handlers.nasa_daily import NasaDailyImportHandler
from tornado.web import StaticFileHandler
route = []
route.append((
    r'/static/(.*)',
    StaticFileHandler,
    {'path': os.path.join(os.path.dirname(__file__), "static")}
))
route.append((r'/', IndexHandler))
route.append((r'/images', NasaDataImportHandler))
route.append((r'/nasa', NasaDailyHandler)) 
