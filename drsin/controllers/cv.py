import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from drsin.lib.base import BaseController, render
from StringIO import StringIO
import pycurl

import ho.pisa as pisa
log = logging.getLogger(__name__)

class CvController(BaseController):

	def publications(self):
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
	def index(self):
		c.publications = self.publications();
		return render('/cv/cv.mako')
	
	def aspdf(self):
		c.publications = self.publications();
		html = render('/cv/cv.mako')
		result = StringIO()
		pdf = pisa.pisaDocument(StringIO(html.encode("utf-8")), result)
		if not pdf.err:
			response.content_type = "application/pdf"
			return result.getvalue()
		return 'We had some errors<pre>%s</pre>' % escape(html)
