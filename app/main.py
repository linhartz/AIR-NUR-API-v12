from fastapi import FastAPI
from app.routers import (
    nur_router, rsz_router, cr_router,
    cycles_router, air_router, debug_router, health_router
)
from app.settings import API_VERSION, APP_TITLE

app = FastAPI(title=APP_TITLE, version=API_VERSION)

# register routers
app.include_router(health_router.router)
app.include_router(debug_router.router)
app.include_router(nur_router.router)
app.include_router(rsz_router.router)
app.include_router(cycles_router.router)
app.include_router(cr_router.router)
app.include_router(air_router.router)

@app.get("/")
def root():
    return {"status": "running", "version": API_VERSION}
