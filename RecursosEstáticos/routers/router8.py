from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class Disco(BaseModel):
    id:int
    title:str
    artist:str
    genre:str

discos_drake=[Disco(id=161, title="Her Loss", artist="Drake", genre="Hip-Hop", year=2022, label="Epic"),
            Disco(id=162, title="Honestly, Nevermind", artist="Drake", genre="Hip-Hop", year=2022, label="Republic Records"),
            Disco(id=163, title="Certified Lover Boy", artist="Drake", genre="Hip-Hop", year=2021, label="Republic Records"),
            Disco(id=164, title="Scorpion", artist="Drake", genre="Hip-Hop", year=2018, label="Young Money"),
            Disco(id=165, title="More Life", artist="Drake", genre="Hip-Hop", year=2017, label="Young Money"),
            Disco(id=166, title="Views", artist="Drake", genre="Hip-Hop", year=2016, label="Young Money"),
            Disco(id=167, title="If You're Reading This It's Too Late", artist="Drake", genre="Hip-Hop", year=2015, label="Young Money"),
            Disco(id=168, title="Nothing Was The Same", artist="Drake", genre="Hip-Hop", year=2013, label="Republic Records"),
            Disco(id=169, title="Take Care (Deluxe)", artist="Drake", genre="Hip-Hop", year=2011, label="Republic Records"),
            Disco(id=170, title="Thank Me Later", artist="Drake", genre="Hip-Hop", year=2010, label="Republic Records"),
            Disco(id=171, title="Dark Lane Demo Tapes", artist="Drake", genre="Hip-Hop", year=2020, label="Republic Records"),
            Disco(id=172, title="Care Package", artist="Drake", genre="Hip-Hop", year=2019, label="Republic Records"),
            Disco(id=173, title="What a Time To Be Alive", artist="Drake", genre="Hip-Hop", year=2015, label="Young Money"),
            Disco(id=174, title="So Far Gone", artist="Drake", genre="Hip-Hop", year=2009, label="OVO")]

# ************** FUNCION GET
@router.get("/Drake/", status_code=status.HTTP_202_ACCEPTED, response_description="Aceptado :)")
async def drakeclass():
    return (discos_drake)

# ************** FUNCION POST
@router.post("/Drake/", response_model=Disco, status_code=status.HTTP_201_CREATED, response_description="Disco creado")
async def drakeclass(disco:Disco):
    for index, saved_disco in enumerate(discos_drake):
        if saved_disco.id == disco.id: 
            raise HTTPException(status_code= status.HTTP_409_CONFLICT,detail="el disco ya existe")
    else:
        discos_drake.append(disco)
        return disco
    
# ************** FUNCION PUT
@router.put("/Drake/", response_model=Disco, status_code=status.HTTP_302_FOUND, response_description="Disco modificado")
async def drakeclass(disco:Disco):
    found=False  
    for index, saved_disco in enumerate(discos_drake):
        if saved_disco.id == disco.id:
            discos_drake[index] = disco
            found=True
    if not found:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="el disco no se modifico")
    else:
        return disco

# ************** FUNCION DELETE
@router.delete("/Drake/{id}", status_code=status.HTTP_202_ACCEPTED, response_description="Eliminado")
async def drakeclass(id:int):
    found=False
    for index, saved_disco in enumerate(discos_drake):
        if saved_disco.id ==id:
           del discos_drake[index] 
           found=True
           return "El registro se ha eliminado"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="el disco no existe")

#uvicorn [title_archivo]:[title_objeto] --reload 