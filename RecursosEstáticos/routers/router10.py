from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_lorde=[Disco(id=20, title="Pure Heroine", artist="Lorde", genre="Alternative", year=2013, label="Universal Music"),
            Disco(id=21, title="The Love Club", artist="Lorde", genre="Alternative", year=2013, label="Universal Music"),
            Disco(id=22, title="Melodrama", artist="Lorde", genre="Pop", year=2017, label="Republic Records"),
            Disco(id=23, title="Solar Power", artist="Lorde", genre="Alternative", year=2021, label="Universal Music")]

# ************** FUNCION GET
@router.get("/Lorde/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def lordeclass():
    return (discos_lorde)

# ************** FUNCION POST
@router.post("/Lorde/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def lordeclass(disco:Disco):
    for index, saved_disco in enumerate(discos_lorde):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_lorde.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/Lorde/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def lordeclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_lorde):
        if saved_disco.id == disco.id:
            discos_lorde[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/Lorde/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def lordeclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_lorde):
        if saved_disco.id ==id:
           del discos_lorde[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 