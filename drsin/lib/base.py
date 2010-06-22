"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.controllers.util import abort, redirect_to
from pylons.templating import render_mako as render
from pylons.decorators import rest,validate
from pylons import request, response, session, tmpl_context as c
from pylons import config
import drsin.lib.helpers as h
import drsin.model as model
import drsin.lib.authentication as auth
from drsin.lib.validators import *
from drsin.lib.flash import *

import logging
log = logging.getLogger(__name__)
class BaseController(WSGIController):
	controller_require_perm = None
	controller_allowed_actions = []
	def __call__(self, environ, start_response):
		try:
			return WSGIController.__call__(self, environ, start_response)
		finally:
			model.Session.remove()
	def __before__(self):
		"""Do authentication and authorization according to controller
		class attributes.

		The login controller MUST set controller_require_perm = None,
		or the login redirect will cause an infinite redirect!
		"""
		c.controller = request.environ['pylons.routes_dict']['controller']
		c.action = request.environ['pylons.routes_dict']['action']

		is_auth = config.get("use_auth")
		user = session.get("user")
		is_admin_bypass = isinstance(user, auth.AdminBypassUser)
		if not config["auth.use_auth"]:
			if not is_admin_bypass:  # Switch to bypass user.
				session["user"] = user = auth.AdminBypassUser()
			return
		if is_admin_bypass:   # Log bypass user out.
			session["user"] = user = None
		if user:   # Set the HTTP variable for the current user.
			request.environ["REMOTE_USER"] = user.username
		if self.controller_require_perm:
			if c.action in self.controller_allowed_actions :
				return
			if not user: # Require login.
				referer = h.current_url()
				session["after_login"] = referer
				log.debug("setting session['after_login'] to %r", referer)
				session.save()
				redirect_to(config["auth.login.path"])
			self._REQUIRE_PERM(self.controller_require_perm)

	def _has_perm(self, perm, **perm_kw):
		"""This method recognizes two additional ``perm`` values besides those
		handled by the User object:
		``None``: no permission required.
		``"authenticated"``: user must be logged in, but no additional
			permission required.
		"""
		if perm is None:
			return True
		user = session.get("user")
		if not user:
			return False
		if perm == "authenticated":
			return True
		return session["user"].has_perm(perm, **perm_kw)

	def _REQUIRE_PERM(self, perm, **perm_kw):
		"""Raise a Forbidden error if the user doesn't have the permission.

		The method name is capitalized to make it easier to find and audit in
		code.
		"""
		if not self._has_perm(perm, **perm_kw):
			reason = "'%s' permission required for the requested operation."
			abort(403, reason % perm.upper())

