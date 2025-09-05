from fastapi import FastAPI
from .routers import users, licenses, mfa, teams, mailbox

app = FastAPI()

app.include_router(users.router)
app.include_router(licenses.router)
app.include_router(mfa.router)
app.include_router(teams.router)
app.include_router(mailbox.router)

@app.get("/health")
def read_root():
    return {"status": "ok"}
