import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
import pycurl
from StringIO import StringIO
from drsin.lib.base import BaseController, render

log = logging.getLogger(__name__)

class StyleController(BaseController):
	
	def index(self):
		response.headers['content-type'] = 'text/css; charset=utf-8'
		return render("/css/main.css")
	
	def face(self):
		return redirect_to("/graphics/face.png")
	
	def recentPubs(self):
		curlStr = """http://eprints.ecs.soton.ac.uk/cgi/search/quicksearch/export_ecs_HTML.html?screen=Public%3A%3AEPrintSearch&_action_export=1&output=HTML&exp=0|1|-date%2Fcreators_name%2Ftitle|archive|-|basic%3Aabstract%2Fcreators_name%2Fdate%2Feditors_name%2Fkeywords%2Ftitle%3AALL%3AIN%3Asamangooei|-|eprint_status%3Aeprint_status%3AALL%3AEQ%3Aarchive|metadata_visibility%3Ametadata_visibility%3AALL%3AEX%3Ashow&cache=4122428"""
		self.curl = pycurl.Curl()
		body = StringIO()
		self.curl.setopt(pycurl.URL, curlStr)
		self.curl.setopt(pycurl.WRITEFUNCTION, body.write)
		self.curl.setopt(pycurl.FOLLOWLOCATION, 1)
		self.curl.setopt(pycurl.MAXREDIRS, 5)
		self.curl.setopt(pycurl.NOSIGNAL, 1)
		self.curl.perform()
		self.curl.close()
		return body.getvalue()
