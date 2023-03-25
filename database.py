from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./ownwait.db"
SQLALCHEMY_DATABASE_URL = "postgresql://gmeiglph:wVc6XfBDD8S2AvoV1WZAtf7GQYNFA20c@satao.db.elephantsql.com/gmeiglph"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

        
