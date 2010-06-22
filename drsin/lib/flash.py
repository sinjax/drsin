class Flash(object):
	def __init__(self,mType="message"):
		self.type = mType
		pass
	def __call__(self, message):
		session = _get_session()
		flash = session.get("flash",{})
		flashType = flash.get(self.type,[])
		flashType.append(message)
		flash[self.type] = flashType
		session['flash'] = flash
		session['flashRendered'] = False
		session.save()

	def pop_message(self):
		session = _get_session()
		message = session.pop("flash", None)
		if not message:
			return None
		session.save()
		return message

def _get_session():
	from pylons import session
	return session

flashMessage = Flash()
flashError = Flash("error")

def getFlash(toRender=True):
	session = _get_session()
	if(toRender):
		session['flashRendered'] = True
	flash = session.get("flash",False)
	if not toRender and session.get('flashRendered',False):
		flash = session.pop("flash",False)
	session.save()
	return flash
	pass