from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

# Configura la conexión a la base de datos
database_url = f"mysql+mysqlconnector://root:appvinoc@mysql/apivinoc"
engine = create_engine(database_url, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()