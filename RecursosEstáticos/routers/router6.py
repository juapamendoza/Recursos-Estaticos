from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_badbunny=[Disco(id=121, title="LAS QUE NO IBAN A SALIR", artist="Bad Bunny", genre="Latin", year=2020, label="Rimas Entertainment"),
            Disco(id=122, title="X 100PRE", artist="Bad Bunny", genre="Latin", year=2018, label="Rimas Entertainment"),
            Disco(id=123, title="OASIS", artist="Bad Bunny", genre="Latin", year=2019, label="Universal Music"),
            Disco(id=124, title="YHLQMDLG", artist="Bad Bunny", genre="Latin", year=2020, label="Rimas Entertainment"),
            Disco(id=125, title="EL ULTIMO TOUR DEL MUNDO", artist="Bad Bunny", genre="Latin", year=2020, label="Rimas Entertainment"),
            Disco(id=126, title="Un Verano Sin Ti", artist="Bad Bunny", genre="Latin", year=2022, label="Rimas Entertainment")]

# ************** FUNCION GET
@router.get("/BadBunny/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def bunnyclass():
    return (discos_badbunny)

# ************** FUNCION POST
@router.post("/BadBunny/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def bunnyclass(disco:Disco):
    for index, saved_disco in enumerate(discos_badbunny):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_badbunny.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/BadBunny/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def bunnyclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_badbunny):
        if saved_disco.id == disco.id:
            discos_badbunny[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/BadBunny/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def bunnyclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_badbunny):
        if saved_disco.id ==id:
           del discos_badbunny[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 