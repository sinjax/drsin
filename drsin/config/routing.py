"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
	"""Create, configure and return the routes Mapper"""
	map = Mapper(directory=config['pylons.paths']['controllers'],
				 always_scan=config['debug'])
	map.minimization = True

	# The ErrorController route (handles 404/500 error pages); it should
	# likely stay at the top, ensuring it can always be resolved
	map.connect('/error/{action}/{id}', controller='error')

	# CUSTOM ROUTES HERE
	map.connect('/',controller="post",action="list")
	map.connect('/post/show/{id}.{isolated}',controller="post",action="show")
	map.connect('/{controller}/{action}/{id}')
	map.connect('/logout',controller="auth",action="logout")
	map.connect('/login',controller="auth",action="login")
	map.connect('/categories',controller="post",action="categories")
	map.connect('/keywords',controller="post",action="keywords")

	return map