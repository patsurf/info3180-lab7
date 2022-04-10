import os
import sys
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

EXEC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = UPLOAD_FOLDER = "./Uploads"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    

     # Create the upload folder if its deleted
    if os.path.isdir(UPLOAD_FOLDER) is False:
        os.mkdir(UPLOAD_FOLDER)

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
