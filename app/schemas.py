# Import Pydantic for request/response validation
from pydantic import BaseModel


# Input schema (when user creates agent)
class AgentCreate(BaseModel):
    name: str
    type: str
    status: str


# Output schema (when returning agent data)
class AgentResponse(BaseModel):
    id: int
    name: str
    type: str
    status: str

    # Enable ORM compatibility
    class Config:
        orm_mode = True