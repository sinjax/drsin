import logging

from drsin.lib.base import BaseController, render
from drsin.lib.base import *

log = logging.getLogger(__name__)

class AuthController(BaseController):
	def logout(self):
		return redirect_to(controller="admin")
	def login(self):
		return render("/auth/login.mako")
		pass
	
	@validate(schema=AuthenticateSchema(), form="login")
	def enter(self):
		username = self.form_result["username"]
		password = self.form_result["password"]
		errors = {}
		try:
			user = auth.authenticate(username, password)
		except auth.UsernameError, e:
			flashError(str(e))
			return redirect_to(controller="auth",action="login")
		except auth.PasswordError, e:
			flashError(str(e))
			return redirect_to(controller="auth",action="login")
		
		flashMessage("You have logged in successfully")
		session["user"] = user
		session.save()
		request.environ["REMOTE_USER"] = user.username
		referer = session.pop("after_login", None)
		session.save()
		if not referer:
			log.debug("no referer found for login")
		#log.debug("redirecting to %s", referer)
		redirect_to(referer or h.url_for("/"))
	def logout(self):
		session["user"] = None
		session.delete()
		request.environ["REMOTE_USER"] = ""
		flashMessage("You have been logged out.")
		redirect_to(h.url_for("/"))
	
	@validate(schema=PasswordChangeSchema(), form="password")
	def password_change(self):
		current = self.form_result["current"]
		newpass = self.form_result["newpass"]
		retypepass = self.form_result["retypepass"]
		
		try:
			user = auth.authenticate(session["user"].username, current)
		except auth.UsernameError, e:
			flashError(str(e))
			return redirect_to(controller="auth",action="password")
		except auth.PasswordError, e:
			flashError(str(e))
			return redirect_to(controller="auth",action="password")
		
		if newpass != retypepass:
			flashError("Passwords don't match!")
			return redirect_to(controller="auth",action="password")
		db_user = model.User.query.filter(model.User.username==session["user"].username).first()
		db_user.password = newpass
		meta.Session.commit()
		flashMessage("Password has been changed!")
		return redirect_to("/")
		
	def password(self):
		return render("/auth/password.mako")
