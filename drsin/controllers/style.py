import logging

from pylons import request, response, session, tmpl_context as c
import pycurl
from StringIO import StringIO
from drsin.lib.base import *

log = logging.getLogger(__name__)

class StyleController(BaseController):
	
	def index(self):
		response.headers['content-type'] = 'text/css; charset=utf-8'
		return render("/css/main.css")
	
	def face(self):
		return redirect_to("/graphics/face.png")
	
	def recentPubs(self):
		return ""
		# curlStr = """http://eprints.ecs.soton.ac.uk/cgi/exportview/person/10294/HTML/10294.html"""
		# self.curl = pycurl.Curl()
		# body = StringIO()
		# self.curl.setopt(pycurl.URL, curlStr)
		# self.curl.setopt(pycurl.WRITEFUNCTION, body.write)
		# self.curl.setopt(pycurl.FOLLOWLOCATION, 1)
		# self.curl.setopt(pycurl.MAXREDIRS, 5)
		# self.curl.setopt(pycurl.NOSIGNAL, 1)
		# self.curl.perform()
		# self.curl.close()
		# retVal = body.getvalue()
		# udata=retVal.decode("utf-8")
		# retVal = udata.encode("ascii","ignore")
		# return retVal
