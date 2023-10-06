from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_metallica=[Disco(id=141, title="72 Seasons", artist="Metallica", genre="Metal", year=2023, label="Blackened"),
            Disco(id=142, title="Metallica Live At Woodstck '94", artist="Metallica", genre="Metal", year=1996, label="Elektra"),
            Disco(id=143, title="The Metallica Blacklist", artist="Metallica", genre="Metal", year=2021, label="Blackened"),
            Disco(id=144, title="Hardwired...To Self-Destruct", artist="Metallica", genre="Metal", year=2016, label="Blackened"),
            Disco(id=145, title="Death Magnetic", artist="Metallica", genre="Metal", year=2008, label="Warner Records"),
            Disco(id=146, title="St. Anger", artist="Metallica", genre="Metal", year=2003, label="Elektra"),
            Disco(id=147, title="Reload", artist="Metallica", genre="Metal", year=1997, label="Elektra"),
            Disco(id=148, title="Load", artist="Metallica", genre="Metal", year=1996, label="Elektra"),
            Disco(id=149, title="Remaining Memories: The Interview", artist="Metallica", genre="Metal", year=1996, label="Elektra"),
            Disco(id=150, title="Live S**t: Binge & Purge", artist="Metallica", genre="Metal", year=1993, label="Elektra"),
            Disco(id=151, title="Metallica", artist="Metallica", genre="Metal", year=1991, label="Elektra"),
            Disco(id=152, title="...And Justice For All", artist="Metallica", genre="Metal", year=1988, label="Elektra"),
            Disco(id=153, title="Master of Puppets", artist="Metallica", genre="Metal", year=1986, label="Elektra"),
            Disco(id=154, title="Ride The Lightning", artist="Metallica", genre="Metal", year=1984, label="Elektra")]

# ************** FUNCION GET
@router.get("/Metallica/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def metallicaclass():
    return (discos_metallica)

# ************** FUNCION POST
@router.post("/Metallica/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def metallicaclass(disco:Disco):
    for index, saved_disco in enumerate(discos_metallica):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_metallica.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/Metallica/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def metallicaclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_metallica):
        if saved_disco.id == disco.id:
            discos_metallica[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/Metallica/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def metallicaclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_metallica):
        if saved_disco.id ==id:
           del discos_metallica[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 