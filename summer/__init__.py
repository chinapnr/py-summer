from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from summer.app import *
from summer.command import cli

engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'),
                       pool_recycle=int(app.config.get('SQLALCHEMY_POOL_RECYCLE', "3600")))
Session = sessionmaker(bind=engine)
db = Session()

__version__ = '0.0.2'
