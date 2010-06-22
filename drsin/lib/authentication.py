import logging

log = logging.getLogger(__name__)
from drsin.model import User
from pylons import config

class SessionUser(object):
	"""docstring for SessionUser"""
	def __init__(self,dbUser):
		super(SessionUser, self).__init__()
		self.username = dbUser.username
		self.password = dbUser.password
	def has_perm(self,perm,**perm_kw):
		return True

class AdminBypassUser(SessionUser):
	"""A default admin user"""
	def __init__(self):
		super(AdminBypassUser, self).__init__()

def authenticate(username, password):
	"""Authenticate a user via database, and return a ``User`` object.
	Raises ``AuthenticationError`` or subclass if the user is rejected.
	If authentication is disabled in the config file, return the
	"Admin Bypass" user, who can do anything.
	"""
	# If authentication is disabled, use Admin Bypass.
	if not config.get("use_auth",True):
		return AdminBypassUser()
	# Here we assume a SQLAlchemy Session object, and an ORM class ``User``.
	# The ``.get`` method returns a User instance, or None if no such user.
	db_user = User.query.filter(User.username==username).first()
	if not db_user:
		log.debug("database has no user '%s'", username)
		raise UsernameError()
	elif not db_user.password:
		log.error("user record '%s' in db has invalid password; pretending user doesn't exist")
		raise UsernameError()
	elif password != db_user.password:
		log.debug("database password for user '%s' does not match", username)
		raise PasswordError()
	return SessionUser(db_user)

class DeclarativeException(Exception):
	"""A simpler way to define an exception with a fixed message.
	"""
	message=""

	def __init__(self, message=None):
		Exception.__init__(self, message or self.message)

class AuthenticationError(DeclarativeException):  
	pass
class UsernameError(AuthenticationError):
	message = "no such user"
class PasswordError(AuthenticationError):
	message = "incorrect password"