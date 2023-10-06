from fastapi import FastAPI, HTTPException, status
from routers import router1, router2, router3, router4, router5, router6, router7, router8, router9, router10
from fastapi.staticfiles import StaticFiles

app= FastAPI()

# Crear routers
app.include_router(router1.router)
app.include_router(router2.router)
app.include_router(router3.router)
app.include_router(router4.router)
app.include_router(router5.router)
app.include_router(router6.router)
app.include_router(router7.router)
app.include_router(router8.router)
app.include_router(router9.router)
app.include_router(router10.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", status_code=status.HTTP_202_ACCEPTED, response_description="Get aceptado :)")
async def imprimir():
    return "Programa Main :)"

#-uvicorn main:app --reload-