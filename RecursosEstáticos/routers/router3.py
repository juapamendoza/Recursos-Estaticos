from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_poppy=[Disco(id=24, title="Bubblebath", artist="Poppy", genre="Pop", year=2016, label="Island Records"),
            Disco(id=25, title="Poppy.Computer", artist="Poppy", genre="Pop", year=2017, label="Mad Decent"),
            Disco(id=26, title="Am I a Girl?", artist="Poppy", genre="Pop", year=2018, label="Mad Decent"),
            Disco(id=27, title="Choke", artist="Poppy", genre="Experimental", year=2019, label="Mad Deent"),
            Disco(id=28, title="I Disagree", artist="Poppy", genre="Rock", year=2020, label="Sumerian Records"),
            Disco(id=29, title="A Very Poppy Christmas", artist="Poppy", genre="Rock", year=2020, label="Sumerian Records"),
            Disco(id=30, title="EAT (NXT Soundtrack)", artist="Poppy", genre="Rock", year=2021, label="Sumerian Records"),
            Disco(id=31, title="Flux", artist="Poppy", genre="Rock", year=2021, label="Sumerian Records"),
            Disco(id=32, title="Stagger", artist="Poppy", genre="Rock", year=2022, label="Republic Records"),
            Disco(id=33, title="Knockoff", artist="Poppy", genre="Rock", year=2023, label="Republic Records")]

# ************** FUNCION GET
@router.get("/Poppy/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def poppyclass():
    return (discos_poppy)

# ************** FUNCION POST
@router.post("/Poppy/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def poppyclass(disco:Disco):
    for index, saved_disco in enumerate(discos_poppy):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_poppy.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/Poppy/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def poppyclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_poppy):
        if saved_disco.id == disco.id:
            discos_poppy[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/Poppy/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def poppyclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_poppy):
        if saved_disco.id ==id:
           del discos_poppy[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 