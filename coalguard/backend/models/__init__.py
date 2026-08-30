import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, Boolean, ForeignKey, DateTime, JSON, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

def generate_uuid():
    return str(uuid.uuid4())

class Role(Base):
    __tablename__ = "roles"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True, index=True)

class Mine(Base):
    __tablename__ = "mines"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=generate_uuid)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password_hash = Column(String)
    role_id = Column(String, ForeignKey("roles.id"))
    mine_id = Column(String, ForeignKey("mines.id"), nullable=True)

class ComplianceRequirement(Base):
    __tablename__ = "compliance_requirements"
    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String)
    mine_id = Column(String, ForeignKey("mines.id"))
    due_date = Column(DateTime)
    status = Column(String) # e.g., compliant, overdue

class Inspection(Base):
    __tablename__ = "inspections"
    id = Column(String, primary_key=True, default=generate_uuid)
    temp_uuid = Column(String, unique=True, index=True)
    mine_id = Column(String, ForeignKey("mines.id"))
    inspector_id = Column(String, ForeignKey("users.id"))
    gps_lat = Column(Float)
    gps_lon = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Observation(Base):
    __tablename__ = "observations"
    id = Column(String, primary_key=True, default=generate_uuid)
    inspection_id = Column(String, ForeignKey("inspections.id"))
    severity = Column(String) # Low, Medium, High, Critical
    description = Column(Text)
    photo_url = Column(String, nullable=True)

class CorrectiveAction(Base):
    __tablename__ = "corrective_actions"
    id = Column(String, primary_key=True, default=generate_uuid)
    observation_id = Column(String, ForeignKey("observations.id"))
    owner_id = Column(String, ForeignKey("users.id"))
    status = Column(String, default="OPEN") # OPEN, ASSIGNED, IN_PROGRESS, VERIFICATION, CLOSED, REOPENED
    due_date = Column(DateTime)
    evidence_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(String, primary_key=True, default=generate_uuid)
    entity_type = Column(String)
    entity_id = Column(String)
    actor_id = Column(String, ForeignKey("users.id"))
    action = Column(String)
    before_json = Column(JSON, nullable=True)
    after_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class RiskScore(Base):
    __tablename__ = "risk_scores"
    id = Column(String, primary_key=True, default=generate_uuid)
    mine_id = Column(String, ForeignKey("mines.id"))
    score = Column(Float)
    reasons_json = Column(JSON)
    calculated_at = Column(DateTime, default=datetime.utcnow)
