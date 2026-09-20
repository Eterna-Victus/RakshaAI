import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ENGINE_PATH = Path(__file__).resolve().parents[2] / "khaan-netra" / "pred_engine.py"


def predict_rul(sensor_values: dict[str, Any]) -> dict[str, Any]:
    """Run the shared edge predictor and return a normalized prediction."""
    completed = subprocess.run(
        [sys.executable, str(ENGINE_PATH), "--input-json", json.dumps(sensor_values)],
        capture_output=True,
        text=True,
        timeout=5,
        check=True,
    )
    return json.loads(completed.stdout)
