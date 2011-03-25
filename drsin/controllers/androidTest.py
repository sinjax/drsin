import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from drsin.lib.base import BaseController, render
import httpagentparser

log = logging.getLogger(__name__)

class AndroidtestController(BaseController):
	def useragent(self):
		agent = request.headers['User-Agent']
		allBits = agent.split(";")
		andBit = [x for x in allBits if "Android" in x]
		if len(andBit) > 0:
			andBit = andBit[0].strip()
			if "2.1" in andBit:
				return redirect_to("http://padkite.com/PadKite-RC7-v1_00-eclair")
			elif "2.2" in andBit: # froyo
				if "r2" in andBit:
					return redirect_to("http://padkite.com/PadKite-RC7-v1_00-froyo-FRG83D")
				else:
					return redirect_to("http://padkite.com/PadKite-RC7-v1_00-froyo")
			
		return "User-Agent Not recognised"