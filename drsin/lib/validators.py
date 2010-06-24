import formencode
from formencode import validators as v
from formencode import compound as cm
from datetime import date, timedelta
import formencode.variabledecode as fvd


class PasswordChangeSchema(formencode.Schema):
	allow_extra_fields = True
	#filter_extra_fields = True
	strip = True

	current = v.String(not_empty=True)
	newpass = v.String(not_empty=True)
	retypepass = v.String(not_empty=True)

class AuthenticateSchema(formencode.Schema):
	allow_extra_fields = True
	strip = True
	
	username = v.String(not_empty=True)
	password = v.String(not_empty=True)

class CommentSchema(formencode.Schema):
	allow_extra_fields = True

	strip = True
	author = v.String(not_empty=True)
	email = v.Email()
	website = v.URL()
	content = v.String(not_empty=True)
