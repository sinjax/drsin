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

class AdvertSchema(formencode.Schema):
	allow_extra_fields = True
	#filter_extra_fields = True
	strip = True
	id = v.Int(not_empty=True)
	name = v.UnicodeString(not_empty=True)
	target = v.UnicodeString(not_empty=True)
	image = v.UnicodeString(not_empty=True)
	alt = v.UnicodeString(not_empty=True)
	# start = cm.All(
	# 	v.DateConverter(),
	# 	v.DateValidator(not_empty=True,latest_date=datetime(2000, 1, 1))
	# )
	start = cm.All(v.DateValidator(not_empty=True),v.DateConverter(month_style="dd/mm/yyyy"))
	end = cm.All(v.DateValidator(not_empty=True),v.DateConverter(month_style="dd/mm/yyyy"))


class CreateAdvertSchema(formencode.Schema):
	allow_extra_fields = True
	#filter_extra_fields = True
	strip = True
	name = v.String(not_empty=True)
	target = v.String(not_empty=True)
	image = v.String(not_empty=True)
	alt = v.String(not_empty=True)
	# start = cm.All(
	# 	v.DateConverter(),
	# 	v.DateValidator(not_empty=True,latest_date=datetime(2000, 1, 1))
	# )
	start = cm.All(v.DateValidator(not_empty=True),v.DateConverter(month_style="dd/mm/yyyy"))
	end = cm.All(v.DateValidator(not_empty=True),v.DateConverter(month_style="dd/mm/yyyy"))

class SettingsSchema(formencode.Schema):
	allow_extra_fields = True
	#filter_extra_fields = True
	strip = True
	contact_email = v.String(not_empty=True)
	suggestion_email = v.String(not_empty=True)
	adverts = v.StringBool(not_empty=True)
	donations = v.StringBool(not_empty=True)

class SuggestionSchema(formencode.Schema):
	allow_extra_fields = False
	
	strip = True
	suggestion = v.String()
	info = v.String()
	web = v.URL()
	notes = v.String()
