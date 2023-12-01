from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://alberto:Alberto69.@db-testing.cmcatynqhv7p.us-east-1.rds.amazonaws.com/python_db"
#DATABASE_URL = "postgresql://sinai:admin@postgreSQL/sinai_db"
DATABASE_URL = "postgresql://sinai:admin@localhost/sinai_db"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()