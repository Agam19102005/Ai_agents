# Import FastAPI
from fastapi import FastAPI, Depends

# Import DB session
from sqlalchemy.orm import Session

# Import local modules
import app.models as models, app.schemas as schemas
from app.database import SessionLocal, engine
from app.auth import verify_token
from app.llm import generate_summary

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()


# Dependency to get DB session
def get_db():
    db = SessionLocal()  # Open DB connection
    try:
        yield db          # Provide DB session
    finally:
        db.close()        # Close connection


# -------------------------------
# 1. CREATE AGENT
# -------------------------------
@app.post("/agents", dependencies=[Depends(verify_token)])
def create_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db)):
    """
    Creates a new AI agent and stores it in database
    """

    # Convert request data → DB model
    new_agent = models.Agent(**agent.dict())

    # Add to database
    db.add(new_agent)

    # Save changes
    db.commit()

    # Refresh object (get ID from DB)
    db.refresh(new_agent)

    return new_agent


# -------------------------------
# 2. UPDATE STATUS
# -------------------------------
@app.put("/agents/{agent_id}", dependencies=[Depends(verify_token)])
def update_status(agent_id: int, status: str, db: Session = Depends(get_db)):
    """
    Updates the status of an existing agent
    """

    # Find agent in DB
    agent = db.query(models.Agent).filter(models.Agent.id == agent_id).first()

    # Update status
    agent.status = status

    # Save changes
    db.commit()

    return {"message": "Status updated successfully"}


# -------------------------------
# 3. GET ALL AGENTS
# -------------------------------
@app.get("/agents", dependencies=[Depends(verify_token)])
def get_agents(db: Session = Depends(get_db)):
    """
    Returns all agents + AI-generated summaries
    """

    # Get all agents from DB
    agents = db.query(models.Agent).all()

    result = []

    # Loop through agents
    for agent in agents:
        # Call LLM for summary
        summary = generate_summary(agent.status)

        # Append response
        result.append({
            "id": agent.id,
            "name": agent.name,
            "type": agent.type,
            "status": agent.status,
            "summary": summary
        })

    return result