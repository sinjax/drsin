"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
from webhelpers.html.tags import checkbox, password
from textile import Textile
t = Textile(lite=True)
from routes import *
from yourgoblin.lib.flash import *
from formbuild import start_with_layout as form_start, end_with_layout as form_end
from formbuild import *

from pylons import request
def current_url():
	# Temporary kludge until pylons.url.current() stabilizes and returns
	# the query string.
	if request.query_string:
		return "%s?%s" % (request.path_info, request.query_string)
	else:
		return request.path_info

def textile(text):
	# remove pre manually (this is a HORRIBLE hack)
	finalString = ""
	preStart = "<pre"
	preEnd = "/pre>"
	while True:
		s = text.find(preStart)
		if(s == -1):
			# no more pre
			finalString += t.textile(text)
			break
		e = text.find(preEnd) + len(preEnd)
		
		finalString += t.textile(text[0:s])
		finalString += text[s:e]
		text = text[e:]
	return finalString