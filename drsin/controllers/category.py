import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from drsin.lib.base import BaseController, render
from drsin.controllers import *
log = logging.getLogger(__name__)

class CategoryController(BaseController):
	def list(self):
		allCats = ",".join([c.category for c in model.Category.query.all()])
		return allCats
	
	def show(self,category):
		return "Working on it :-)"
		pass