from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, inspections, actions, compliance, dashboard, admin

app = FastAPI(title="CoalGuard API")

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

@app.get("/health")
def health_check():
    return {"status": "ok"}
