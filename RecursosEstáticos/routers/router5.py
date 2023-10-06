from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_nata=[Disco(id=127, title="Todo Es Diferente", artist="Natanael Cano", genre="Latin", year=2019, label="Hyphy Music"),
            Disco(id=128, title="Corridos Tumbados", artist="Natanael Cano", genre="Latin", year=2019, label="Rancho Humilde"),
            Disco(id=129, title="Trap Tumbado", artist="Natanael Cano", genre="Latin", year=2020, label="Rancho Humilde"),
            Disco(id=130, title="Soy El Nata", artist="Natanael Cano", genre="Latin", year=2020, label="Rancho Humilde"),
            Disco(id=131, title="Las 3 Torres", artist="Natanael Cano", genre="Latin", year=2020, label="WEA Latina"),
            Disco(id=132, title="Mi Nuevo Yo", artist="Natanael Cano", genre="Latin", year=2019, label="Rancho Humilde"),
            Disco(id=133, title="Nata", artist="Natanael Cano", genre="Latin", year=2021, label="Rancho Humilde"),
            Disco(id=134, title="A Mis 20", artist="Natanael Cano", genre="Latin", year=2021, label="WEA Latina"),
            Disco(id=135, title="NataKong", artist="Natanael Cano", genre="Latin", year=2022, label="WEA Latina"),
            Disco(id=136, title="Nata Montana", artist="Natanael Cano", genre="Latin", year=2023, label="WEA Latina")]

# ************** FUNCION GET
@router.get("/NatanaelCano/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def nataclass():
    return (discos_nata)

# ************** FUNCION POST
@router.post("/NatanaelCano/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def nataclass(disco:Disco):
    for index, saved_disco in enumerate(discos_nata):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_nata.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/NatanaelCano/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def nataclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_nata):
        if saved_disco.id == disco.id:
            discos_nata[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/NatanaelCano/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def nataclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_nata):
        if saved_disco.id ==id:
           del discos_nata[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 