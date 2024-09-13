from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

###########################################################################################################

# opening a file with the SQLite database
# The file will be located at the same directory in the file sql_app.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


###########################################################################################################

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#connect_args={"check_same_thread": False}
#...is needed only for SQLite. It's not needed for other databases.


###########################################################################################################

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


###########################################################################################################

# Create a Base class
Base = declarative_base()


###########################################################################################################



###########################################################################################################