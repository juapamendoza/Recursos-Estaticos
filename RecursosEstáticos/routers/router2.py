from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_lana=[Disco(id=11, title="Did you know that there's a tunnel under Ocean Blvd", artist="Lana del Rey", genre="Alternative", year=2023, label="Interscope Records"),
            Disco(id=12, title="Blue Banisters", artist="Lana del Rey", genre="Alternative", year=2021, label="Interscope Records"),
            Disco(id=13, title="Chemtrails Over The Country Club", artist="Lana del Rey", genre="Alternative", year=2021, label="Interscope Records"),
            Disco(id=14, title="Norman Fucking Rockwell", artist="Lana del Rey", genre="Alternative", year=2019, label="Interscope Records"),
            Disco(id=15, title="Lust For Life", artist="Lana del Rey", genre="Alternative", year=2017, label="Interscope Records"),
            Disco(id=16, title="Honeymoon", artist="Lana del Rey", genre="Alternative", year=2015, label="Interscope Records"),
            Disco(id=17, title="Ultraviolence", artist="Lana del Rey", genre="Alternative", year=2014, label="Interscope Records"),
            Disco(id=18, title="Born to Die", artist="Lana del Rey", genre="Alternative", year=2012, label="Interscope Records"),
            Disco(id=19, title="Paradise", artist="Lana del Rey", genre="Alternative", year=2012, label="Interscope Records")]

# ************** FUNCION GET
@router.get("/LanaDelRey/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def lanaclass():
    return (discos_lana)

# ************** FUNCION POST
@router.post("/LanaDelRey/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def lanaclass(disco:Disco):
    for index, saved_disco in enumerate(discos_lana):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_lana.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/LanaDelRey/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def lanaclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_lana):
        if saved_disco.id == disco.id:
            discos_lana[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/LanaDelRey/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def lanaclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_lana):
        if saved_disco.id ==id:
           del discos_lana[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 