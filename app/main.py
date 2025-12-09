from fastapi import FastAPI

# Importujeme přímo instanci routeru z každého souboru
from app.routers.air_router import router as air_router
from app.routers.cr_router import router as cr_router
from app.routers.cycles_router import router as cycles_router
from app.routers.debug_router import router as debug_router
from app.routers.health_router import router as health_router
from app.routers.nur_router import router as nur_router
from app.routers.rsz_router import router as rsz_router

app = FastAPI(title="Systemic Risk Model – v12")

# Zahrnutí všech routerů
app.include_router(air_router)
app.include_router(cr_router)
app.include_router(cycles_router)
app.include_router(debug_router)
app.include_router(health_router)
app.include_router(nur_router)
app.include_router(rsz_router)

@app.get("/")
def root():
    return {"status": "running", "version": "12"}
