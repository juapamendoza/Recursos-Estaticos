from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_travis=[Disco(id=155, title="UTOPIA", artist="Travis Scott", genre="Hip-Hop", year=2023, label="Epic Cactus Jack"),
            Disco(id=156, title="ASTROWORLD", artist="Travis Scott", genre="Hip-Hop", year=2018, label="Epic Cactus Jack"),
            Disco(id=157, title="Huncho Jack, Jack Huncho", artist="Travis Scott", genre="Hip-Hop", year=2017, label="Capitol CMG"),
            Disco(id=158, title="Birds in the Trap Sing McKnight", artist="Travis Scott", genre="Hip-Hop", year=2016, label="Epic"),
            Disco(id=159, title="Rodeo (Expanded Edition)", artist="Travis Scott", genre="Hip-Hop", year=2015, label="Epic"),
            Disco(id=160, title="JACKBOYS", artist="Travis Scott", genre="Hip-Hop", year=2019, label="Epic")]

# ************** FUNCION GET
@router.get("/TravisScott/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def travisclass():
    return (discos_travis)

# ************** FUNCION POST
@router.post("/TravisScott/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def travisclass(disco:Disco):
    for index, saved_disco in enumerate(discos_travis):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_travis.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/TravisScott/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def travisclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_travis):
        if saved_disco.id == disco.id:
            discos_travis[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/TravisScott/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def travisclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_travis):
        if saved_disco.id ==id:
           del discos_travis[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 