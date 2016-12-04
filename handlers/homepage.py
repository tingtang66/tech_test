from tornado.web import RequestHandler
import subprocess

class IndexHandler(RequestHandler):
    def get(self):
    	interfaces = subprocess.Popen(['ip', 'addr'], stdout=subprocess.PIPE)
    	eth1_brief = subprocess.Popen(
    		['grep', 'global eth1'],
    		stdin=interfaces.stdout,
    		stdout=subprocess.PIPE
    	)
    	interfaces.stdout.close()
    	output = eth1_brief()[0]
        self.render("index.html", output=output)

