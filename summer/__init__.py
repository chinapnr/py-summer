from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from summer.app import app, Base, Summer, Blueprint
from summer.command import cli

engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)
db = Session()

__version__ = '0.0.1.1'
