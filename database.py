import os
from dotenv import load_dotenv

# 🔥 FORCE FULL PATH
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# Now read variable
DATABASE_URL = os.getenv("DATABASE_URL")

print("DEBUG DATABASE_URL:", DATABASE_URL)  # 👈 MUST SHOW VALUE

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()