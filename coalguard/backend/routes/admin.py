from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.database import get_db
from models import User
from auth import verify_role
import subprocess
import os

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/reset-demo")
def reset_demo(
    db: Session = Depends(get_db),
    current_user: User = Depends(verify_role(["Corporate Manager"]))
):
    try:
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        seed_script = os.path.join(current_dir, "scripts", "seed_reset.py")
        
        result = subprocess.run([r"c:\users\krish_wq7qnor\appdata\local\programs\python\python311\python.exe", seed_script], capture_output=True, text=True, check=True)
        return {"message": "Demo data reset successfully", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to reset demo data: {e.stderr}"
        )
