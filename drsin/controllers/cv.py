import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from drsin.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CvController(BaseController):

	def index(self):
		return render('/cv/cv.mako')
