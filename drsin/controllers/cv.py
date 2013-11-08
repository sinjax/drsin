import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from drsin.lib.base import BaseController, render
from StringIO import StringIO
import pycurl
from IPython import embed
from BeautifulSoup import BeautifulSoup
import re


log = logging.getLogger(__name__)

class CvController(BaseController):

	def publications(self,year=None):
		curlStr = """http://eprints.soton.ac.uk/view/people/47613.include"""
		self.curl = pycurl.Curl()
		body = StringIO()
		self.curl.setopt(pycurl.URL, curlStr)
		self.curl.setopt(pycurl.WRITEFUNCTION, body.write)
		self.curl.setopt(pycurl.FOLLOWLOCATION, 1)
		self.curl.setopt(pycurl.MAXREDIRS, 5)
		self.curl.setopt(pycurl.NOSIGNAL, 1)
		self.curl.perform()
		self.curl.close()
		retVal = body.getvalue()
		udata=retVal.decode("utf-8")
		retVal = udata.encode("ascii","ignore")
		if year is not None:
			year = str(int(year) - 1)
			out = ""
			soup = BeautifulSoup(retVal)
			maindiv = soup.find(attrs={'class': re.compile(r".*\ep_view_page_view_people\b.*")})
			# embed()
			for x in maindiv.findChildren(recursive=False):
				atts = dict(x.attrs)
				if x.name == "h2" and x.text == year:
					break
				out += str(x)
			retVal = out

		return retVal

	def academic(self):
		# c.publications = "wang"
		c.publications = self.publications(2012);
		return render('/cv/cv-academic.mako')

	def index(self):
		# c.publications = "wang"
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
