import logging

from pylons import request, response, session, tmpl_context as c

from drsin.lib.base import *
from drsin.controllers import *
from drsin.controllers import post
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
	
	# @validate(schema=CommentSchema(),form=post.show)
	def save(self):
		return
		schema = CommentSchema()
		form_result = None
		try:
			form_result = schema.to_python(request.params)
		except formencode.validators.Invalid, error:
			c.form_result = error.value
			c.form_errors = error.error_dict or {}
			print "THE ERRORS",error.error_dict 
			print c.form_result
			c.post = model.Post.query.filter_by(id=request.params['postid']).first()
			return render("/post/show.mako")
		comment = model.Comment()
		print "THE RESULTS:",form_result
		comment.author = form_result.get('author')
		comment.email = form_result.get('email')
		comment.url = form_result.get('website')
		comment.content = form_result.get('content')
		comment.posts = model.Post.get_by(id=request.params['postid'])
		comment.ham = 0.9
		comment.spam = 0.1
		model.Session.commit()
		return redirect_to(controller="post",action="show",id=request.params['postid'])