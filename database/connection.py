from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:1234@localhost/college"

engine = create_engine(DATABASE_URL)