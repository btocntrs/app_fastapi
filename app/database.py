from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Valores predeterminados o de respaldo si las variables de entorno no están definidas
default_driver = "postgresql"
default_user = "postgres"
default_password = "admin"
default_host = "localhost"
default_port = "5432"
default_db_name = "postgres"

# Obtener los valores de las variables de entorno si están definidas, de lo contrario, usa los valores predeterminados
db_driver = os.getenv("DB_DRIVER", default_driver)
user = os.getenv("DB_USER", default_user)
password = os.getenv("DB_PASSWORD", default_password)
host = os.getenv("DB_HOST", default_host)
port = os.getenv("DB_PORT", default_port)
db_name = os.getenv("DB_NAME", default_db_name)

# Construir la URL de la base de datos
DATABASE_URL = f"{db_driver}://{user}:{password}@{host}:{port}/{db_name}"
#DATABASE_URL = "postgresql://alberto:Alberto69.@db-testing.cmcatynqhv7p.us-east-1.rds.amazonaws.com/python_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()