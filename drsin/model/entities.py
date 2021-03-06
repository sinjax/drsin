from elixir import *
from sqlalchemy.sql.expression import *
from sqlalchemy.orm.properties import CompositeProperty
import PyRSS2Gen
import drsin.lib.helpers as h
class Category(Entity):
	category = Field(Unicode(30))
	parent = ManyToOne('Category')
	children = OneToMany('Category')
	posts = OneToMany('Post')

_defaultCategory = None
def getDefaultCategory():
	global _defaultCategory
	if(_defaultCategory == None):
		_defaultCategory = Category.query.filter_by(category=u"Default").first().id
	return _defaultCategory

class Comment(Entity):
	author = Field(Unicode(30))
	email = Field(Unicode(30))
	url = Field(Unicode(30))
	date = Field(DateTime,default=func.now())
	content = Field(UnicodeText)
	spam = Field(Float)
	ham = Field(Float)
	posts = ManyToOne('Post')

	using_options(order_by='date')


def commentFilter(wang):
	print "Called with",wang
	return "comment.ham/comment.spam > 1.0"
	pass

class Post(Entity):
	"""A Blog Post"""
	title = Field(Unicode(30))
	date = Field(DateTime,default=func.now())
	content = Field(UnicodeText)
	keywords = ManyToMany('Keyword')
	category = ManyToOne('Category',column_kwargs={
		"default":getDefaultCategory
	})
	comments = OneToMany('Comment',filter=commentFilter)

def postRSS(posts):
	items = []
	for post in posts:
		item = PyRSS2Gen.RSSItem(
			title = post.title,
			link = "http://www.sinjax.net/post/show/" + str(post.id),
			description = h.textile(" ".join([k for k in post.content.split(" ")][:100]) + "... "),
			guid = PyRSS2Gen.Guid("http://www.sinjax.net/post/show/" + str(post.id)),
			pubDate = post.date)
		items.append(item)
	return items

class Keyword(Entity):
	keyword = Field(Unicode(30))
	posts = ManyToMany('Post')

class User(Entity):
	username = Field(Unicode(30))
	password = Field(Unicode(30))

