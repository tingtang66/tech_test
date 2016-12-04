from tornado.web import RequestHandler
from handlers import Env

class NasaDailyHandler(RequestHandler):
	def get(self):
		#Get Local IP
		host_ip = self.request.host	
		nasa_api = 
		template = Env.get_template('nasa_daily.j2')
		self.write(template.render())
	def post(self):
		pass
