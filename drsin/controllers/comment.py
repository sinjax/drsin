import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from drsin.lib.base import BaseController, render
from drsin.controllers import *
log = logging.getLogger(__name__)

import urllib, hashlib
class CommentController(BaseController):
	def show(self,id):
		c.post = model.Post.query.filter_by(id=id).first()
		return render("/comment/show.mako")
	
	def gravatar(self,email):
		size = 64
		# construct the url
		default = h.url_for("/graphics/gravatar.jpg",qualified=True)
		gravatar_url = "http://www.gravatar.com/avatar.php?"
		gravatar_url += urllib.urlencode({'gravatar_id':hashlib.md5(email.lower()).hexdigest(), 'default':default, 'size':str(size)})
		return redirect_to(gravatar_url)
	
	@rest.dispatch_on(POST='save')
	def create(self):
		return render("/comment/create.mako")
		pass
	
	def save(self):
		comment = model.Comment()
		comment.author = request.params['author']
		comment.email = request.params['email']
		comment.website = request.params['website']
		comment.content = request.params['content']
		comment.posts = model.Post.get_by(id=request.params['postid'])
		comment.ham = 0.9
		comment.spam = 0.1
		model.Session.commit()
		return redirect_to(controller="post",action="show",id=request.params['postid'])