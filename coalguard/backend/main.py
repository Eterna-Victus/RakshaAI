from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, inspections, actions, compliance, dashboard, admin, telemetry, ml, tickets, cv_incidents, dgms
from services.telemetry import telemetry_simulator


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await telemetry_simulator.start()
    yield
    await telemetry_simulator.stop()

app = FastAPI(title="CoalGuard API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(inspections.router)
app.include_router(actions.router)
app.include_router(compliance.router)
app.include_router(dashboard.router)
app.include_router(admin.router)
app.include_router(telemetry.router)
app.include_router(ml.router)
app.include_router(tickets.router)
app.include_router(cv_incidents.router)
app.include_router(dgms.router)


@app.websocket("/ws/telemetry")
async def telemetry_websocket(websocket: WebSocket):
    await telemetry.telemetry_socket(websocket)

@app.get("/health")
def health_check():
    return {"status": "ok"}
