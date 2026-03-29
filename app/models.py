# Import database columns and types
from sqlalchemy import Column, Integer, String

# Import Base class from database file
from app.database import Base


# Define Agent table
class Agent(Base):
    __tablename__ = "agents"  # Table name in PostgreSQL

    # Unique ID for each agent
    id = Column(Integer, primary_key=True, index=True)

    # Agent name (e.g., Chatbot-1)
    name = Column(String, nullable=False)

    # Agent type (e.g., NLP, Vision)
    type = Column(String, nullable=False)

    # Current status (running, stopped, error)
    status = Column(String, nullable=False)