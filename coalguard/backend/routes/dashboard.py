from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from models import User, Mine, RiskScore, ComplianceRequirement, CorrectiveAction, Observation, Inspection
from auth import get_current_user

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/corporate")
def get_corporate_dashboard(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    mines = db.query(Mine).all()
    total_mines = len(mines)
    
    overdue_actions = db.query(CorrectiveAction).filter(
        CorrectiveAction.status != "CLOSED",
    ).count() # Simplified for hackathon, normally check due_date
    
    risk_scores = db.query(RiskScore).order_by(RiskScore.score.desc()).all()
    
    return {
        "total_mines": total_mines,
        "overdue_actions": overdue_actions,
        "critical_mines": len([rs for rs in risk_scores if rs.score > 75]),
        "mine_risks": [{"mine_id": rs.mine_id, "score": rs.score, "reasons": rs.reasons_json} for rs in risk_scores]
    }
