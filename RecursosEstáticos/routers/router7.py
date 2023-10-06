from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_gaga=[Disco(id=180, title="Love For Sale (Deluxe)", artist="Lady Gaga", genre="Jazz", year=2021, label="Interscope"),
            Disco(id=181, title="Chromatica", artist="Lady Gaga", genre="Pop", year=2020, label="Interscope"),
            Disco(id=182, title="Joanne", artist="Lady Gaga", genre="Indie", year=2016, label="Interscope"),
            Disco(id=183, title="Cheek to Cheek", artist="Lady Gaga", genre="Jazz", year=2014, label="Interscope"),
            Disco(id=184, title="ARTPOP", artist="Lady Gaga", genre="Pop", year=2013, label="Interscope"),
            Disco(id=185, title="Born this Way", artist="Lady Gaga", genre="Pop", year=2011, label="Interscope"),
            Disco(id=186, title="The Fame Monster", artist="Lady Gaga", genre="Pop", year=2009, label="Interscope"),
            Disco(id=187, title="The Fame", artist="Lady Gaga", genre="Pop", year=2008, label="Interscope")]

# ************** FUNCION GET
@router.get("/LadyGaga/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def gagaclass():
    return (discos_gaga)

# ************** FUNCION POST
@router.post("/LadyGaga/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def gagaclass(disco:Disco):
    for index, saved_disco in enumerate(discos_gaga):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_gaga.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/LadyGaga/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def gagaclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_gaga):
        if saved_disco.id == disco.id:
            discos_gaga[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/LadyGaga/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def gagaclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_gaga):
        if saved_disco.id ==id:
           del discos_gaga[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 