import logging

from pylons import request, response, session, tmpl_context as c

from drsin.lib.base import *
from drsin.controllers import *
log = logging.getLogger(__name__)

class TagsController(BaseController):
	def list(self):
		allKeys = ",".join([c.keyword for c in model.Keyword.query.all()])
		return allKeys
	def show(self,keyword):
		return "Working on it :-)"
		pass