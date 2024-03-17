from os import getenv

from dotenv import load_dotenv

def init(app):

    load_dotenv()

    app.config[
        'SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
