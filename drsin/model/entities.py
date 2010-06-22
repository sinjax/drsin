from elixir import *
from sqlalchemy.sql.expression import *
class Category(Entity):
	category = Field(Unicode(30))
	parent = ManyToOne('Category')
	children = OneToMany('Category')

_defaultCategory = None
def getDefaultCategory():
	global _defaultCategory
	if(_defaultCategory == None):
		_defaultCategory = Category.query.filter_by(category=u"Default").first().id
	return _defaultCategory


class Post(Entity):
	"""A Blog Post"""
	title = Field(Unicode(30))
	date = Field(DateTime,default=func.now())
	content = Field(UnicodeText)
	keywords = ManyToMany('Keyword')
	category = ManyToOne('Category',colname="",column_kwargs={
		"default":getDefaultCategory
	})
	comments = OneToMany('Comment')

class Keyword(Entity):
	keyword = Field(Unicode(30))
	posts = ManyToMany('Post')

class User(Entity):
	username = Field(Unicode(30))
	password = Field(Unicode(30))

class Comment(Entity):
	author = Field(Unicode(30))
	email = Field(Unicode(30))
	url = Field(Unicode(30))
	date = Field(DateTime)
	content = Field(UnicodeText)
	spam = Field(Float)
	ham = Field(Float)
	posts = ManyToOne('Post')
	