from pydantic import BaseModel

class banknote_schema(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float