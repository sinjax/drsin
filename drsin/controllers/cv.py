import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from drsin.lib.base import BaseController, render
from StringIO import StringIO
import pycurl

log = logging.getLogger(__name__)

class CvController(BaseController):

	def publications(self):
		curlStr = """http://eprints.ecs.soton.ac.uk/cgi/exportview/person/10294/HTML/10294.html"""
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
		# c.publications = "wang"
		c.publications = self.publications();
		udata=c.publications.decode("utf-8")
		c.publications = udata.encode("ascii","ignore")
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
