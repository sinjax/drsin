import logging

from pylons import request, response, session, tmpl_context as c
import datetime
from drsin.controllers import *
from drsin.lib.base import *
import PyRSS2Gen
log = logging.getLogger(__name__)

class PostController(BaseController):
	controller_require_perm = True
	controller_allowed_actions = ["index","show","list","rss"]
	def index(self):
		return self.show()
	
	def show(self,id=None,isolated=False):
		c.post = model.Post.query.filter_by(id=id).first()
		# c.post.comments = [x for x in c.post.comments if (x.ham/x.spam) > 1]
		if isolated :
			return render("/post/post.mako")
		else:
			return render("/post/show.mako")
	
	def list(self):
		c.posts = model.Post.query.order_by(model.desc(model.Post.date))
		c.posts = c.posts.all()[:4]
		c.post_list = True
		return render("/post/list.mako")
	
	@rest.dispatch_on(POST='save')
	def create(self):
		c.post = model.Post()
		return render("/post/edit.mako")
	
	@rest.dispatch_on(POST='save')
	def update(self,id=None):
		c.post = model.Post.query.filter_by(id=id).first()
		return render("/post/edit.mako")
	
	def delete(self,id=None):
		post = model.Post.query.filter_by(id=id).first()
		post.delete()
		model.Session.commit()
		return redirect_to("/")
	
	@rest.restrict('POST')
	def save(self):
		edit = model.Post.query.filter_by(id=request.params['id']).first()
		print edit
		if(edit == None):
			edit = model.Post()
			edit.date = datetime.datetime.now()
		edit.title = request.params['title']
		edit.content = request.params['content']
		cat = model.Category.get_by(category=request.params.get('category'))
		if(cat is None):
			cat = model.Category(category=request.params.get('category'))
		edit.category = cat
		
		keys = [x.strip() for x in request.params.get('keywords',"").split(",")]
		keywords = []
		for keyword in keys:
			if keyword == "": continue
			k = model.Keyword.get_by(keyword=keyword)
			if(k is None):
				k = model.Keyword(keyword=keyword)
			keywords.append(k)
		edit.keywords = keywords
		model.Session.commit()
		return
	def rss(self):
		nposts = model.Post.query.order_by(model.desc(model.Post.date)).all()[:4]
		rss = PyRSS2Gen.RSS2(
			title = "MagicalThinking",
			# author = "Dr. Sina Samangooei"
			link = "http://sinjax.net",
			description = "The latest blog posts from Dr. Sina Samangooei, an engineer trapped in an academic's body",
			lastBuildDate = datetime.datetime.utcnow(),
			items = model.postRSS(nposts))
		return rss.to_xml()	
	