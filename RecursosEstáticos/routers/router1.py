from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_taylor=[Disco(id=1, title="Midnights", artist="Taylor Swift", genre="Pop"),
            Disco(id=2, title="reputation", artist="Taylor Swift", genre="Pop"),
            Disco(id=3, title="Lover", artist="Taylor Swift", genre="Pop"),
            Disco(id=4, title="1989", artist="Taylor Swift", genre="Pop"),
            Disco(id=5, title="Taylor Swift", artist="Taylor Swift", genre="Country"),
            Disco(id=6, title="Fearless", artist="Taylor Swift", genre="Country"),
            Disco(id=7, title="Speak Now", artist="Taylor Swift", genre="Country"),
            Disco(id=8, title="Red", artist="Taylor Swift", genre="Pop"),
            Disco(id=9, title="folklore", artist="Taylor Swift", genre="Indie"),
            Disco(id=10, title="evermore", artist="Taylor Swift", genre="Indie")]

# ************** FUNCION GET
@router.get("/TaylorSwift/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def taylorclass():
    return (discos_taylor)

# ************** FUNCION POST
@router.post("/TaylorSwift/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def taylorclass(disco:Disco):
    for index, saved_disco in enumerate(discos_taylor):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_taylor.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/TaylorSwift/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def taylorclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_taylor):
        if saved_disco.id == disco.id:
            discos_taylor[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/TaylorSwift/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def taylorclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_taylor):
        if saved_disco.id ==id:
           del discos_taylor[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 