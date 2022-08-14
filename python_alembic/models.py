import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON, Text # ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.orm import relationship

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv(".env")
try:
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_HOSTNAME =os.environ["DB_HOSTNAME"]
    DB_NAME =os.environ["DB_NAME"]
except KeyError:
    raise Exception("Please set DB_USER, DB_PASSWORD, DB_HOSTNAME, DB_NAME in .env file")

# postgresql+psycopg2://postgres:password@db:5432/db_name
SQLALCHEMY_DATABASE_URL="mysql+pymysql://{}:{}@{}:3306/{}".format(DB_USER,DB_PASSWORD,DB_HOSTNAME,DB_NAME)

# Autobind engine with declarative_base. Initialise session with db_session.session_factory()
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Sample_table(Base):
    """ORM object for table
    """
    __tablename__ = 'sample_table'
    id = Column(Integer, primary_key=True, index=True) # auto incrementing
    username = Column(String(200), nullable=False) 
    input = Column(JSON) # Json 
    log = Column(Text) # Long text    
    created_at = Column(DateTime, server_default=func.now())  # Get timestamp upon creation
    updated_at = Column(DateTime, onupdate=func.now())  # Get timestamp per updates

    def _getdict(self):
        return {
            "id": self.id,
            "username": self.username,
            "input": self.input,
            "log": self.log,
            "created_at": self.created_at,
            "updated_at": self.updated_at, 
        }

if __name__ == "__main__":
    pass