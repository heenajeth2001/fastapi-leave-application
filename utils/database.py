from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool

load_dotenv()
env = os.getenv  

class DBConnection:
    def __init__(self) -> None:
        DB_NAME = env('DB_NAME')
        DB_HOST = env('DB_HOST')
        DB_USER = env('DB_USER')
        DB_PASSWORD = env('DB_PASSWORD')
        DB_PORT = env('DB_PORT')
        password = urllib.parse.quote_plus(DB_PASSWORD)
        connection_string = 'postgresql://' + DB_USER + ':' + password + '@' + DB_HOST + ':' + str(DB_PORT) + '/' + DB_NAME
        print(connection_string)
        SQLALCHEMY_DATABASE_URI = connection_string
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URI,
            echo = False,
            poolclass = NullPool
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
    def getSession(self):
        return  self.SessionLocal()

    def getConnection(self):
        return self.engine.connect()
    
    def getEngine(self):
        return self.engine