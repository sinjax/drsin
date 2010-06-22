"""The application's model objects"""
from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker
import elixir

# replace the elixir session with pylons one
Session = scoped_session(sessionmaker(autoflush=True)) 
elixir.session = Session
elixir.options_defaults.update({'shortnames': True})
# use the elixir metadata
metadata = elixir.metadata
from entities import *

def init_model(engine):
	"""Call me before using any of the tables or classes in the model"""
	metadata.bind = engine
	metadata.echo = False
	elixir.setup_all()
	

